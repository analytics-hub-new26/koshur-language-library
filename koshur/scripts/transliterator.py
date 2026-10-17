"""
Universal Kashmiri Script Transliterator:
Provides bidirectional transliteration across all historical and contemporary scripts:
- Sharada (𑆯𑆳𑆫𑆢𑆳)
- Devanagari (कश्मीरी देवनागरी with ॳ, ॴ, ॶ, ॷ, ॅ, ॉ)
- Perso-Arabic (کٲشُر / نستعلیق with ٚ, ٛ, ۄ, ؠ)
- Roman / Latin (Phonetic / IAST)
"""

from typing import Optional
from koshur.scripts.sharada import (
    SHARADA_VOWELS, SHARADA_CONSONANTS, SHARADA_MATRAS,
    SHARADA_VIRAMA, SHARADA_CANDRABINDU, SHARADA_ANUSVARA,
    SHARADA_VISARGA, SHARADA_DANDA, SHARADA_DOUBLE_DANDA,
    SHARADA_DIGITS, is_sharada
)
from koshur.scripts.devanagari import (
    DEV_KASHMIRI_VOWELS, DEV_KASHMIRI_MATRAS,
    DEV_KASHMIRI_CONSONANTS, DEV_VIRAMA, DEV_ANUSVARA,
    DEV_CANDRABINDU, DEV_VISARGA, DEV_DANDA, DEV_DOUBLE_DANDA,
    is_devanagari
)
from koshur.scripts.persoarabic import (
    PERSOARABIC_LETTERS, KASHMIRI_YEH, KASHMIRI_VOWEL_INVERTED_DAMMA,
    KASHMIRI_VOWEL_NOON_GHUNNA, KASHMIRI_WAW_RING, is_persoarabic,
    normalize_persoarabic
)

# Bidirectional Dev <-> Sharada mapping
DEV_TO_SHARADA_VOWELS = {
    "अ": SHARADA_VOWELS["A"],
    "आ": SHARADA_VOWELS["AA"],
    "इ": SHARADA_VOWELS["I"],
    "ई": SHARADA_VOWELS["II"],
    "उ": SHARADA_VOWELS["U"],
    "ऊ": SHARADA_VOWELS["UU"],
    "ए": SHARADA_VOWELS["E"],
    "ऐ": SHARADA_VOWELS["AI"],
    "ओ": SHARADA_VOWELS["O"],
    "औ": SHARADA_VOWELS["AU"],
}

DEV_TO_SHARADA_MATRAS = {
    "ा": SHARADA_MATRAS["aa"],
    "ि": SHARADA_MATRAS["i"],
    "ी": SHARADA_MATRAS["ii"],
    "ु": SHARADA_MATRAS["u"],
    "ू": SHARADA_MATRAS["uu"],
    "े": SHARADA_MATRAS["e"],
    "ै": SHARADA_MATRAS["ai"],
    "ो": SHARADA_MATRAS["o"],
    "ौ": SHARADA_MATRAS["au"],
    # For Kashmiri specific central vowels, map cleanly to matra + virama / combiner
    "\u093a": SHARADA_MATRAS["e"],   # /ə/
    "\u093b": SHARADA_MATRAS["ai"],  # /əː/
    "\u0956": SHARADA_MATRAS["u"],   # /ɨ/
    "\u0957": SHARADA_MATRAS["uu"],  # /ɨː/
}

DEV_TO_SHARADA_CONSONANTS = {
    "क": SHARADA_CONSONANTS["k"],
    "ख": SHARADA_CONSONANTS["kh"],
    "ग": SHARADA_CONSONANTS["g"],
    "घ": SHARADA_CONSONANTS["gh"],
    "ङ": SHARADA_CONSONANTS["ng"],
    "च": SHARADA_CONSONANTS["c"],
    "छ": SHARADA_CONSONANTS["ch"],
    "ज": SHARADA_CONSONANTS["j"],
    "झ": SHARADA_CONSONANTS["jh"],
    "ञ": SHARADA_CONSONANTS["ny"],
    "ट": SHARADA_CONSONANTS["tt"],
    "ठ": SHARADA_CONSONANTS["tth"],
    "ड": SHARADA_CONSONANTS["dd"],
    "ढ": SHARADA_CONSONANTS["ddh"],
    "ण": SHARADA_CONSONANTS["nn"],
    "त": SHARADA_CONSONANTS["t"],
    "थ": SHARADA_CONSONANTS["th"],
    "द": SHARADA_CONSONANTS["d"],
    "ध": SHARADA_CONSONANTS["dh"],
    "न": SHARADA_CONSONANTS["n"],
    "प": SHARADA_CONSONANTS["p"],
    "फ": SHARADA_CONSONANTS["ph"],
    "ब": SHARADA_CONSONANTS["b"],
    "भ": SHARADA_CONSONANTS["bh"],
    "म": SHARADA_CONSONANTS["m"],
    "य": SHARADA_CONSONANTS["y"],
    "र": SHARADA_CONSONANTS["r"],
    "ल": SHARADA_CONSONANTS["l"],
    "व": SHARADA_CONSONANTS["v"],
    "श": SHARADA_CONSONANTS["sh"],
    "ष": SHARADA_CONSONANTS["ss"],
    "स": SHARADA_CONSONANTS["s"],
    "ह": SHARADA_CONSONANTS["h"],
    # Ligatures / Nukta forms
    "ज़": SHARADA_CONSONANTS["j"],
    "फ़": SHARADA_CONSONANTS["ph"],
    "ख़": SHARADA_CONSONANTS["kh"],
    "ग़": SHARADA_CONSONANTS["g"],
}

