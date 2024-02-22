import logging
from typing import Union

from mediawiki_langcodes import name_to_code
from wikitextprocessor import NodeKind, WikiNode
from wikitextprocessor.parser import LevelNode
from wiktextract.extractor.de.models import WordEntry
from wiktextract.wxr_context import WiktextractContext

from .example import extract_examples
from .gloss import extract_glosses
from .linkage import extract_linkages
from .pronunciation import extract_pronunciation
from .section_titles import POS_SECTIONS
from .translation import extract_translation

# Templates that are used to form panels on pages and that should be ignored in
# various positions
PANEL_TEMPLATES = set()

# Template name prefixes used for language-specific panel templates (i.e.,
# templates that create side boxes or notice boxes or that should generally
# be ignored).
PANEL_PREFIXES = set()

# Additional templates to be expanded in the pre-expand phase
ADDITIONAL_EXPAND_TEMPLATES = {"NoCat"}


def parse_section(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    base_data: WordEntry,
    level_node_or_children: Union[WikiNode, list[Union[WikiNode, str]]],
) -> None:
    # Page structure: https://de.wiktionary.org/wiki/Hilfe:Formatvorlage
    if isinstance(level_node_or_children, list):
        for x in level_node_or_children:
            parse_section(wxr, page_data, base_data, x)
        return

    elif not isinstance(level_node_or_children, WikiNode):
        if (
            not isinstance(level_node_or_children, str)
            or not level_node_or_children.strip() == ""
        ):
            wxr.wtp.debug(
                f"Unexpected node type in parse_section: {level_node_or_children}",
                sortid="extractor/de/page/parse_section/31",
            )
        return

    # Level 3 headings are used to start POS sections like
    # === {{Wortart|Verb|Deutsch}} ===
    elif level_node_or_children.kind == NodeKind.LEVEL3:
        for template_node in level_node_or_children.find_content(
            NodeKind.TEMPLATE
        ):
            # German Wiktionary uses a `Wortart` template to define the POS
            if template_node.template_name == "Wortart":
                process_pos_section(
                    wxr,
                    page_data,
                    base_data,
                    level_node_or_children,
                    template_node,
                )
        return

    # Level 4 headings were introduced by overriding the default templates.
    # See overrides/de.json for details.
    elif level_node_or_children.kind == NodeKind.LEVEL4:
        section_name = level_node_or_children.largs[0][0]
        wxr.wtp.start_subsection(section_name)
        if not len(page_data) > 0:
            wxr.wtp.debug(
                f"Reached section without extracting some page data first: {level_node_or_children}",
                sortid="extractor/de/page/parse_section/55",
            )
            return
        if section_name == "Bedeutungen":
            extract_glosses(wxr, page_data[-1], level_node_or_children)
        elif wxr.config.capture_pronunciation and section_name == "Aussprache":
            extract_pronunciation(wxr, page_data[-1], level_node_or_children)
        elif wxr.config.capture_examples and section_name == "Beispiele":
            extract_examples(wxr, page_data[-1], level_node_or_children)
        elif (
            wxr.config.capture_translations and section_name == "Übersetzungen"
        ):
            extract_translation(wxr, page_data[-1], level_node_or_children)
        elif (
            wxr.config.capture_linkages
            and section_name in wxr.config.LINKAGE_SUBTITLES
        ):
            extract_linkages(wxr, page_data[-1], level_node_or_children)


FORM_POS = {
    "Konjugierte Form",
    "Deklinierte Form",
    "Dekliniertes Gerundivum",
    "Komparativ",
    "Superlativ",
    "Supinum",
    "Partizip",
    "Partizip I",
    "Partizip II",
    "Erweiterter Infinitiv",
    "Adverbialpartizip",
    "Exzessiv",
    "Gerundium",
}

IGNORE_POS = {"Albanisch", "Pseudopartizip", "Ajami"}


