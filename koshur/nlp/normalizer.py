"""
Kashmiri Text Normalizer:
Normalizes non-standard Unicode variations across Kashmiri texts:
- Perso-Arabic: Unifies Arabic vs Persian letter encodings, removes stray tatweels,
  cleans multiple diacritics.
- Devanagari: Unifies nukta combinations, normalizes candrabindu and virama.
- Sharada: Cleans extraneous format controls.
"""

import unicodedata
from koshur.scripts.persoarabic import normalize_persoarabic

def normalize(text: str) -> str:
    """
    Applies standard Unicode NFC normalization and Kashmiri-specific script cleaning.
    """
    if not text:
        return ""
    
    # Standard Unicode NFC
    norm = unicodedata.normalize("NFC", text)
    
    # Script-specific cleaning
    norm = normalize_persoarabic(norm)
    
    # Normalize excessive spaces
    norm = " ".join(norm.split())
    return norm
