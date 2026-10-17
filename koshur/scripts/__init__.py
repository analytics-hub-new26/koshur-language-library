"""
Scripts and Orthography subpackage for Koshur.
Supports Sharada, Devanagari, Perso-Arabic, and Roman scripts.
"""

from koshur.scripts.transliterator import (
    transliterate,
    to_sharada,
    to_devanagari,
    to_persoarabic,
    to_latin,
    detect_script,
    latin_to_devanagari,
)
from koshur.scripts.sharada import is_sharada
from koshur.scripts.devanagari import is_devanagari
from koshur.scripts.persoarabic import is_persoarabic, normalize_persoarabic
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

__all__ = [
    "transliterate",
    "to_sharada",
    "to_devanagari",
    "to_persoarabic",
    "to_latin",
    "detect_script",
    "latin_to_devanagari",
    "is_sharada",
    "is_devanagari",
    "is_persoarabic",
    "normalize_persoarabic",
    "SHIKASTA_RULES",
    "SHIKASTA_ABBREVIATIONS",
    "explain_shikasta_rule",
    "list_shikasta_rules",
    "lookup_shikasta_abbreviation",
    "list_shikasta_abbreviations",
    "convert_traditional_weight",
    "format_traditional_currency",
    "calculate_fasli_year",
]