def process_pos_section(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    base_data: WordEntry,
    level_node: LevelNode,
    pos_template_node: WikiNode,
) -> None:
    # Extract the POS
    pos_argument = pos_template_node.template_parameters.get(1)
    if pos_argument in IGNORE_POS:
        return
    if pos_argument in FORM_POS:
        # XXX: Extract form from form pages. Investigate first if this is needed
        # at all or redundant with form tables.
        return

    pos = ""
    if pos_argument in POS_SECTIONS:
        pos = POS_SECTIONS[pos_argument]["pos"]
    else:
        wxr.wtp.debug(
            f"Unknown POS type: {pos_argument}",
            sortid="extractor/de/page/process_pos_section/55",
        )
    base_data.pos = pos
    page_data.append(base_data.model_copy(deep=True))

    wxr.wtp.start_section(page_data[-1].lang_code + "_" + pos)

    # There might be other templates in the level node that define grammatical
    # features other than the POS. Extract them here.
    for template_node in level_node.find_content(NodeKind.TEMPLATE):
        template_name = template_node.template_name

        GENDER_TAGS_TEMPLATES = {
            "m",
            "f",
            "f ",
            "n",
            "n ",
            "mf",
            "mn.",
            "fn",
            "fm",
            "nf",
            "nm",
            "mfn",
            "u",
            "un",
            "Geschlecht",  # placeholder template
        }

        VERB_TAGS_TEMPLATES = {
            "unreg.",
            "intrans.",
            "trans.",
            "refl.",
        }

        ARAB_VERB_STEM_TEMPLATES = {
            "Grundstamm",
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
        }

        NOUN_TAGS_TEMPLATES = {
            "adjektivische Deklination",
            "kPl.",
            "Pl.",
            "mPl.",
            "fPl.",
            "nPl.",
            "Sachklasse",
            "Personenklasse",
            "indekl.",
            "Suaheli Klassen",
        }

        if template_name == "Wortart":
            continue

        elif template_name in GENDER_TAGS_TEMPLATES.union(
            ARAB_VERB_STEM_TEMPLATES
        ).union(NOUN_TAGS_TEMPLATES).union(VERB_TAGS_TEMPLATES):
            # XXX: de: Extract additional grammatical markers
            pass

        else:
            wxr.wtp.debug(
                f"Unexpected template in POS section heading: {template_node}",
                sortid="extractor/de/page/process_pos_section/31",
            )

    for level_4_node in level_node.find_child(NodeKind.LEVEL4):
        parse_section(wxr, page_data, base_data, level_4_node)

    for non_l4_node in level_node.invert_find_child(NodeKind.LEVEL4):
        if (
            isinstance(non_l4_node, WikiNode)
            and non_l4_node.kind == NodeKind.TEMPLATE
            and "Übersicht" in non_l4_node.template_name
        ):
            # XXX: de: Extract form table templates
            pass
        elif (
            isinstance(non_l4_node, WikiNode)
            and non_l4_node.kind == NodeKind.TABLE
            and "inflection-table" in non_l4_node.attrs.get("class")
        ):
            # XXX: de: Extract html form table
            pass
        elif (
            isinstance(non_l4_node, WikiNode)
            and non_l4_node.kind == NodeKind.LINK
            and len(non_l4_node.largs) > 0
            and len(non_l4_node.largs[0]) > 0
            and "Kategorie" in non_l4_node.largs[0][0]
        ):
            # XXX Process categories
            pass
        else:
            wxr.wtp.debug(
                f"Unexpected node in pos section: {non_l4_node}",
                sortid="extractor/de/page/process_pos_section/41",
            )
    return


def parse_page(
    wxr: WiktextractContext, page_title: str, page_text: str
) -> list[dict[str, any]]:
    if wxr.config.verbose:
        logging.info(f"Parsing page: {page_title}")

    wxr.config.word = page_title
    wxr.wtp.start_page(page_title)

    # Parse the page, pre-expanding those templates that are likely to
    # influence parsing
    tree = wxr.wtp.parse(
        page_text,
        pre_expand=True,
        additional_expand=ADDITIONAL_EXPAND_TEMPLATES,
    )

    page_data: list[WordEntry] = []
    for level2_node in tree.find_child(NodeKind.LEVEL2):
        for subtitle_template in level2_node.find_content(NodeKind.TEMPLATE):
            # The language sections are marked with
            # == <title> ({{Sprache|<lang>}}) ==
            # where <title> is the title of the page and <lang> is the
            # German name of the language of the section.
            if subtitle_template.template_name == "Sprache":
                lang = subtitle_template.template_parameters.get(1)
                lang_code = name_to_code(lang, "de")
                if lang_code == "":
                    wxr.wtp.warning(
                        f"Unknown language: {lang}",
                        sortid="extractor/de/page/parse_page/76",
                    )
                if (
                    wxr.config.capture_language_codes is not None
                    and lang_code not in wxr.config.capture_language_codes
                ):
                    continue

                base_data = WordEntry(
                    lang=lang, lang_code=lang_code, word=wxr.wtp.title
                )
                parse_section(wxr, page_data, base_data, level2_node.children)

    return [d.model_dump(exclude_defaults=True) for d in page_data]
