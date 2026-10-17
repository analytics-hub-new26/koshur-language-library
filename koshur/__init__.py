"""
Koshur: A Comprehensive Computational Linguistics, Application Development,
and Digital Preservation Toolkit for the Kashmiri Language (कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳).

Features:
- Multi-Script Support & Bidirectional Transliteration:
  * Sharada (𑆯𑆳𑆫𑆢𑆳) - Historic native script of Kashmir (Unicode U+11180..U+111DF)
  * Kashmiri Devanagari (with extended vowels ॳ, ॴ, ॶ, ॷ, ॅ, ॉ)
  * Kashmiri Perso-Arabic (Nastaliq with Kashmiri diacritics ٚ, ٛ, ۄ, ؠ)
  * Roman / Latin (Phonetic & IAST)
- Web & Mobile App Development (i18n UI strings, HTML/CSS font helpers, virtual keyboards)
- Date, Time & Calendar Localization (Traditional Saptrishi/Navreh & Gregorian calendars)
- Multi-Script Search Indexing & Diacritic-Insensitive Engine
- Linguistic Research & Fieldwork (Leipzig glossing, CoNLL-U, TEI-XML, lexical metrics)
- Phonology & IPA transcription (Kashmiri 16-vowel system, palatalization / matsaryar)
- Morphology & Grammar (4-class noun declension, split-ergative verbs, V2 word order)
- Rich Lexicon & Dictionary (Over 300 culturally authentic words with English & Hindi definitions)
- Traditional Kashmiri Proverbs & Idioms (Kahan & Masal)
- Kashmiri Number System (Numbers to Words & Words to Numbers)
- Jammu & Kashmir Historical Land Records & Revenue Register (Jamabandi, Khasra, Girdawari)
- Regional Dialect Studies (Kishtwari, Poguli, Siraji, Rambani)
"""

__version__ = "1.2.0"
__author__ = "Koshur Preservation Initiative"

# Re-export core functions for high-level convenience

from koshur.scripts.shikasta import (
    SHIKASTA_RULES,
    SHIKASTA_ABBREVIATIONS,
    explain_shikasta_rule,
    list_shikasta_rules,
    lookup_shikasta_abbreviation,
    list_shikasta_abbreviations,
    convert_traditional_weight,
    format_traditional_currency,
    calculate_fasli_year,
)

from koshur.scripts.transliterator import (
    transliterate,
    to_sharada,
    to_devanagari,
    to_persoarabic,
    to_latin,
    detect_script,
    latin_to_devanagari,
)
from koshur.phonology.ipa import to_ipa, describe_phonology
from koshur.nlp.tokenizer import tokenize, sent_tokenize
from koshur.nlp.normalizer import normalize
from koshur.lexicon.dictionary import (
    lookup,
    search_words,
    translate,
    get_lexicon_size,
    get_words_by_tag,
    get_all_tags,
)
from koshur.lexicon.proverbs import (
    get_proverb,
    get_all_proverbs,
    search_proverbs,
    random_proverb,
)
from koshur.lexicon.numbers import (
    number_to_koshur,
    koshur_to_number,
)
from koshur.revenue.land_records import (
    lookup_revenue_term,
    convert_land_area,
    explain_record_type,
    list_revenue_terms,
    get_terms_by_category,
    list_categories,
    search_revenue_terms,
)
from koshur.translator import (
    translate_record,
    translate_record_file,
    generate_html_certificate,
    extract_all_entities,
    extract_document_text,
    preprocess_image,
    get_sample_record,
    list_sample_records,
)
from koshur.grammar.v2_syntax import analyze_v2_syntax, analyze_v2_clause, check_v2_order
from koshur.grammar.noun import decline_noun, form_plural
from koshur.grammar.verb import conjugate_verb, get_imperative, get_converb
from koshur.dialects.comparator import compare_dialects, get_dialect_info

# Developer Web & Application Tools
from koshur.web.i18n import get_ui_string, get_all_ui_keys, export_i18n_json, UI_STRINGS
from koshur.web.html_helper import get_script_attributes, generate_webfont_css, wrap_html_text
from koshur.web.keyboard import get_keyboard_layout, transcribe_keystrokes

# Datetime & Localization
from koshur.datetime.calendar import (
    format_date,
    format_relative_time,
    get_weekday_name,
    get_month_name,
    get_time_of_day,
    KASHMIRI_WEEKDAYS,
    KASHMIRI_MONTHS,
    GREGORIAN_MONTHS_KASHMIRI,
)

# Search & Indexing
from koshur.search.indexer import strip_kashmiri_diacritics, KoshurSearchIndex

