"""
Kashmiri Dictionary & Lookup Engine:
Enables multilingual search, multi-stage fuzzy lookup, and cross-script translation
for Kashmiri words.
"""

from typing import List, Dict, Any, Optional
import difflib
from koshur.lexicon.words_data import WORDS_DATA

def _normalize_key(text: str) -> str:
    """
    Normalizes a romanized Kashmiri word by removing diacritics, macrons,
    spaces, and punctuation for flexible phonetic search.
    """
    if not text:
        return ""
    t = text.lower().strip()
    replacements = [
        ("ā", "a"), ("ē", "e"), ("ī", "i"), ("ō", "o"), ("ū", "u"),
        ("ə̄", "a"), ("ə", "a"), ("ɨ̄", "i"), ("ɨ", "i"),
        ("ṭ", "t"), ("ḍ", "d"), ("ṣ", "s"), ("ñ", "n"), ("ṅ", "n"),
        ("ç", "s"), ("é", "e"), ("è", "e"), ("á", "a"), ("í", "i"),
        ("ó", "o"), ("ú", "u"), ("ö", "o"), ("ü", "u")
    ]
    for src, dst in replacements:
        t = t.replace(src, dst)
    return "".join(c for c in t if c.isalnum())

def lookup(word: str) -> Optional[Dict[str, Any]]:
    """
    Intelligent multi-stage lookup for a Kashmiri word:
    1. Exact match across scripts (Roman, Devanagari, Perso-Arabic, Sharada).
    2. Exact match in registered search aliases.
    3. Normalized phonetic match (ignoring macrons and diacritics: e.g. 'pheran' matches 'Phēran').
    4. Fuzzy string match (difflib with threshold 0.75: e.g. 'phoran' matches 'Phēran').
    5. Semantic fallback (matching primary English or Hindi meaning).
    """
    if not word or not word.strip():
        return None

    raw = word.strip()
    w_lower = raw.lower()
    norm_w = _normalize_key(raw)

    # Stage 1: Exact match on native scripts or Roman lemma
    for entry in WORDS_DATA:
        if (
            entry["lemma"].lower() == w_lower
            or entry["roman"].lower() == w_lower
            or entry["devanagari"] == raw
            or entry["persoarabic"] == raw
            or entry["sharada"] == raw
        ):
            return entry

    # Stage 2: Check explicit aliases
    for entry in WORDS_DATA:
        aliases = entry.get("aliases", [])
        if any(a.lower() == w_lower for a in aliases):
            return entry

    # Stage 3: Normalized key match (handles accents, macrons: pheran -> Phēran)
    if norm_w:
        for entry in WORDS_DATA:
            if _normalize_key(entry["lemma"]) == norm_w or _normalize_key(entry["roman"]) == norm_w:
                return entry
            for a in entry.get("aliases", []):
                if _normalize_key(a) == norm_w:
                    return entry

    # Stage 4: Fuzzy matching with Levenshtein-like SequenceMatcher
    if norm_w and len(norm_w) >= 3:
        best_entry = None
        best_score = 0.0
        for entry in WORDS_DATA:
            candidates = [entry["lemma"], entry["roman"]] + entry.get("aliases", [])
            for cand in candidates:
                cand_norm = _normalize_key(cand)
                score = difflib.SequenceMatcher(None, norm_w, cand_norm).ratio()
                if score > best_score and score >= 0.72:
                    best_score = score
                    best_entry = entry
        if best_entry:
            return best_entry

    # Stage 5: Semantic keyword search in English / Hindi meanings
    for entry in WORDS_DATA:
        en_words = [tok.lower().strip("(),.;:") for tok in entry["meaning_en"].split()]
        hi_words = [tok.lower().strip("(),.;:") for tok in entry["meaning_hi"].split()]
        if w_lower in en_words or w_lower in hi_words:
            return entry

    return None

def search_words(query: str, tag: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Search lexicon entries matching query string anywhere in lemma,
    translations, etymology, or filtered by category tag.
    """
    if not query or not query.strip():
        if tag:
            return get_words_by_tag(tag)
        return []

    q = query.strip().lower()
    norm_q = _normalize_key(query)
    results = []

    for entry in WORDS_DATA:
        if tag and tag.lower() not in [t.lower() for t in entry.get("tags", [])]:
            continue

        aliases = [a.lower() for a in entry.get("aliases", [])]
        norm_aliases = [_normalize_key(a) for a in aliases]

        if (
            q in entry["lemma"].lower()
            or q in entry["roman"].lower()
            or q in entry["meaning_en"].lower()
            or q in entry["meaning_hi"].lower()
            or q in entry.get("etymology", "").lower()
            or query.strip() in entry["devanagari"]
            or query.strip() in entry["persoarabic"]
            or query.strip() in entry["sharada"]
            or any(q in a for a in aliases)
            or (norm_q and (norm_q in _normalize_key(entry["lemma"]) or any(norm_q in na for na in norm_aliases)))
        ):
            results.append(entry)

    return results

def get_words_by_tag(tag: str) -> List[Dict[str, Any]]:
    """Return all words classified under a specific semantic/cultural tag."""
    t = tag.lower().strip()
    return [e for e in WORDS_DATA if t in [tag_item.lower() for tag_item in e.get("tags", [])]]

def get_all_tags() -> List[str]:
    """Return a sorted list of all unique category tags in the dictionary."""
    tags = set()
    for e in WORDS_DATA:
        tags.update(e.get("tags", []))
    return sorted(tags)

def translate(word: str, target_lang: str = "en") -> str:
    """
    Convenience quick-translation for a Kashmiri word or concept.
    target_lang: 'en' (English) or 'hi' (Hindi).
    """
    match = lookup(word)
    if not match:
        matches = search_words(word)
        if matches:
            match = matches[0]

    if not match:
        return f"[Translation not found for '{word}']"

    if target_lang.lower().startswith("hi"):
        return match["meaning_hi"]
    return match["meaning_en"]

def get_lexicon_size() -> int:
    """Returns the total number of words in the curated lexicon."""
    return len(WORDS_DATA)
