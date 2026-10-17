"""
Sharada script (𑆯𑆳𑆫𑆢𑆳 𑆬𑆴𑆥𑆴) definitions and mappings.
Sharada is the historic Brahmic script indigenous to the Kashmir Valley,
used from the 8th century CE to write Sanskrit and Old Kashmiri manuscripts.
Unicode Block: U+11180 – U+111DF
"""

# Independent Vowels
SHARADA_VOWELS = {
    "A": "\U00011183",      # 𑆃
    "AA": "\U00011184",     # 𑆄
    "I": "\U00011185",      # 𑆅
    "II": "\U00011186",     # 𑆆
    "U": "\U00011187",      # 𑆇
    "UU": "\U00011188",     # 𑆈
    "VOC_R": "\U00011189",  # 𑆉
    "VOC_RR": "\U0001118A", # 𑆊
    "VOC_L": "\U0001118B",  # 𑆋
    "VOC_LL": "\U0001118C", # 𑆌
    "E": "\U0001118D",      # 𑆍
    "AI": "\U0001118E",     # 𑆎
    "O": "\U0001118F",      # 𑆏
    "AU": "\U00011190",     # 𑆐
}

# Consonants
SHARADA_CONSONANTS = {
    "k": "\U00011191",   # 𑆑
    "kh": "\U00011192",  # 𑆒
    "g": "\U00011193",   # 𑆓
    "gh": "\U00011194",  # 𑆔
    "ng": "\U00011195",  # 𑆕
    "c": "\U00011196",   # 𑆖 (ch)
    "ch": "\U00011197",  # 𑆗 (chh)
    "j": "\U00011198",   # 𑆘
    "jh": "\U00011199",  # 𑆙
    "ny": "\U0001119A",  # 𑆚
    "tt": "\U0001119B",  # 𑆛
    "tth": "\U0001119C", # 𑆜
    "dd": "\U0001119D",  # 𑆝
    "ddh": "\U0001119E", # 𑆞
    "nn": "\U0001119F",  # 𑆟
    "t": "\U000111A0",   # 𑆠
    "th": "\U000111A1",  # 𑆡
    "d": "\U000111A2",   # 𑆢
    "dh": "\U000111A3",  # 𑆣
    "n": "\U000111A4",   # 𑆤
    "p": "\U000111A5",   # 𑆥
    "ph": "\U000111A6",  # 𑆦
    "b": "\U000111A7",   # 𑆧
    "bh": "\U000111A8",  # 𑆨
    "m": "\U000111A9",   # 𑆩
    "y": "\U000111AA",   # 𑆪
    "r": "\U000111AB",   # 𑆫
    "l": "\U000111AC",   # 𑆬
    "ll": "\U000111AD",  # 𑆭
    "v": "\U000111AE",   # 𑆮
    "sh": "\U000111AF",  # 𑆯
    "ss": "\U000111B0",  # 𑆰
    "s": "\U000111B1",   # 𑆱
    "h": "\U000111B2",   # 𑆲
}

# Dependent Vowel Signs (Matras)
SHARADA_MATRAS = {
    "aa": "\U000111B3",  # 𑆳
    "i": "\U000111B4",   # 𑆴
    "ii": "\U000111B5",  # 𑆵
    "u": "\U000111B6",   # 𑆶
    "uu": "\U000111B7",  # 𑆷
    "voc_r": "\U000111B8",
    "voc_rr": "\U000111B9",
    "voc_l": "\U000111BA",
    "voc_ll": "\U000111BB",
    "e": "\U000111BC",   # 𑆼
    "ai": "\U000111BD",  # 𑆽
    "o": "\U000111BE",   # 𑆾
    "au": "\U000111BF",  # 𑆿
}

# Modifiers & Punctuations
SHARADA_VIRAMA = "\U000111C0"       # 𑇀 (Halant)
SHARADA_CANDRABINDU = "\U000111C1"  # 𑇁
SHARADA_ANUSVARA = "\U000111C2"     # 𑇂
SHARADA_VISARGA = "\U000111C3"      # 𑇃
SHARADA_AVAGRAHA = "\U000111C4"     # 𑇄
SHARADA_DANDA = "\U000111C5"        # 𑇅
SHARADA_DOUBLE_DANDA = "\U000111C6" # 𑇆
SHARADA_ABBREVIATION = "\U000111C7" # 𑇇
SHARADA_SEPARATOR = "\U000111C8"    # 𑇈

# Digits
SHARADA_DIGITS = {
    0: "\U000111D0",  # 𑇐
    1: "\U000111D1",  # 𑇑
    2: "\U000111D2",  # 𑇒
    3: "\U000111D3",  # 𑇓
    4: "\U000111D4",  # 𑇔
    5: "\U000111D5",  # 𑇕
    6: "\U000111D6",  # 𑇖
    7: "\U000111D7",  # 𑇗
    8: "\U000111D8",  # 𑇘
    9: "\U000111D9",  # 𑇙
}

def is_sharada(char: str) -> bool:
    """Check if character falls within the Unicode Sharada block."""
    if not char:
        return False
    cp = ord(char[0])
    return 0x11180 <= cp <= 0x111DF