# Invert mappings for Sharada -> Dev
SHARADA_TO_DEV_VOWELS = {v: k for k, v in DEV_TO_SHARADA_VOWELS.items()}
SHARADA_TO_DEV_MATRAS = {v: k for k, v in DEV_TO_SHARADA_MATRAS.items()}
SHARADA_TO_DEV_CONSONANTS = {v: k for k, v in DEV_TO_SHARADA_CONSONANTS.items()}

# Devanagari to Roman Phonetic Mapping
DEV_TO_ROMAN = {
    "अ": "a", "आ": "ā", "इ": "i", "ई": "ī", "उ": "u", "ऊ": "ū",
    "ए": "ē", "ऐ": "ai", "ओ": "ō", "औ": "au", "ॅ": "e", "ॉ": "o",
    "\u0973": "ə", "\u0974": "ə̄", "\u0976": "ɨ", "\u0977": "ɨ̄",
    "ा": "ā", "ि": "i", "ी": "ī", "ु": "u", "ू": "ū",
    "े": "ē", "ै": "ai", "ो": "ō", "ौ": "au", "्": "",
    "\u093a": "ə", "\u093b": "ə̄", "\u0956": "ɨ", "\u0957": "ɨ̄",
    "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ṅ",
    "च": "ch", "छ": "chh", "ज": "j", "झ": "jh", "ञ": "ñ",
    "ट": "ṭ", "ठ": "ṭh", "ड": "ḍ", "ढ": "ḍh", "ण": "ṇ",
    "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
    "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
    "य": "y", "र": "r", "ल": "l", "व": "v", "श": "sh",
    "ष": "ṣ", "स": "s", "ह": "h", "ज़": "z", "च़": "ts",
    "छ़": "tsh", "फ़": "f", "ख़": "kh", "ग़": "gh",
    "ं": "n", "ँ": "̃", "ः": "h", "।": ".", "॥": ".."
}

# Devanagari to Perso-Arabic map
DEV_TO_ARABIC = {
    "अ": "ا", "आ": "آ", "इ": "اِ", "ई": "ای", "उ": "اُ", "ऊ": "او",
    "ए": "ای", "ऐ": "ای", "ओ": "او", "औ": "او",
    "\u0973": "ا" + KASHMIRI_VOWEL_NOON_GHUNNA, # ə
    "\u0976": "ا" + KASHMIRI_VOWEL_INVERTED_DAMMA, # ɨ
    "क": "ک", "ख": "کھ", "ग": "گ", "घ": "گھ",
    "च": "چ", "छ": "چھ", "ज": "ج", "झ": "جھ",
    "ट": "ٹ", "ठ": "ٹھ", "ड": "ڈ", "ढ": "ڈھ",
    "त": "ت", "थ": "تھ", "द": "د", "ध": "دھ", "न": "ن",
    "प": "پ", "फ": "پھ", "ब": "ب", "भ": "بھ", "म": "م",
    "य": "ی", "र": "ر", "ल": "ل", "व": "و",
    "श": "ش", "ष": "ش", "स": "س", "ह": "ہ",
    "ज़": "ز", "च़": "ژ", "छ़": "ڇ", "फ़": "ف",
    "ख़": "خ", "ग़": "غ",
    # Matras
    "ा": "ا", "ि": "", "ी": "ی", "ु": "", "ू": "و",
    "े": "ے", "ै": "ے", "ो": "و", "ौ": "و",
    "ॉ": KASHMIRI_WAW_RING,
    "\u093a": KASHMIRI_VOWEL_NOON_GHUNNA,
    "\u0956": KASHMIRI_VOWEL_INVERTED_DAMMA,
    "्": "", "ं": "ں", "ँ": "ں", "।": "۔", "॥": "۔"
}

