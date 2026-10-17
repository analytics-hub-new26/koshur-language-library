"""
Kashmiri Devanagari script definitions and standardizations.
Kashmiri has unique central vowels and phonemes that require extended
Devanagari characters standardized by the Central Hindi Directorate (CHD)
and encoded in the Unicode Standard (U+0973..U+0977, U+093A..U+093B, U+0956..U+0957).
"""

# Independent Vowels
DEV_KASHMIRI_VOWELS = {
    "a": "अ",
    "aa": "आ",
    "i": "इ",
    "ii": "ई",
    "u": "उ",
    "uu": "ऊ",
    "e_short": "ऎ",
    "e": "ए",
    "ai": "ऐ",
    "o_short": "ऒ",
    "o": "ओ",
    "au": "औ",
    "candra_e": "ऍ",     # /ɛ/
    "candra_o": "ऑ",     # /ɔ/
    "oe": "\u0973",      # ॳ - Short neutral central vowel /ə/
    "ooe": "\u0974",     # ॴ - Long neutral central vowel /əː/
    "ue": "\u0976",      # ॶ - Short high central vowel /ɨ/
    "uue": "\u0977",     # ॷ - Long high central vowel /ɨː/
}

# Dependent Vowel Signs (Matras)
DEV_KASHMIRI_MATRAS = {
    "aa": "ा",
    "i": "ि",
    "ii": "ी",
    "u": "ु",
    "uu": "ू",
    "e_short": "ॆ",
    "e": "े",
    "ai": "ै",
    "o_short": "ॊ",
    "o": "ो",
    "au": "ौ",
    "candra_e": "ॅ",     # /ɛ/
    "candra_o": "ॉ",     # /ɔ/
    "oe": "\u093a",      # ऺ - Matra for /ə/
    "ooe": "\u093b",     # ऻ - Matra for /əː/
    "ue": "\u0956",      # ॖ - Matra for /ɨ/
    "uue": "\u0957",     # ॗ - Matra for /ɨː/
}

# Kashmiri Consonants in Devanagari
DEV_KASHMIRI_CONSONANTS = {
    "k": "क",
    "kh": "ख",
    "g": "ग",
    "gh": "घ",
    "ng": "ङ",
    "c": "च",
    "ch": "छ",
    "j": "ज",
    "jh": "झ",
    "ny": "ञ",
    "tt": "ट",
    "tth": "ठ",
    "dd": "ड",
    "ddh": "ढ",
    "nn": "ण",
    "t": "त",
    "th": "थ",
    "d": "द",
    "dh": "ध",
    "n": "न",
    "p": "प",
    "ph": "फ",
    "b": "ब",
    "bh": "भ",
    "m": "म",
    "y": "य",
    "r": "र",
    "l": "ल",
    "v": "व",
    "w": "व",
    "sh": "श",
    "ss": "ष",
    "s": "स",
    "h": "ह",
    # Kashmiri-specific affricates and loans with nukta
    "ts": "च़",        # Kashmiri Tse /ʦ/
    "tsh": "छ़",       # Kashmiri Tshe /ʦʰ/
    "z": "ज़",         # Kashmiri Ze /z/
    "f": "फ़",
    "kh_fric": "ख़",   # /x/
    "g_fric": "ग़",    # /ɣ/
}

DEV_VIRAMA = "्"
DEV_ANUSVARA = "ं"
DEV_CANDRABINDU = "ँ"
DEV_VISARGA = "ः"
DEV_NUKTA = "़"
DEV_DANDA = "।"
DEV_DOUBLE_DANDA = "॥"

def is_devanagari(char: str) -> bool:
    """Check if character is in the Devanagari Unicode range."""
    if not char:
        return False
    cp = ord(char[0])
    return 0x0900 <= cp <= 0x097F
