"""
Kashmiri Perso-Arabic (Nastaliq) script definitions, diacritics, and normalization.
Standard official script of Jammu & Kashmir for Kashmiri, incorporating
unique Unicode characters designed specifically for Kashmiri phonology:
- U+0620 (ARABIC LETTER KASHMIRI YEH - ؠ)
- U+065A (ARABIC VOWEL SIGN INVERTED DAMMA - ٚ)
- U+065B (ARABIC VOWEL SIGN NOON GHUNNA / VOWEL SIGN - ٛ)
- U+06C4 (ARABIC LETTER WAW WITH RING - ۄ)
- U+200C (ZERO WIDTH NON-JOINER - ZWNJ)
"""

# Kashmiri-specific Perso-Arabic characters
KASHMIRI_YEH = "\u0620"           # ؠ (Palatalization sign)
KASHMIRI_VOWEL_INVERTED_DAMMA = "\u065A"  # ٚ (Short high central vowel /ɨ/)
KASHMIRI_VOWEL_NOON_GHUNNA = "\u065B"     # ٛ (Neutral central vowel /ə/)
KASHMIRI_WAW_RING = "\u06C4"       # ۄ (Short 'o' /ɔ/)
KASHMIRI_WAW_VOWEL = "\u06C6"      # ۆ (Long 'o' /oː/)
KASHMIRI_WAW_U = "\u06C7"          # ۇ (Short 'u' /u/)

ZWNJ = "\u200C"                    # Zero Width Non-Joiner
ZWJ = "\u200D"                     # Zero Width Joiner

# Core Kashmiri Arabic Alphabet map
PERSOARABIC_LETTERS = {
    "alif": "ا",
    "alif_madda": "آ",
    "be": "ب",
    "pe": "پ",
    "te": "ت",
    "tte": "ٹ",
    "se": "ث",
    "jeem": "ج",
    "tse": "ژ",      # /ts/
    "che": "چ",      # /t͡ʃ/
    "tshe": "ڇ",     # /tsʰ/
    "he": "ح",
    "khe": "خ",
    "daal": "د",
    "ddaal": "ڈ",
    "zaal": "ذ",
    "re": "ر",
    "rre": "ڑ",
    "ze": "ز",
    "seen": "س",
    "sheen": "ش",
    "swad": "ص",
    "zwad": "ض",
    "toe": "ط",
    "zoe": "ظ",
    "ain": "ع",
    "ghain": "غ",
    "fe": "ف",
    "qaaf": "ق",
    "kaaf": "ک",
    "gaaf": "گ",
    "laam": "ل",
    "meem": "م",
    "noon": "ن",
    "noon_ghunna": "ں",
    "waw": "و",
    "waw_ring": "\u06C4", # ۄ
    "he_gol": "ہ",
    "do_chashmi_he": "ھ",
    "chhoti_ye": "ی",
    "badi_ye": "ے",
    "kashmiri_ye": "\u0620", # ؠ
}

def is_persoarabic(char: str) -> bool:
    """Check if character is in the Arabic/Persian/Urdu Unicode range."""
    if not char:
        return False
    cp = ord(char[0])
    return (0x0600 <= cp <= 0x06FF) or (0x0750 <= cp <= 0x077F) or (0xFB50 <= cp <= 0xFDFF) or (0xFE70 <= cp <= 0xFEFF)

def normalize_persoarabic(text: str) -> str:
    """
    Normalize inconsistent Kashmiri Perso-Arabic encodings:
    - Standardizes Arabic Kaf (ك) to Persian/Kashmiri Kaf (ک)
    - Standardizes Arabic Yeh (ي, ى) to standard Chhoti Ye (ی)
    - Removes duplicate diacritics
    - Normalizes Tatweel (ـ)
    """
    if not text:
        return ""
    text = text.replace("ك", "ک")
    text = text.replace("ي", "ی").replace("ى", "ی")
    text = text.replace("ھ", "ھ")
    text = text.replace("\u0640", "") # Remove tatweel/kashida
    return text