# Perso-Arabic to Devanagari map
ARABIC_TO_DEV = {
    "ا": "अ", "آ": "आ", "ب": "ब", "پ": "प", "ت": "त", "ٹ": "ट",
    "ث": "स", "ج": "ज", "چ": "च", "ح": "ह", "خ": "ख़", "د": "द",
    "ڈ": "ड", "ذ": "ज़", "ر": "र", "ڑ": "ड़", "ز": "ज़", "ژ": "च़",
    "ڇ": "छ़", "س": "स", "ش": "श", "ص": "स", "ض": "ज़", "ط": "त",
    "ظ": "ज़", "ع": "अ", "غ": "ग़", "ف": "फ़", "ق": "क़", "ک": "क",
    "گ": "ग", "ل": "ल", "م": "म", "ن": "न", "ں": "ँ", "و": "व",
    "ہ": "ह", "ه": "ह", "ھ": "ह", "ی": "य", "ي": "य", "ے": "े", "ى": "या", "ة": "ह",
    "أ": "अ", "إ": "इ", "آ": "आ", "ك": "क",
    KASHMIRI_YEH: "्य",
    KASHMIRI_WAW_RING: "ॉ",
    KASHMIRI_VOWEL_NOON_GHUNNA: "\u093a",
    KASHMIRI_VOWEL_INVERTED_DAMMA: "\u0956",
    "ء": "", "ئ": "इ", "ؤ": "उ",
    "\u064e": "", "\u0650": "", "\u064f": "", "\u064b": "ं", "\u064c": "", "\u064d": "",
    "\u0651": "", "\u0652": "", "\u0670": "ा", "\u0671": "अ",
    "۔": "।"
}

def detect_script(text: str) -> str:
    """
    Detect the primary script of the input text:
    Returns one of: 'sharada', 'devanagari', 'persoarabic', 'latin', 'unknown'
    """
    if not text:
        return "unknown"
    
    counts = {"sharada": 0, "devanagari": 0, "persoarabic": 0, "latin": 0}
    for ch in text:
        if is_sharada(ch):
            counts["sharada"] += 1
        elif is_devanagari(ch):
            counts["devanagari"] += 1
        elif is_persoarabic(ch):
            counts["persoarabic"] += 1
        elif ("a" <= ch.lower() <= "z") or (ch in "āīūēōə̄ɨ̄ṭḍṇṣñṅ"):
            counts["latin"] += 1

    best = max(counts, key=counts.get)
    return best if counts[best] > 0 else "unknown"

def devanagari_to_sharada(text: str) -> str:
    """Transliterate Devanagari Kashmiri text to Sharada script."""
    result = []
    i = 0
    n = len(text)
    while i < n:
        # Check two-char combos first (like ज़, फ़, च़)
        if i + 1 < n and text[i:i+2] in DEV_TO_SHARADA_CONSONANTS:
            result.append(DEV_TO_SHARADA_CONSONANTS[text[i:i+2]])
            i += 2
            continue
        ch = text[i]
        if ch in DEV_TO_SHARADA_VOWELS:
            result.append(DEV_TO_SHARADA_VOWELS[ch])
        elif ch in DEV_TO_SHARADA_MATRAS:
            result.append(DEV_TO_SHARADA_MATRAS[ch])
        elif ch in DEV_TO_SHARADA_CONSONANTS:
            result.append(DEV_TO_SHARADA_CONSONANTS[ch])
        elif ch == DEV_VIRAMA:
            result.append(SHARADA_VIRAMA)
        elif ch == DEV_ANUSVARA:
            result.append(SHARADA_ANUSVARA)
        elif ch == DEV_CANDRABINDU:
            result.append(SHARADA_CANDRABINDU)
        elif ch == DEV_VISARGA:
            result.append(SHARADA_VISARGA)
        elif ch == DEV_DANDA:
            result.append(SHARADA_DANDA)
        elif ch == DEV_DOUBLE_DANDA:
            result.append(SHARADA_DOUBLE_DANDA)
        elif ch.isdigit() and int(ch) in SHARADA_DIGITS:
            result.append(SHARADA_DIGITS[int(ch)])
        else:
            result.append(ch)
        i += 1
    return "".join(result)

