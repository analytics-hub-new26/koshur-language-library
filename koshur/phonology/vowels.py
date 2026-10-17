"""
Kashmiri Vowel System:
Kashmiri has a distinctive 16-vowel phonemic inventory featuring
four central unrounded vowels (/ɨ/, /ɨː/, /ə/, /əː/) that distinguish
it from almost all other modern Indo-Aryan languages.
"""

from typing import Dict, Any, List

KASHMIRI_VOWEL_INVENTORY: List[Dict[str, Any]] = [
    {
        "symbol": "a",
        "ipa": "/a/",
        "devanagari": "अ",
        "persoarabic": "اَ",
        "sharada": "𑆃",
        "height": "low",
        "backness": "central",
        "roundedness": "unrounded",
        "length": "short",
        "example": "akh (one)"
    },
    {
        "symbol": "ā",
        "ipa": "/aː/",
        "devanagari": "आ",
        "persoarabic": "آ",
        "sharada": "𑆄",
        "height": "low",
        "backness": "central",
        "roundedness": "unrounded",
        "length": "long",
        "example": "āb (water)"
    },
    {
        "symbol": "i",
        "ipa": "/i/",
        "devanagari": "इ",
        "persoarabic": "اِ",
        "sharada": "𑆅",
        "height": "high",
        "backness": "front",
        "roundedness": "unrounded",
        "length": "short",
        "example": "in’ (to bring)"
    },
    {
        "symbol": "ī",
        "ipa": "/iː/",
        "devanagari": "ई",
        "persoarabic": "ای",
        "sharada": "𑆆",
        "height": "high",
        "backness": "front",
        "roundedness": "unrounded",
        "length": "long",
        "example": "nīl (blue)"
    },
    {
        "symbol": "u",
        "ipa": "/u/",
        "devanagari": "उ",
        "persoarabic": "اُ",
        "sharada": "𑆇",
        "height": "high",
        "backness": "back",
        "roundedness": "rounded",
        "length": "short",
        "example": "yus (who)"
    },
    {
        "symbol": "ū",
        "ipa": "/uː/",
        "devanagari": "ऊ",
        "persoarabic": "او",
        "sharada": "𑆈",
        "height": "high",
        "backness": "back",
        "roundedness": "rounded",
        "length": "long",
        "example": "mūrath (statue)"
    },
    {
        "symbol": "e",
        "ipa": "/e/",
        "devanagari": "ऎ",
        "persoarabic": "اؠ",
        "sharada": "𑆍",
        "height": "mid",
        "backness": "front",
        "roundedness": "unrounded",
        "length": "short",
        "example": "yeti (here)"
    },
    {
        "symbol": "ē",
        "ipa": "/eː/",
        "devanagari": "ए",
        "persoarabic": "اے",
        "sharada": "𑆍",
        "height": "mid",
        "backness": "front",
        "roundedness": "unrounded",
        "length": "long",
        "example": "tēl (oil)"
    },
    {
        "symbol": "o",
        "ipa": "/o/",
        "devanagari": "ऒ",
        "persoarabic": "او",
        "sharada": "𑆏",
        "height": "mid",
        "backness": "back",
        "roundedness": "rounded",
        "length": "short",
        "example": "so (she)"
    },
    {
        "symbol": "ō",
        "ipa": "/oː/",
        "devanagari": "ओ",
        "persoarabic": "او",
        "sharada": "𑆏",
        "height": "mid",
        "backness": "back",
        "roundedness": "rounded",
        "length": "long",
        "example": "gōr (milkman)"
    },
    {
        "symbol": "ə",
        "ipa": "/ə/",
        "devanagari": "\u0973", # ॳ
        "persoarabic": "اٛ",
        "sharada": "𑆃𑇀",
        "height": "mid",
        "backness": "central",
        "roundedness": "unrounded",
        "length": "short",
        "example": "gəb (sheep)"
    },
    {
        "symbol": "ə̄",
        "ipa": "/əː/",
        "devanagari": "\u0974", # ॴ
        "persoarabic": "آٛ",
        "sharada": "𑆄𑇀",
        "height": "mid",
        "backness": "central",
        "roundedness": "unrounded",
        "length": "long",
        "example": "sə̄r (lake)"
    },
    {
        "symbol": "ɨ",
        "ipa": "/ɨ/",
        "devanagari": "\u0976", # ॶ
        "persoarabic": "اٚ",
        "sharada": "𑆇𑇀",
        "height": "high",
        "backness": "central",
        "roundedness": "unrounded",
        "length": "short",
        "example": "kɨth (pocket)"
    },
    {
        "symbol": "ɨ̄",
        "ipa": "/ɨː/",
        "devanagari": "\u0977", # ॷ
        "persoarabic": "اوٚ",
        "sharada": "𑆈𑇀",
        "height": "high",
        "backness": "central",
        "roundedness": "unrounded",
        "length": "long",
        "example": "mɨ̄ts (soil)"
    },
    {
        "symbol": "ɔ",
        "ipa": "/ɔ/",
        "devanagari": "ऑ",
        "persoarabic": "ۄ",
        "sharada": "𑆐",
        "height": "low-mid",
        "backness": "back",
        "roundedness": "rounded",
        "length": "short",
        "example": "kɔ̄l (stream)"
    },
    {
        "symbol": "ɛ",
        "ipa": "/ɛ/",
        "devanagari": "ऍ",
        "persoarabic": "اؠ",
        "sharada": "𑆍",
        "height": "low-mid",
        "backness": "front",
        "roundedness": "unrounded",
        "length": "short",
        "example": "bɛy (brother/friend)"
    }
]

def get_vowel_info(symbol: str) -> Dict[str, Any]:
    """Retrieve phonetic classification details for a Kashmiri vowel."""
    for v in KASHMIRI_VOWEL_INVENTORY:
        if v["symbol"] == symbol or v["devanagari"] == symbol or v["ipa"] == symbol:
            return v
    return {}
