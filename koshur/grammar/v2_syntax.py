"""
Kashmiri V2 (Verb-Second) Syntax Analyzer:
Kashmiri is the only major modern Indo-Aryan language with strict Verb-Second (V2)
word order in root clauses (typologically identical to Germanic languages like German,
Dutch, and Icelandic), contrasting with the Verb-Final (SOV) order of other Indo-Aryan tongues.
"""

from typing import List, Dict, Any, Union

# Common Kashmiri auxiliary/copular finite verbs
FINITE_VERB_AUXILIARIES = {
    # Present auxiliaries (छु, छ़े, छि, छ्य, etc.)
    "chhu", "chhi", "chhe", "chha", "chhus", "chhukh", "chhum",
    "छु", "छि", "छ़े", "छ़ा", "छ़ुस", "छ़ुख", "छ़ुम",
    "چھُ", "چھِ", "چھئے", "چھُس", "چھُکھ", "چھُم",
    # Past auxiliaries / finite copulas (ओस, ऑस, ऎस, आदि)
    "ōs", "ə̄s", "ə̄y", "ə̄sʲ", "ōsukh", "ōsum",
    "ओस", "ऑस", "ऐस", "ओसुम", "ओसुख",
    "اوس", "ٲس", "ٲسی", "اوسُم", "اوسُکھ",
    # Future auxiliaries
    "āsi", "āsan", "āsē", "आसि", "आसन", "आसे", "آسِ", "آسَن",
}

def analyze_v2_syntax(clause_tokens: Union[str, List[str]]) -> Dict[str, Any]:
    """
    Analyzes a Kashmiri sentence or clause to detect and evaluate its V2 structure.
    Returns:
      - is_v2: bool indicating whether the finite verb is in position 2.
      - first_constituent: token or phrase in position 1 (Topic/Subject/Adverbial).
      - finite_verb: verb token in position 2.
      - remainder: tokens following position 2.
      - explanation: linguistic analysis.
    """
    if isinstance(clause_tokens, str):
        tokens = clause_tokens.split()
    else:
        tokens = clause_tokens

    if not tokens:
        return {"error": "Empty clause", "is_v2": False}

    # Clean punctuation
    cleaned = [t.strip(".,!?|॥۔") for t in tokens if t.strip(".,!?|॥۔")]
    if len(cleaned) < 2:
        return {
            "is_v2": False,
            "tokens": cleaned,
            "explanation": "Clause too short to evaluate V2 constituent structure."
        }

    # Locate finite verb
    v_pos = -1
    for idx, tok in enumerate(cleaned):
        if tok.lower() in FINITE_VERB_AUXILIARIES:
            v_pos = idx
            break

    if v_pos == 1:
        return {
            "is_v2": True,
            "is_v2_compliant": True,
            "position": 2, # 1-indexed
            "finite_verb_position": 2,
            "first_constituent": cleaned[0],
            "finite_verb": cleaned[1],
            "remainder": cleaned[2:],
            "elements": {
                "position_1": cleaned[0],
                "position_2_verb": cleaned[1],
                "remainder": cleaned[2:]
            },
            "explanation": (
                f"Valid Kashmiri V2 structure! The finite verb '{cleaned[1]}' strictly "
                f"occupies position 2 following initial constituent '{cleaned[0]}'."
            )
        }
    elif v_pos > 1:
        return {
            "is_v2": False,
            "is_v2_compliant": False,
            "position": v_pos + 1,
            "finite_verb_position": v_pos + 1,
            "finite_verb": cleaned[v_pos],
            "elements": {
                "position_1": cleaned[0],
                "finite_verb": cleaned[v_pos]
            },
            "explanation": (
                f"Non-standard or subordinate clause order: Finite verb '{cleaned[v_pos]}' "
                f"is at position {v_pos + 1} rather than root V2 position."
            )
        }
    else:
        return {
            "is_v2": False,
            "is_v2_compliant": False,
            "finite_verb_position": 0,
            "explanation": "No standard finite auxiliary identified; lexical main verb might be inflected directly."
        }

def analyze_v2_clause(sentence: Union[str, List[str]]) -> Dict[str, Any]:
    """Convenience alias for analyze_v2_syntax."""
    return analyze_v2_syntax(sentence)

def check_v2_order(sentence: Union[str, List[str]]) -> bool:
    """Returns True if the sentence satisfies canonical Kashmiri V2 word order."""
    res = analyze_v2_syntax(sentence)
    return bool(res.get("is_v2", False))
