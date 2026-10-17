"""
Koshur Research & Computational Linguistics Package.
Fieldwork glossing, corpus dataset exports (CoNLL-U, TEI-XML, JSON-LD),
and quantitative typological metrics for the Kashmiri language.
"""

from koshur.research.glossing import (
    GLOSSING_TAGS,
    generate_leipzig_gloss,
    get_gloss_tag_description
)
from koshur.research.corpus import (
    export_conllu,
    export_tei_xml,
    export_jsonld
)
from koshur.research.metrics import (
    count_syllables_kashmiri,
    compute_lexical_metrics,
    verify_v2_word_order
)
from koshur.research.sources import (
    HISTORICAL_SOURCES,
    get_research_sources,
    search_research_sources
)

__all__ = [
    "GLOSSING_TAGS",
    "generate_leipzig_gloss",
    "get_gloss_tag_description",
    "export_conllu",
    "export_tei_xml",
    "export_jsonld",
    "count_syllables_kashmiri",
    "compute_lexical_metrics",
    "verify_v2_word_order",
    "HISTORICAL_SOURCES",
    "get_research_sources",
    "search_research_sources",
]