def sharada_to_devanagari(text: str) -> str:
    """Transliterate Sharada text to Devanagari script."""
    result = []
    for ch in text:
        if ch in SHARADA_TO_DEV_VOWELS:
            result.append(SHARADA_TO_DEV_VOWELS[ch])
        elif ch in SHARADA_TO_DEV_MATRAS:
            result.append(SHARADA_TO_DEV_MATRAS[ch])
        elif ch in SHARADA_TO_DEV_CONSONANTS:
            result.append(SHARADA_TO_DEV_CONSONANTS[ch])
        elif ch == SHARADA_VIRAMA:
            result.append(DEV_VIRAMA)
        elif ch == SHARADA_ANUSVARA:
            result.append(DEV_ANUSVARA)
        elif ch == SHARADA_CANDRABINDU:
            result.append(DEV_CANDRABINDU)
        elif ch == SHARADA_VISARGA:
            result.append(DEV_VISARGA)
        elif ch == SHARADA_DANDA:
            result.append(DEV_DANDA)
        elif ch == SHARADA_DOUBLE_DANDA:
            result.append(DEV_DOUBLE_DANDA)
        else:
            result.append(ch)
    return "".join(result)

def devanagari_to_persoarabic(text: str) -> str:
    """Transliterate Devanagari Kashmiri text to Kashmiri Perso-Arabic."""
    result = []
    i = 0
    n = len(text)
    while i < n:
        if i + 1 < n and text[i:i+2] in DEV_TO_ARABIC:
            result.append(DEV_TO_ARABIC[text[i:i+2]])
            i += 2
            continue
        ch = text[i]
        result.append(DEV_TO_ARABIC.get(ch, ch))
        i += 1
    return "".join(result)

def persoarabic_to_devanagari(text: str) -> str:
    """Transliterate Kashmiri Perso-Arabic text to Devanagari script."""
    text = normalize_persoarabic(text)
    result = []
    i = 0
    n = len(text)
    # Check aspirates like کھ, پھ, تھ, etc.
    aspirates = {
        "کھ": "ख", "گھ": "घ", "چھ": "छ", "جھ": "झ",
        "ٹھ": "ठ", "ڈھ": "ढ", "تھ": "थ", "دھ": "ध",
        "پھ": "फ", "بھ": "भ", "ژھ": "छ़"
    }
    while i < n:
        if i + 1 < n and text[i:i+2] in aspirates:
            result.append(aspirates[text[i:i+2]])
            i += 2
            continue
        ch = text[i]
        if ch in ARABIC_TO_DEV:
            result.append(ARABIC_TO_DEV[ch])
        elif '\u0600' <= ch <= '\u06FF':
            pass
        else:
            result.append(ch)
        i += 1
    return "".join(result)

def devanagari_to_latin(text: str) -> str:
    """Convert Devanagari Kashmiri text to Roman / Latin phonetic transliteration."""
    result = []
    i = 0
    n = len(text)
    while i < n:
        if i + 1 < n and text[i:i+2] in DEV_TO_ROMAN:
            result.append(DEV_TO_ROMAN[text[i:i+2]])
            i += 2
            continue
        ch = text[i]
        result.append(DEV_TO_ROMAN.get(ch, ch))
        i += 1
    return "".join(result)


ROMAN_CONSONANTS = [
    ('tsh', 'छ़'), ('chh', 'छ'), ('ts', 'च़'), ('ch', 'च'),
    ('kh', 'ख'), ('gh', 'घ'), ('ṭh', 'ठ'), ('th', 'थ'),
    ('ḍh', 'ढ'), ('dh', 'ध'), ('ph', 'फ'), ('bh', 'भ'),
    ('sh', 'श'), ('ṣ', 'ष'), ('zh', 'ज़'), ('ng', 'ङ्'), ('ny', 'ञ'),
    ('k', 'क'), ('g', 'ग'), ('j', 'ज'), ('ṭ', 'ट'),
    ('ḍ', 'ड'), ('ṇ', 'ण'), ('t', 'त'), ('d', 'द'),
    ('n', 'न'), ('p', 'प'), ('b', 'ब'), ('m', 'म'),
    ('y', 'य'), ('r', 'र'), ('l', 'ल'), ('v', 'व'),
    ('w', 'व'), ('s', 'स'), ('h', 'ह'), ('z', 'ज़'),
    ('f', 'फ़'), ('q', 'क़')
]

