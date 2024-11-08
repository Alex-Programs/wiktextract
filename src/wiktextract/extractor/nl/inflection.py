import re
from dataclasses import dataclass

from wikitextprocessor import NodeKind, TemplateNode, WikiNode

from ...page import clean_node
from ...wxr_context import WiktextractContext
from .models import Form, WordEntry
from .tags import translate_raw_tags


def extract_inflection_template(
    wxr: WiktextractContext, word_entry: WordEntry, t_node: TemplateNode
) -> None:
    if t_node.template_name in ["-nlnoun-", "adjcomp"]:
        extract_noun_adj_table(wxr, word_entry, t_node)
    elif t_node.template_name == "-nlstam-":
        extract_nlstam_template(wxr, word_entry, t_node)


def extract_noun_adj_table(
    wxr: WiktextractContext, word_entry: WordEntry, t_node: TemplateNode
) -> None:
    # https://nl.wiktionary.org/wiki/Sjabloon:-nlnoun-
    # https://nl.wiktionary.org/wiki/Sjabloon:adjcomp
    expanded_node = wxr.wtp.parse(
        wxr.wtp.node_to_wikitext(t_node), expand_all=True
    )
    column_headers = []
    for table_node in expanded_node.find_child(NodeKind.TABLE):
        for row_node in table_node.find_child(NodeKind.TABLE_ROW):
            for header_node in row_node.find_child(NodeKind.TABLE_HEADER_CELL):
                header_text = clean_node(wxr, None, header_node)
                if header_text != "":
                    column_headers.append(header_text)
            row_header = ""
            for col_index, data_node in enumerate(
                row_node.find_child(NodeKind.TABLE_CELL)
            ):
                if col_index == 0:
                    row_header = clean_node(wxr, None, data_node)
                else:
                    for form_str in clean_node(
                        wxr, None, data_node
                    ).splitlines():
                        if form_str not in ["", "-", wxr.wtp.title]:
                            form = Form(form=form_str)
                            if row_header not in ["", "naamwoord", "demoniem"]:
                                form.raw_tags.append(row_header)
                            if col_index - 1 < len(column_headers):
                                form.raw_tags.append(
                                    column_headers[col_index - 1]
                                )
                            translate_raw_tags(form)
                            word_entry.forms.append(form)

    for link_node in expanded_node.find_child(NodeKind.LINK):
        clean_node(wxr, word_entry, link_node)


def extract_nlstam_template(
    wxr: WiktextractContext, word_entry: WordEntry, t_node: TemplateNode
) -> None:
    # verb table
    # https://nl.wiktionary.org/wiki/Sjabloon:-nlstam-
    for arg in [2, 3]:
        form_str = clean_node(
            wxr, None, t_node.template_parameters.get(arg, "")
        )
        if form_str != "":
            form = Form(
                form=form_str,
                ipa=clean_node(
                    wxr, None, t_node.template_parameters.get(arg + 3, "")
                ),
            )
            form.tags.extend(["past"] if arg == 2 else ["past", "participle"])
            word_entry.forms.append(form)
    clean_node(wxr, word_entry, t_node)
    extract_vervoeging_page(wxr, word_entry)


def extract_vervoeging_page(
    wxr: WiktextractContext, word_entry: WordEntry
) -> None:
    page = wxr.wtp.get_page(f"{wxr.wtp.title}/vervoeging", 0)
    if page is None:
        return
    root = wxr.wtp.parse(page.body)
    for t_node in root.find_child(NodeKind.TEMPLATE):
        if t_node.template_name == "-nlverb-":
            extract_nlverb_template(wxr, word_entry, t_node)


@dataclass
class TableHeader:
    text: str
    col_index: int
    colspan: int
    row_index: int
    rowspan: int


NLVERB_HEADER_PREFIXES = {
    "vervoeging van de bedrijvende vorm van": ["active"],
    "onpersoonlijke lijdende vorm": ["impersonal", "passive"],
    "lijdende vorm": ["passive"],
}


