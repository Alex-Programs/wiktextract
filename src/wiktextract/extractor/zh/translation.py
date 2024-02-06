from typing import Optional, Union

from mediawiki_langcodes import code_to_name, name_to_code
from wikitextprocessor import NodeKind, WikiNode
from wikitextprocessor.parser import LEVEL_KIND_FLAGS, TemplateNode
from wiktextract.page import clean_node
from wiktextract.wxr_context import WiktextractContext

from .models import Translation, WordEntry


def extract_translation(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    level_node: WikiNode,
    sense: str = "",
) -> None:
    for child in level_node.find_child(NodeKind.TEMPLATE | NodeKind.LIST):
        if isinstance(child, TemplateNode):
            template_name = child.template_name.lower()
            if (
                template_name in {"trans-top", "翻譯-頂", "trans-top-also"}
                and 1 in child.template_parameters
            ):
                sense = clean_node(wxr, None, child.template_parameters.get(1))
            elif template_name in {"see translation subpage", "trans-see"}:
                translation_subpage(wxr, page_data, child)
            elif template_name == "multitrans":
                wikitext = "".join(
                    wxr.wtp.node_to_wikitext(c)
                    for c in child.template_parameters.get("data", [])
                )
                multitrans = wxr.wtp.parse(wikitext)
                extract_translation(wxr, page_data, multitrans, sense)
        else:
            for list_item in child.find_child_recursively(NodeKind.LIST_ITEM):
                process_translation_list_item(
                    wxr,
                    page_data,
                    list_item,
                    sense,
                )


def process_translation_list_item(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    list_item: WikiNode,
    sense: str,
) -> None:
    tr_data = Translation(word="", sense=sense)

    for child_index, child in enumerate(list_item.filter_empty_str_child()):
        if child_index == 0:
            lang_text = ""
            if isinstance(child, str):
                if "：" in child:
                    lang_text = child[: child.index("：")]
                elif ":" in child:
                    lang_text = child[: child.index(":")]
            else:
                lang_text = clean_node(wxr, None, child)
            if len(lang_text) > 0:
                tr_data.lang = lang_text.strip()
                tr_data.lang_code = name_to_code(tr_data.lang, "zh")
        elif isinstance(child, TemplateNode):
            template_name = child.template_name.lower()
            if template_name in {
                "t",
                "t+",
                "tt",
                "tt+",
                "t-check",
                "t+check",
                "l",
            }:
                if len(tr_data.word) > 0:
                    page_data[-1].translations.append(
                        tr_data.model_copy(deep=True)
                    )
                    tr_data = Translation(
                        word="",
                        lang=tr_data.lang,
                        lang_code=tr_data.lang_code,
                        sense=sense,
                    )
                if tr_data.lang_code == "":
                    tr_data.lang_code = child.template_parameters.get(1, "")
                if tr_data.lang == "":
                    tr_data.lang = code_to_name(tr_data.lang_code, "zh")
                tr_data.word = clean_node(
                    wxr, None, child.template_parameters.get(2, "")
                )
                tr_data.roman = clean_node(
                    wxr, None, child.template_parameters.get("tr", "")
                )
                tr_data.alt = clean_node(
                    wxr, None, child.template_parameters.get("alt", "")
                )
                tr_data.lit = clean_node(
                    wxr, None, child.template_parameters.get("lit", "")
                )
                # find gender tags
                expanded_template = wxr.wtp.parse(
                    wxr.wtp.node_to_wikitext(child), expand_all=True
                )
                for span_node in expanded_template.find_html("span"):
                    class_str = span_node.attrs.get("class", "")
                    if "gender" in class_str:
                        for abbr_tag in span_node.find_html("abbr"):
                            if len(abbr_tag.attrs.get("title")) > 0:
                                tr_data.tags.append(
                                    clean_node(
                                        wxr, None, abbr_tag.attrs.get("title")
                                    )
                                )
                    elif tr_data.roman == "" and class_str.startswith("tr "):
                        tr_data.roman = clean_node(wxr, None, span_node)
            elif template_name == "t-needed":
                # ignore empty translation
                continue
            else:
                # qualifier template
                expanded_template = wxr.wtp.parse(
                    wxr.wtp.node_to_wikitext(child), expand_all=True
                )
                find_title = False
                for span_node in expanded_template.find_html("span"):
                    tag = span_node.attrs.get("title", "")
                    if len(tag) > 0:
                        tr_data.tags.append(tag.strip())
                        find_title = True
                if not find_title:
                    tag = clean_node(wxr, None, child)
                    if len(tag) > 0:
                        tr_data.tags.append(tag.strip("()"))
        elif isinstance(child, WikiNode) and child.kind == NodeKind.LINK:
            if len(tr_data.word) > 0:
                page_data[-1].translations.append(tr_data.model_copy(deep=True))
                tr_data = Translation(
                    word="",
                    lang=tr_data.lang,
                    lang_code=tr_data.lang_code,
                    sense=sense,
                )
            tr_data.word = clean_node(wxr, None, child)

    if len(tr_data.word) > 0:
        page_data[-1].translations.append(tr_data.model_copy(deep=True))


def translation_subpage(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    template_node: TemplateNode,
) -> None:
    # https://zh.wiktionary.org/wiki/Template:翻譯-見
    # https://zh.wiktionary.org/wiki/Template:See_translation_subpage
    from .page import ADDITIONAL_EXPAND_TEMPLATES

    page_title = wxr.wtp.title
    target_section = None
    if template_node.template_name == "see translation subpage":
        target_section = template_node.template_parameters.get(1)
    page_title = template_node.template_parameters.get(2, wxr.wtp.title)

    translation_subpage_title = page_title
    if page_title == wxr.wtp.title:
        translation_subpage_title = f"{page_title}/翻譯"
    subpage = wxr.wtp.get_page(translation_subpage_title)
    if subpage is None:
        return

    root = wxr.wtp.parse(
        subpage.body,
        pre_expand=True,
        additional_expand=ADDITIONAL_EXPAND_TEMPLATES,
    )
    target_section_node = (
        root
        if target_section is None
        else find_subpage_section(wxr, root, target_section)
    )
    translation_node = find_subpage_section(
        wxr, target_section_node, wxr.config.OTHER_SUBTITLES["translations"]
    )
    if translation_node is not None:
        extract_translation(wxr, page_data, translation_node)


def find_subpage_section(
    wxr: WiktextractContext,
    node: Union[WikiNode, str],
    target_section: Union[str, list[str]],
) -> Optional[WikiNode]:
    if not isinstance(node, WikiNode):
        return None
    for level_node in node.find_child_recursively(LEVEL_KIND_FLAGS):
        section_title = clean_node(wxr, None, level_node.largs)
        if isinstance(target_section, str) and section_title == target_section:
            return level_node
        if isinstance(target_section, list) and section_title in target_section:
            return level_node
    return None