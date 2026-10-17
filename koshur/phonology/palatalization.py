"""
Kashmiri Palatalization (Matsaryar / ماتسٔریار):
Palatalization is a defining morphophonemic process in Kashmiri grammar,
affecting noun pluralization, feminine derivation, and verb past tense inflection.
"""

from typing import Tuple

# Consonant palatalization shifts in Kashmiri
DENTAL_TO_AFFRICATE_SHIFTS = {
    "t": "ts",     # Dental voiceless stop -> Dental-alveolar affricate
    "th": "tsh",   # Dental aspirated stop -> Aspirated affricate
    "d": "j",      # Dental voiced stop -> Palatal affricate
    "dh": "jh",
}

# Vowel ablaut patterns triggered by palatalization / inflection
VOWEL_ABLAUT = {
    "oː": "əː",
    "ō": "ə̄",
    "uː": "ɨː",
    "ū": "ɨ̄",
    "aː": "ə̄",
    "ā": "ə̄",
    "o": "ə",
    "u": "ɨ",
}

def palatalize_consonant(consonant: str) -> str:
    """
    Applies regular Kashmiri palatalization to a final consonant.
    Dentals shift to affricates; other consonants acquire palatal glide [ʲ].
    """
    if consonant in DENTAL_TO_AFFRICATE_SHIFTS:
        return DENTAL_TO_AFFRICATE_SHIFTS[consonant]
    return f"{consonant}ʲ"

def apply_kashmiri_plural_mutation(singular_stem: str) -> str:
    """
    Simulates masculine plural formation by applying vowel umlaut & palatalization.
    Example: 'gōr' (milkman) -> 'gərʲ' (milkmans)
             'kōr' (girl/bracelet) -> 'kə̄rʲ'
    """
    stem = singular_stem
    for old_v, new_v in VOWEL_ABLAUT.items():
        if old_v in stem:
            stem = stem.replace(old_v, new_v)
            break
    if stem and not stem.endswith("ʲ"):
        stem = stem + "ʲ"
    return stem
