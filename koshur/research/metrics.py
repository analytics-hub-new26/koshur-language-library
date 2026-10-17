"""
Computational Linguistics & Typological Metrics Engine for Kashmiri.
Calculates:
1. Type-Token Ratio (TTR) & Root TTR (lexical richness).
2. Hapax Legomena count & ratio (words occurring exactly once).
3. Syllable counter adapted for Kashmiri central vowels.
4. Verb-Second (V2) Word Order syntactic compliance scoring.
5. Vowel-to-Consonant ratio and script distribution.
"""

from typing import Dict, Any, List
import re
from collections import Counter
import math

# Vowel regex patterns across scripts
_DEVA_VOWELS = set("अआइईउऊऋएऐओऔॳॴॶॷॅॉािीुूृेैोौँं")
_ARAB_VOWELS = set("اآوىوۄیؠًٌٍَُِّْٚٛ")
_ROMAN_VOWELS = set("aeiouāēīōūəɨáéíóúöü")

def count_syllables_kashmiri(word: str) -> int:
    """
    Heuristic syllable counter for Kashmiri words across scripts.
    Counts phonemic vowel nucleus peaks.
    """
    if not word or not word.strip():
        return 0

    w = word.strip().lower()

    # Romanized
    vowels = 0
    in_vowel = False
    for char in w:
        if char in _ROMAN_VOWELS:
            if not in_vowel:
                vowels += 1
                in_vowel = True
        else:
            in_vowel = False
    if vowels > 0:
        return max(1, vowels)

    # Devanagari
    deva_count = 0
    for char in w:
        if char in _DEVA_VOWELS:
            deva_count += 1
    if deva_count > 0:
        return deva_count

    # Perso-Arabic
    arab_count = 0
    for char in w:
        if char in _ARAB_VOWELS:
            arab_count += 1
    if arab_count > 0:
        return arab_count

    return max(1, len(w) // 3)

def compute_lexical_metrics(text: str) -> Dict[str, Any]:
    """
    Compute comprehensive quantitative linguistic metrics for a Kashmiri text/corpus:
    - Total Tokens (N)
    - Total Types (V)
    - Type-Token Ratio (TTR)
    - Root TTR (Guiraud's Index: V / sqrt(N))
    - Hapax Legomena (count and proportion)
    - Average Word Length
    - Syllables per word
    """
    if not text or not text.strip():
        return {
            "tokens": 0, "types": 0, "ttr": 0.0, "root_ttr": 0.0,
            "hapax_count": 0, "hapax_ratio": 0.0, "avg_word_length": 0.0,
            "avg_syllables_per_word": 0.0
        }

    raw_tokens = [tok.strip(".,;:?!-()\"'“”‘’—") for tok in text.split()]
    tokens = [t for t in raw_tokens if t]
    total_tokens = len(tokens)
    if total_tokens == 0:
        return {"tokens": 0, "types": 0, "ttr": 0.0}

    counts = Counter(tokens)
    total_types = len(counts)
    ttr = round(total_types / total_tokens, 4)
    root_ttr = round(total_types / math.sqrt(total_tokens), 4)

    hapax_legomena = sum(1 for w, c in counts.items() if c == 1)
    hapax_ratio = round(hapax_legomena / total_types, 4) if total_types > 0 else 0.0

    total_chars = sum(len(w) for w in tokens)
    avg_len = round(total_chars / total_tokens, 2)

    total_syllables = sum(count_syllables_kashmiri(w) for w in tokens)
    avg_syllables = round(total_syllables / total_tokens, 2)

    return {
        "tokens": total_tokens,
        "types": total_types,
        "ttr": ttr,
        "root_ttr": root_ttr,
        "hapax_count": hapax_legomena,
        "hapax_ratio": hapax_ratio,
        "avg_word_length": avg_len,
        "avg_syllables_per_word": avg_syllables,
    }

def verify_v2_word_order(sentence: str) -> Dict[str, Any]:
    """
    Linguistic analyzer assessing whether a Kashmiri clause complies with
    strict Verb-Second (V2) word order constraints.
    Checks if the finite auxiliary/verb appears in Position 2.
    """
    from koshur.grammar.v2_syntax import analyze_v2_clause

    res = analyze_v2_clause(sentence)
    compliance = res.get("is_v2_compliant", False)
    finite_pos = res.get("finite_verb_position", 0)

    feedback = (
        "Compliant with Kashmiri V2 syntax (finite verb in second structural position)."
        if compliance else
        f"Non-canonical word order (finite verb detected at position {finite_pos}, expected 2)."
    )

    return {
        "sentence": sentence,
        "is_v2_compliant": compliance,
        "finite_verb_position": finite_pos,
        "parsed_elements": res.get("elements", {}),
        "explanation": feedback
    }
