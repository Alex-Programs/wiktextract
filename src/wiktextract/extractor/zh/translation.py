import re
from typing import Optional, Union

from mediawiki_langcodes import name_to_code
from wikitextprocessor import NodeKind, WikiNode
from wiktextract.page import LEVEL_KINDS, clean_node
from wiktextract.wxr_context import WiktextractContext

from ..share import capture_text_in_parentheses
from .models import Translation, WordEntry


def extract_translation(
    wxr: WiktextractContext, page_data: list[WordEntry], node: WikiNode
) -> None:
    sense_text = ""
    for child in node.children:
        if isinstance(child, WikiNode):
            if child.kind == NodeKind.TEMPLATE:
                template_name = child.template_name.lower()
                if (
                    template_name in {"trans-top", "翻譯-頂", "trans-top-also"}
                    and 1 in child.template_parameters
                ):
                    sense_text = clean_node(
                        wxr, None, child.template_parameters.get(1)
                    )
                elif template_name == "checktrans-top":
                    return
                elif template_name == "see translation subpage":
                    translation_subpage(
                        wxr, page_data, child.template_parameters
                    )
            elif child.kind == NodeKind.LIST:
                for list_item_node in child.find_child(NodeKind.LIST_ITEM):
                    if not list_item_node.contain_node(NodeKind.LIST):
                        process_translation_list_item(
                            wxr,
                            page_data,
                            clean_node(wxr, None, list_item_node.children),
                            sense_text,
                        )
                    else:
                        nested_list_index = 0
                        for index, item_child in enumerate(
                            list_item_node.children
                        ):
                            if (
                                isinstance(item_child, WikiNode)
                                and item_child.kind == NodeKind.LIST
                            ):
                                nested_list_index = index
                                break

                        process_translation_list_item(
                            wxr,
                            page_data,
                            clean_node(
                                wxr,
                                None,
                                list_item_node.children[:nested_list_index],
                            ),
                            sense_text,
                        )
                        for nested_list_node in list_item_node.find_child(
                            NodeKind.LIST
                        ):
                            for nested_list_item in nested_list_node.find_child(
                                NodeKind.LIST_ITEM
                            ):
                                process_translation_list_item(
                                    wxr,
                                    page_data,
                                    clean_node(
                                        wxr, None, nested_list_item.children
                                    ),
                                    sense_text,
                                )


def process_translation_list_item(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    expanded_text: str,
    sense: str,
) -> None:
    from .headword_line import GENDERS

    split_results = re.split(r":|：", expanded_text, maxsplit=1)
    if len(split_results) != 2:
        return
    lang_text, words_text = split_results
    lang_text = lang_text.strip()
    words_text = words_text.strip()
    if len(words_text) == 0:
        return
    lang_code = name_to_code(lang_text, "zh")

    # split words by `,` or `;` that are not inside `()`
    for word_and_tags in re.split(r"[,;、](?![^(]*\))\s*", words_text):
        tags, word = capture_text_in_parentheses(word_and_tags)
        tags = [tag for tag in tags if tag != lang_code]  # rm Wiktionary link
        translation_data = Translation(
            lang_code=lang_code, lang_name=lang_text, word=word
        )
        tags_without_roman = []
        for tag in tags:
            if re.search(r"[a-z]", tag):
                translation_data.roman = tag
            else:
                tags_without_roman.append(tag)

        if len(tags_without_roman) > 0:
            translation_data.tags = tags_without_roman

        gender = word.split(" ")[-1]
        if gender in GENDERS:
            translation_data.word = word.removesuffix(f" {gender}")
            translation_data.tags.append(GENDERS.get(gender))

        if len(sense) > 0:
            translation_data.sense = sense
        page_data[-1].translations.append(translation_data)


def translation_subpage(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    template_args: dict[str, str],
) -> None:
    from .page import ADDITIONAL_EXPAND_TEMPLATES

    page_title = wxr.wtp.title
    target_section = None
    if len(template_args) > 0:
        target_section = template_args.get(1)
    if len(template_args) > 1:
        page_title = template_args.get(2)

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
    if isinstance(node, WikiNode):
        if node.kind in LEVEL_KINDS:
            section_title = clean_node(wxr, None, node.largs)
            if (
                isinstance(target_section, str)
                and section_title == target_section
            ):
                return node
            if (
                isinstance(target_section, list)
                and section_title in target_section
            ):
                return node

        for child in node.children:
            returned_node = find_subpage_section(wxr, child, target_section)
            if returned_node is not None:
                return returned_node
    return None
