"""
Kashmiri IPA (International Phonetic Alphabet) transcription engine.
Generates phonemic and phonetic representations for Kashmiri words and sentences.
"""

from typing import Dict
from koshur.scripts.transliterator import to_devanagari, detect_script
from koshur.phonology.vowels import KASHMIRI_VOWEL_INVENTORY

DEV_TO_IPA_MAP: Dict[str, str] = {
    # Vowels
    "अ": "a", "आ": "aː", "इ": "i", "ई": "iː", "उ": "u", "ऊ": "uː",
    "ए": "eː", "ऐ": "əi", "ओ": "oː", "औ": "əu", "ऍ": "ɛ", "ऑ": "ɔ",
    "ॳ": "ə", "ॴ": "əː", "ॶ": "ɨ", "ॷ": "ɨː",
    # Matras
    "ा": "aː", "ि": "i", "ी": "iː", "ु": "u", "ू": "uː",
    "े": "eː", "ै": "əi", "ो": "oː", "ौ": "əu", "ॅ": "ɛ", "ॉ": "ɔ",
    "\u093a": "ə", "\u093b": "əː", "\u0956": "ɨ", "\u0957": "ɨː",
    # Consonants
    "क": "k", "ख": "kʰ", "ग": "ɡ", "घ": "ɡʱ", "ङ": "ŋ",
    "च": "t͡ʃ", "छ": "t͡ʃʰ", "ज": "d͡ʒ", "झ": "d͡ʒʱ", "ञ": "ɲ",
    "ट": "ʈ", "ठ": "ʈʰ", "ड": "ɖ", "ढ": "ɖʱ", "ण": "ɳ",
    "त": "t", "थ": "tʰ", "द": "d", "ध": "dʱ", "न": "n",
    "प": "p", "फ": "pʰ", "ब": "b", "भ": "bʱ", "म": "m",
    "य": "j", "र": "r", "ल": "l", "व": "w", "श": "ʃ", "ष": "ʂ",
    "स": "s", "ह": "h", "ज़": "z", "च़": "t͡s", "छ़": "t͡sʰ",
    "फ़": "f", "ख़": "x", "ग़": "ɣ",
    "ं": "̃", "ँ": "̃", "ः": "h", "्": "",
    "।": " | ", "॥": " || "
}

def to_ipa(text: str) -> str:
    """
    Generate IPA transcription for Kashmiri text.
    Handles input in Devanagari, Perso-Arabic, Sharada, or Roman scripts.
    """
    dev = to_devanagari(text)
    ipa_tokens = []
    i = 0
    n = len(dev)
    
    while i < n:
        # Check two-character combinations first (nukta combinations)
        if i + 1 < n and dev[i:i+2] in DEV_TO_IPA_MAP:
            ipa_tokens.append(DEV_TO_IPA_MAP[dev[i:i+2]])
            i += 2
            continue
        ch = dev[i]
        if ch in DEV_TO_IPA_MAP:
            ipa_tokens.append(DEV_TO_IPA_MAP[ch])
        else:
            ipa_tokens.append(ch)
        i += 1
        
    return "".join(ipa_tokens)

def describe_phonology() -> str:
    """Returns a comprehensive linguistic summary of Kashmiri phonology."""
    return (
        "=== Kashmiri (Koshur) Phonological Overview ===\n"
        "1. Vowels: 16 contrastive monophthongs (front, central, back across short & long durations).\n"
        "   - Hallmark Central Vowels: /ə/ (short mid central), /əː/ (long mid central), "
        "/ɨ/ (short high central), /ɨː/ (long high central).\n"
        "2. Consonants: Rich inventory of dental-alveolar affricates (/t͡s/, /t͡sʰ/) distinct from palato-alveolars.\n"
        "3. Matsaryar (Palatalization): Extensive morphophonemic palatalization affecting almost all consonants.\n"
        "4. Syntax: Strict Verb-Second (V2) order in main clauses, unique among modern South Asian Indo-Aryan languages.\n"
    )