def extract_nlverb_template(
    wxr: WiktextractContext, word_entry: WordEntry, t_node: TemplateNode
) -> None:
    # https://nl.wiktionary.org/wiki/Sjabloon:-nlverb-
    expanded_node = wxr.wtp.parse(
        wxr.wtp.node_to_wikitext(t_node), expand_all=True
    )
    for link_node in expanded_node.find_child(NodeKind.LINK):
        clean_node(wxr, word_entry, link_node)
    for table_node in expanded_node.find_child(NodeKind.TABLE):
        row_index = 0
        shared_tags = []
        shared_raw_tags = []
        last_row_all_header = False
        col_headers = []
        row_headers = []
        for row_node in table_node.find_child(NodeKind.TABLE_ROW):
            col_index = 0
            for row_header in row_headers:
                if (
                    row_index >= row_header.row_index
                    and row_index < row_header.row_index + row_header.rowspan
                ):
                    col_index += row_header.rowspan

            current_row_all_header = all(
                nlverb_table_cell_is_header(n)
                for n in row_node.find_child(
                    NodeKind.TABLE_HEADER_CELL | NodeKind.TABLE_CELL
                )
            )
            if current_row_all_header and not last_row_all_header:
                row_index = 0
                shared_tags.clear()
                shared_raw_tags.clear()
                col_headers.clear()
                row_headers.clear()

            is_row_first_node = True
            for cell_node in row_node.find_child(
                NodeKind.TABLE_HEADER_CELL | NodeKind.TABLE_CELL
            ):
                cell_colspan = 1
                cell_colspan_str = cell_node.attrs.get("colspan", "1")
                if re.fullmatch(r"\d+", cell_colspan_str):
                    cell_colspan = int(cell_colspan_str)
                cell_rowspan = 1
                cell_rowspan_str = cell_node.attrs.get("rowspan", "1")
                if re.fullmatch(r"\d+", cell_rowspan_str):
                    cell_rowspan = int(cell_rowspan_str)
                cell_str = clean_node(wxr, None, cell_node).strip("| ")
                if cell_str in ["", wxr.wtp.title]:
                    col_index += cell_colspan
                    is_row_first_node = False
                    continue
                if nlverb_table_cell_is_header(cell_node):
                    for (
                        header_prefix,
                        prefix_tags,
                    ) in NLVERB_HEADER_PREFIXES.items():
                        if cell_str.startswith(header_prefix):
                            shared_tags.extend(prefix_tags)
                            break
                    else:
                        if current_row_all_header:
                            if is_row_first_node:
                                shared_raw_tags.append(cell_str)
                            else:
                                col_headers.append(
                                    TableHeader(
                                        cell_str,
                                        col_index,
                                        cell_colspan,
                                        row_index,
                                        cell_rowspan,
                                    )
                                )
                        else:
                            if "(" in cell_str:
                                cell_str = cell_str[
                                    : cell_str.index("(")
                                ].strip()
                            row_headers.append(
                                TableHeader(
                                    cell_str,
                                    col_index,
                                    cell_colspan,
                                    row_index,
                                    cell_rowspan,
                                )
                            )
                else:
                    form = Form(
                        form=cell_str,
                        tags=shared_tags,
                        raw_tags=shared_raw_tags,
                        source=f"{wxr.wtp.title}/vervoeging",
                    )
                    for row_header in row_headers:
                        if (
                            row_index >= row_header.row_index
                            and row_index
                            < row_header.row_index + row_header.rowspan
                        ):
                            form.raw_tags.append(row_header.text)
                    for col_header in col_headers:
                        if (
                            col_index >= col_header.col_index
                            and col_index
                            < col_header.col_index + col_header.colspan
                        ):
                            form.raw_tags.append(col_header.text)
                    translate_raw_tags(form)
                    word_entry.forms.append(form)

                col_index += cell_colspan
                is_row_first_node = False

            row_index += 1
            last_row_all_header = current_row_all_header


def nlverb_table_cell_is_header(node: WikiNode) -> bool:
    return (
        node.kind == NodeKind.TABLE_HEADER_CELL
        or node.attrs.get("class", "") == "infoboxrijhoofding"
    )
