"""
Kashmiri Morphological Stemmer:
Strips inflectional affixes, case markers, pronominal clitics, and participles.
"""

# Kashmiri common suffix patterns
KASHMIRI_SUFFIXES = [
    # Participles
    "ān", "aan", "वान", "وان", "ان", "vān",
    # Infinitive
    "un", "ुन", "ن",
    # Case & Plural suffixes
    "yav", "yev", "यव", "یو",
    "yan", "yen", "यन", "ین",
    "as", "स", "س",
    "an", "न", "ن",
    "av", "व", "و",
    # Pronominal clitics
    "um", "uth", "un", "uk", "okh", "ukh",
]

def stem_word(word: str) -> str:
    """Strips regular inflectional suffixes from a Kashmiri word to yield the stem."""
    w = word.strip()
    for sfx in sorted(KASHMIRI_SUFFIXES, key=len, reverse=True):
        if w.endswith(sfx) and len(w) > len(sfx) + 1:
            return w[:-len(sfx)]
    return w

stem_kashmiri_word = stem_word