ROMAN_VOWELS = [
    ('ə̄', ('ॴ', 'ऻ')),
    ('ə', ('ॳ', 'ऺ')),
    ('ɨ̄', ('ॷ', 'ॗ')),
    ('ɨ', ('ॶ', 'ॖ')),
    ('aa', ('आ', 'ा')),
    ('ā', ('आ', 'ा')),
    ('ee', ('ई', 'ी')),
    ('ii', ('ई', 'ी')),
    ('ī', ('ई', 'ी')),
    ('oo', ('ऊ', 'ू')),
    ('uu', ('ऊ', 'ू')),
    ('ū', ('ऊ', 'ू')),
    ('ai', ('ऐ', 'ै')),
    ('au', ('औ', 'ौ')),
    ('ē', ('ए', 'े')),
    ('ō', ('ओ', 'ो')),
    ('e', ('ए', 'े')),
    ('o', ('ओ', 'ो')),
    ('i', ('इ', 'ि')),
    ('u', ('उ', 'ु')),
    ('a', ('अ', ''))
]

def latin_to_devanagari(text: str) -> str:
    """
    Convert Latin / Roman transliterated Kashmiri into Kashmiri Devanagari.
    Supports both phonetic typing and standard diacritic academic romanization.
    """
    res = []
    i = 0
    n = len(text)
    t_lower = text.lower()

    while i < n:
        if not text[i].isalnum() and text[i] not in 'āīūēōə̄ɨ̄ṭḍṇṣñṅəɨ':
            res.append(text[i])
            i += 1
            continue

        c_found = None
        c_dev = None
        for r_c, d_c in ROMAN_CONSONANTS:
            if t_lower.startswith(r_c, i):
                c_found = r_c
                c_dev = d_c
                break

        if c_found:
            i += len(c_found)
            v_found = None
            v_mat = None
            for r_v, (v_ind, v_m) in ROMAN_VOWELS:
                if t_lower.startswith(r_v, i):
                    v_found = r_v
                    v_mat = v_m
                    break
            if v_found:
                i += len(v_found)
                res.append(c_dev + v_mat)
            else:
                if i < n and (t_lower[i].isalpha() or t_lower[i] in 'āīūēōə̄ɨ̄ṭḍṇṣñṅəɨ'):
                    res.append(c_dev + '्')
                elif i >= n or text[i].isspace():
                    res.append(c_dev + '्')
                else:
                    res.append(c_dev)
            continue

        v_found = None
        v_ind = None
        for r_v, (v_i, v_m) in ROMAN_VOWELS:
            if t_lower.startswith(r_v, i):
                v_found = r_v
                v_ind = v_i
                break
        if v_found:
            i += len(v_found)
            res.append(v_ind)
            continue

        res.append(text[i])
        i += 1

    return ''.join(res)

def to_sharada(text: str) -> str:
    """Convert any supported script (Devanagari, Perso-Arabic, Latin, Sharada) to Sharada."""
    s = detect_script(text)
    if s == "sharada":
        return text
    if s == "latin":
        dev = latin_to_devanagari(text)
        return devanagari_to_sharada(dev)
    if s == "persoarabic":
        dev = persoarabic_to_devanagari(text)
        return devanagari_to_sharada(dev)
    return devanagari_to_sharada(text)

def to_devanagari(text: str) -> str:
    """Convert any supported script to Kashmiri Devanagari."""
    s = detect_script(text)
    if s == "devanagari":
        return text
    if s == "sharada":
        return sharada_to_devanagari(text)
    if s == "persoarabic":
        return persoarabic_to_devanagari(text)
    if s == "latin":
        return latin_to_devanagari(text)
    return text

def to_persoarabic(text: str) -> str:
    """Convert any supported script to Kashmiri Perso-Arabic."""
    s = detect_script(text)
    if s == "persoarabic":
        return normalize_persoarabic(text)
    if s == "sharada":
        dev = sharada_to_devanagari(text)
        return devanagari_to_persoarabic(dev)
    if s == "latin":
        dev = latin_to_devanagari(text)
        return devanagari_to_persoarabic(dev)
    return devanagari_to_persoarabic(text)

def to_latin(text: str) -> str:
    """Convert any Kashmiri text to Roman phonetic transliteration."""
    s = detect_script(text)
    if s == "latin":
        return text
    dev = to_devanagari(text)
    return devanagari_to_latin(dev)

def transliterate(text: str, target_script: str, source_script: Optional[str] = None) -> str:
    """
    Universal transliteration dispatcher.
    target_script: 'sharada', 'devanagari', 'persoarabic', 'latin'
    """
    target = target_script.lower()
    if target in ("sharada", "sharda"):
        return to_sharada(text)
    elif target in ("devanagari", "dev"):
        return to_devanagari(text)
    elif target in ("persoarabic", "arabic", "nastaliq", "urdu"):
        return to_persoarabic(text)
    elif target in ("latin", "roman", "english", "iast"):
        return to_latin(text)
    else:
        raise ValueError(f"Unsupported target script: {target_script}. Choose from 'sharada', 'devanagari', 'persoarabic', 'latin'.")
