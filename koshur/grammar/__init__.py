"""
Kashmiri Morphosyntax & Grammar Engine.
"""

from koshur.grammar.v2_syntax import analyze_v2_clause, check_v2_order
from koshur.grammar.noun import decline_noun, form_plural, NOUN_PARADIGMS
from koshur.grammar.verb import conjugate_verb, get_imperative, get_converb, PRONOMINAL_CLITICS, VERB_LEXICON
from koshur.grammar.stemmer import stem_kashmiri_word

__all__ = [
    "analyze_v2_clause",
    "check_v2_order",
    "decline_noun",
    "form_plural",
    "NOUN_PARADIGMS",
    "conjugate_verb",
    "get_imperative",
    "get_converb",
    "PRONOMINAL_CLITICS",
    "VERB_LEXICON",
    "stem_kashmiri_word",
]
