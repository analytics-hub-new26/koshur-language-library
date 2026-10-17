"""
Lexicon subpackage for Koshur.
Includes words data, dictionary lookup, proverbs, and number converters.
"""

from koshur.lexicon.dictionary import (
    lookup,
    search_words,
    translate,
    get_lexicon_size,
    get_words_by_tag,
    get_all_tags,
)
from koshur.lexicon.words_data import WORDS_DATA
from koshur.lexicon.proverbs import (
    get_proverb,
    get_all_proverbs,
    search_proverbs,
    random_proverb,
    PROVERBS_DATA,
)
from koshur.lexicon.numbers import (
    number_to_koshur,
    koshur_to_number,
    KASHMIRI_NUMBERS,
)

__all__ = [
    "lookup",
    "search_words",
    "translate",
    "get_lexicon_size",
    "get_words_by_tag",
    "get_all_tags",
    "WORDS_DATA",
    "get_proverb",
    "get_all_proverbs",
    "search_proverbs",
    "random_proverb",
    "PROVERBS_DATA",
    "number_to_koshur",
    "koshur_to_number",
    "KASHMIRI_NUMBERS",
]
