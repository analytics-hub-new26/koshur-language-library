"""
Phonology subpackage for Koshur.
Includes 16-vowel inventory, palatalization (matsaryar) rules, and IPA transcription.
"""

from koshur.phonology.vowels import KASHMIRI_VOWEL_INVENTORY, get_vowel_info
from koshur.phonology.palatalization import (
    palatalize_consonant,
    apply_kashmiri_plural_mutation,
)
from koshur.phonology.ipa import to_ipa, describe_phonology

__all__ = [
    "KASHMIRI_VOWEL_INVENTORY",
    "get_vowel_info",
    "palatalize_consonant",
    "apply_kashmiri_plural_mutation",
    "to_ipa",
    "describe_phonology",
]
