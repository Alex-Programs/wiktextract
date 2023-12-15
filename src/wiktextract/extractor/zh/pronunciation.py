import re
from typing import Optional, Union

from wikitextprocessor import NodeKind, WikiNode
from wikitextprocessor.parser import HTMLNode, TemplateNode
from wiktextract.extractor.share import create_audio_url_dict
from wiktextract.page import clean_node
from wiktextract.wxr_context import WiktextractContext

from .models import Sound, WordEntry
from .util import append_base_data


def extract_pronunciation_recursively(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    base_data: WordEntry,
    lang_code: str,
    node: Union[WikiNode, list[Union[WikiNode, str]]],
    tags: list[str],
) -> None:
    if isinstance(node, list):
        for x in node:
            extract_pronunciation_recursively(
                wxr, page_data, base_data, lang_code, x, tags
            )
        return
    if not isinstance(node, WikiNode):
        return
    if node.kind == NodeKind.LIST_ITEM:
        if not node.contain_node(NodeKind.LIST):
            used_children = node.children
            rest_children = []
        else:
            used_children = list(node.invert_find_child(NodeKind.LIST))
            rest_children = list(node.find_child(NodeKind.LIST))
        data = extract_pronunciation_item(
            wxr, page_data, lang_code, used_children, tags
        )
        if isinstance(data, str):  # is audio file name
            # audio file usually after Pinyin
            # add back to previous Pinyin dictionary if it doesn't have
            # audio file data and they are sibling nodes(similar tags).
            last_sounds_list = page_data[-1].sounds
            for index in range(len(last_sounds_list)):
                if last_sounds_list[index].audio == "" and (
                    tags == last_sounds_list[index].tags[:-1]
                    or lang_code != "zh"
                ):
                    for key, value in create_audio_url_dict(data).items():
                        if key in Sound.model_fields:
                            setattr(page_data[-1].sounds[index], key, value)
                        else:
                            wxr.wtp.warning(
                                f"{key=} not defined in Sound",
                                sortid="zh.pronunciation/56",
                            )
        elif isinstance(data, Sound):
            append_base_data(
                page_data,
                "sounds",
                data,
                base_data,
            )
            # list children could contain audio file
            extract_pronunciation_recursively(
                wxr,
                page_data,
                base_data,
                lang_code,
                rest_children,
                data.tags[:-1],
            )
        elif isinstance(data, list):
            # list item is a tag
            extract_pronunciation_recursively(
                wxr,
                page_data,
                base_data,
                lang_code,
                rest_children,
                data,
            )
    else:
        extract_pronunciation_recursively(
            wxr, page_data, base_data, lang_code, node.children, tags
        )


def combine_pronunciation_tags(
    old_tags: list[str], new_tags: list[str]
) -> list[str]:
    combined_tags = old_tags[:]
    old_tags_set = set(old_tags)
    for tag in new_tags:
        if tag not in old_tags_set:
            combined_tags.append(tag)
    return combined_tags


def split_pronunciation_tags(text: str) -> list[str]:
    return list(
        filter(
            None,
            re.split(
                r"，|, | \(|\) ?|和|包括|: |、",
                text.removesuffix("^((幫助))")  # remove help link
                # remove link to page "Wiktionary:漢語發音表記"
                .removesuffix("(維基詞典)").strip("（）()⁺\n "),
            ),
        )
    )


def extract_pronunciation_item(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    lang_code: str,
    node_children: list[WikiNode],
    tags: list[str],
) -> Optional[Union[Sound, str, list[str]]]:
    """
    Return audio file name(eg. "File:LL-Q1860 (eng)-Vealhurl-manga.wav") string
    or a dictionary contains IPA and tags
    or a list of tags
    """
    expanded_text = clean_node(wxr, None, node_children)
    # remove Dungan language pronunciation warning from "Module:Zh-pron"
    expanded_text = expanded_text.removesuffix(
        "(注意：東干語發音目前仍處於實驗階段，可能會不準確。)"
    )

    if expanded_text.startswith("File:"):
        return expanded_text
    elif expanded_text.startswith("(福建: "):
        # it's a tag
        return combine_pronunciation_tags(
            tags, split_pronunciation_tags(expanded_text)
        )
    elif expanded_text.startswith(("同音詞", "同音词")):
        process_homophone_data(wxr, page_data, node_children, tags)
    else:
        sound_tags_text, *ipa = re.split(r"：|:", expanded_text, 1)
        new_tags = combine_pronunciation_tags(
            tags, split_pronunciation_tags(sound_tags_text)
        )
        if len(ipa) > 0:
            data = Sound(tags=new_tags)
            ipa_key = "zh_pron" if lang_code == "zh" else "ipa"
            setattr(data, ipa_key, ipa[0].strip())
            return data

        for child in filter(
            lambda x: isinstance(x, WikiNode) and x.kind == NodeKind.TEMPLATE,
            node_children,
        ):
            if child.template_name == "audio":
                return child.template_parameters.get(2)

        return new_tags


def process_homophone_data(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    node_children: list[WikiNode],
    tags: list[str],
) -> None:
    # Process the collapsible homophone table created from "zh-pron" template
    # and the "homophones" template
    tags = combine_pronunciation_tags(tags, ["同音詞"])
    for node in node_children:
        if isinstance(node, HTMLNode) and node.tag == "table":
            for span_node in node.find_html_recursively(
                "span", attr_name="lang"
            ):
                sound_data = Sound(
                    homophone=clean_node(wxr, None, span_node), tags=tags
                )
                page_data[-1].sounds.append(sound_data)
        elif (
            isinstance(node, TemplateNode)
            and node.template_name == "homophones"
        ):
            expaned_template = wxr.wtp.parse(
                wxr.wtp.node_to_wikitext(node), expand_all=True
            )
            for span_node in expaned_template.find_html_recursively(
                "span", attr_name="lang"
            ):
                sound_data = Sound(
                    homophone=clean_node(wxr, None, span_node), tags=tags
                )
                page_data[-1].sounds.append(sound_data)