# Linguistic Research Tools
from koshur.research.glossing import generate_leipzig_gloss, get_gloss_tag_description, GLOSSING_TAGS
from koshur.research.corpus import export_conllu, export_tei_xml, export_jsonld
from koshur.research.metrics import count_syllables_kashmiri, compute_lexical_metrics, verify_v2_word_order
from koshur.research.sources import (
    HISTORICAL_SOURCES,
    get_research_sources,
    search_research_sources,
    get_library_catalog,
    get_library_stats,
    get_sources_by_category,
    get_sources_by_level,
    read_library_source,
    search_library_text,
)

# Folklore, Songs & Sacred Pantheon
from koshur.folklore import (
    FOLKLORE_GENRES,
    get_folklore_genre,
    get_all_folklore_genres,
    KASHMIRI_DEITIES,
    ASHTA_BHAIRAVAS,
    lookup_deity,
    get_all_deities,
    get_guardian_bhairavas,
    TRADITIONAL_SONGS,
    get_song,
    search_songs,
    get_all_songs,
)

__all__ = [
    # Scripts
    # Khat-i-Shikast & Palaeography
    "SHIKASTA_RULES",
    "SHIKASTA_ABBREVIATIONS",
    "explain_shikasta_rule",
    "list_shikasta_rules",
    "lookup_shikasta_abbreviation",
    "list_shikasta_abbreviations",
    "convert_traditional_weight",
    "format_traditional_currency",
    "calculate_fasli_year",
    "transliterate",
    "to_sharada",
    "to_devanagari",
    "to_persoarabic",
    "to_latin",
    "detect_script",
    "latin_to_devanagari",

    # Phonology
    "to_ipa",
    "describe_phonology",

    # NLP
    "tokenize",
    "sent_tokenize",
    "normalize",

    # Lexicon
    "lookup",
    "search_words",
    "translate",
    "get_lexicon_size",
    "get_words_by_tag",
    "get_all_tags",
    "get_proverb",
    "get_all_proverbs",
    "search_proverbs",
    "random_proverb",
    "number_to_koshur",
    "koshur_to_number",

    # Revenue
    "lookup_revenue_term",
    "convert_land_area",
    "explain_record_type",
    "list_revenue_terms",
    "get_terms_by_category",
    "list_categories",
    "search_revenue_terms",

    # Government Record Translator & Decipherment
    "translate_record",
    "translate_record_file",
    "generate_html_certificate",
    "extract_all_entities",
    "extract_document_text",
    "preprocess_image",
    "get_sample_record",
    "list_sample_records",

    # Grammar
    "analyze_v2_syntax",
    "analyze_v2_clause",
    "check_v2_order",
    "decline_noun",
    "form_plural",
    "conjugate_verb",
    "get_imperative",
    "get_converb",

    # Dialects
    "compare_dialects",
    "get_dialect_info",

    # Web & UI (For Developers)
    "get_ui_string",
    "get_all_ui_keys",
    "export_i18n_json",
    "UI_STRINGS",
    "get_script_attributes",
    "generate_webfont_css",
    "wrap_html_text",
    "get_keyboard_layout",
    "transcribe_keystrokes",

    # Datetime & Calendar
    "format_date",
    "format_relative_time",
    "get_weekday_name",
    "get_month_name",
    "get_time_of_day",
    "KASHMIRI_WEEKDAYS",
    "KASHMIRI_MONTHS",
    "GREGORIAN_MONTHS_KASHMIRI",

    # Search & Indexing
    "strip_kashmiri_diacritics",
    "KoshurSearchIndex",

    # Linguistic Research
    "generate_leipzig_gloss",
    "get_gloss_tag_description",
    "GLOSSING_TAGS",
    "export_conllu",
    "export_tei_xml",
    "export_jsonld",
    "count_syllables_kashmiri",
    "compute_lexical_metrics",
    "verify_v2_word_order",
    "HISTORICAL_SOURCES",
    "get_research_sources",
    "search_research_sources",
    "get_library_catalog",
    "get_library_stats",
    "get_sources_by_category",
    "get_sources_by_level",
    "read_library_source",
    "search_library_text",

    # Folklore, Songs & Sacred Pantheon
    "FOLKLORE_GENRES",
    "get_folklore_genre",
    "get_all_folklore_genres",
    "KASHMIRI_DEITIES",
    "ASHTA_BHAIRAVAS",
    "lookup_deity",
    "get_all_deities",
    "get_guardian_bhairavas",
    "TRADITIONAL_SONGS",
    "get_song",
    "search_songs",
    "get_all_songs",
]
