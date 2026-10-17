"""
Kashmiri NLP Tokenizer:
Word and sentence tokenizers customized for Kashmiri orthography, handling
Perso-Arabic punctuation (؟،؛۔), Devanagari dandas (। ॥), Sharada separators (𑇅 𑇆),
and Zero-Width Non-Joiners (ZWNJ).
"""

import re
from typing import List

# Sentence break regex across Kashmiri scripts
SENTENCE_SPLIT_REGEX = re.compile(r'([.?!।॥۔𑇅𑇆\n]+)')

# Explicit word characters excluding punctuation
WORD_CHARS = (
    r'\u0901-\u0963\u0966-\u096F\u0971-\u097F' # Devanagari excluding danda (0964, 0965)
    r'\u0620-\u064A\u065A-\u065B\u066E-\u06D3\u0750-\u077F' # Perso-Arabic excluding punctuation
    r'\U00011180-\U000111C4\U000111CE-\U000111DF' # Sharada excluding dandas
    r'a-zA-Z0-9'
    r'āīūēōə̄ɨ̄ṭḍṇṣñṅ'
    r'\u200C\u200D'
    r'\'-'
)

WORD_TOKEN_REGEX = re.compile(rf'[{WORD_CHARS}]+|[।॥۔𑇅𑇆.,!?;:؟،؛\(\)\[\]"\'«»]')

def tokenize(text: str) -> List[str]:
    """
    Tokenizes Kashmiri text into words and punctuation tokens,
    preserving Kashmiri diacritics, ZWNJ bonds, and Sharada glyphs.
    """
    if not text:
        return []
    tokens = WORD_TOKEN_REGEX.findall(text)
    return [t for t in tokens if t.strip()]

def sent_tokenize(text: str) -> List[str]:
    """
    Splits Kashmiri text into constituent sentences based on
    Urdu/Arabic full stop (۔), Devanagari Danda (।), Sharada danda (𑇅), or Latin period (.).
    """
    if not text:
        return []
    parts = SENTENCE_SPLIT_REGEX.split(text)
    sentences = []
    current = ""
    for p in parts:
        if not p:
            continue
        if SENTENCE_SPLIT_REGEX.match(p):
            current += p
            if current.strip():
                sentences.append(current.strip())
            current = ""
        else:
            current += p
    if current.strip():
        sentences.append(current.strip())
    return sentences
