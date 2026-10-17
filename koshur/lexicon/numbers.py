"""
Kashmiri Numeral System (Cardinal & Ordinal):
Converts numbers to Kashmiri words across Devanagari, Perso-Arabic, Roman scripts,
and parses Kashmiri numerals into integers.
"""

from typing import Dict, Any

KASHMIRI_NUMBERS: Dict[int, Dict[str, str]] = {
    0: {"roman": "sifar", "dev": "सिफ़र", "arabic": "صِفر"},
    1: {"roman": "akh", "dev": "अख", "arabic": "اَکھ"},
    2: {"roman": "zə", "dev": "ज़ॳ", "arabic": "زٕ"},
    3: {"roman": "trē", "dev": "त्रे", "arabic": "ترے"},
    4: {"roman": "tsōr", "dev": "च़ोर", "arabic": "ژور"},
    5: {"roman": "pānts", "dev": "पाँच़", "arabic": "پانژ"},
    6: {"roman": "shē", "dev": "शे", "arabic": "شے"},
    7: {"roman": "sath", "dev": "सथ", "arabic": "سَتھ"},
    8: {"roman": "ə̄ṭh", "dev": "ऑठ", "arabic": "اٲٹھ"},
    9: {"roman": "nav", "dev": "नव", "arabic": "نَو"},
    10: {"roman": "dəh", "dev": "दॳह", "arabic": "دَہ"},
    11: {"roman": "kāh", "dev": "काह", "arabic": "کاہ"},
    12: {"roman": "bāh", "dev": "बाह", "arabic": "باہ"},
    13: {"roman": "truwah", "dev": "त्रुवाह", "arabic": "تُرواہ"},
    14: {"roman": "tsuwah", "dev": "च़ुवाह", "arabic": "ژُواہ"},
    15: {"roman": "pandāh", "dev": "पंदाह", "arabic": "پَنداہ"},
    16: {"roman": "shurah", "dev": "शुरह", "arabic": "شُرَہ"},
    17: {"roman": "sadah", "dev": "सदह", "arabic": "سَدَہ"},
    18: {"roman": "ardah", "dev": "अर्दह", "arabic": "اَردَہ"},
    19: {"roman": "kunwuh", "dev": "कुनवुह", "arabic": "کُنوُہ"},
    20: {"roman": "wuh", "dev": "वुह", "arabic": "وُہ"},
    30: {"roman": "trɨh", "dev": "त्रिह", "arabic": "ترِہ"},
    40: {"roman": "tsatji", "dev": "च़तजि", "arabic": "ژَتَجِ"},
    50: {"roman": "pantsāh", "dev": "पंचास", "arabic": "پَنژاہ"},
    60: {"roman": "hə̄th", "dev": "हॴठ", "arabic": "ہٲٹھ"},
    70: {"roman": "sattar", "dev": "सत्तर", "arabic": "سَتَر"},
    80: {"roman": "shīt", "dev": "शीत", "arabic": "شِیت"},
    90: {"roman": "namath", "dev": "नमथ", "arabic": "نَمَتھ"},
    100: {"roman": "hath", "dev": "हथ", "arabic": "ہَتھ"},
    1000: {"roman": "sās", "dev": "सास", "arabic": "ساس"},
    100000: {"roman": "lachh", "dev": "लच्छ", "arabic": "لَچھ"},
    10000000: {"roman": "krōr", "dev": "क्रोर", "arabic": "کرور"},
}

def number_to_koshur(n: int, script: str = "roman") -> str:
    """
    Converts integer to Kashmiri number word.
    script: 'roman', 'dev', 'arabic'
    """
    s = script.lower()
    if s in ("devanagari", "dev"):
        key = "dev"
    elif s in ("persoarabic", "arabic", "urdu"):
        key = "arabic"
    else:
        key = "roman"

    if n in KASHMIRI_NUMBERS:
        return KASHMIRI_NUMBERS[n][key]

    if n < 100:
        tens = (n // 10) * 10
        rem = n % 10
        if rem == 0:
            return KASHMIRI_NUMBERS.get(tens, {}).get(key, str(n))
        t_w = KASHMIRI_NUMBERS.get(tens, {}).get(key, "")
        r_w = KASHMIRI_NUMBERS.get(rem, {}).get(key, "")
        return f"{t_w} tɨ {r_w}" if key == "roman" else f"{t_w} तॳ {r_w}"

    if n < 1000:
        h = n // 100
        rem = n % 100
        h_str = f"{number_to_koshur(h, script)} {KASHMIRI_NUMBERS[100][key]}"
        return f"{h_str} {number_to_koshur(rem, script)}" if rem else h_str

    if n < 100000:
        th = n // 1000
        rem = n % 1000
        th_str = f"{number_to_koshur(th, script)} {KASHMIRI_NUMBERS[1000][key]}"
        return f"{th_str} {number_to_koshur(rem, script)}" if rem else th_str

    if n < 10000000:
        l = n // 100000
        rem = n % 100000
        l_str = f"{number_to_koshur(l, script)} {KASHMIRI_NUMBERS[100000][key]}"
        return f"{l_str} {number_to_koshur(rem, script)}" if rem else l_str

    c = n // 10000000
    rem = n % 10000000
    c_str = f"{number_to_koshur(c, script)} {KASHMIRI_NUMBERS[10000000][key]}"
    return f"{c_str} {number_to_koshur(rem, script)}" if rem else c_str

def koshur_to_number(word: str) -> int:
    """Parses a Kashmiri number word back into an integer."""
    w = word.strip().lower()
    for num, data in KASHMIRI_NUMBERS.items():
        if (
            w == data["roman"].lower()
            or word.strip() == data["dev"]
            or word.strip() == data["arabic"]
        ):
            return num
    return -1
