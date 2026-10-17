"""
Multi-Script Search Indexer & Diacritic-Insensitive Engine for Kashmiri.
Enables web search bars and app queries to find Kashmiri words regardless of:
- Diacritics (Persian harakat, Devanagari matras, Roman macrons)
- Script used (searches simultaneously across English, Devanagari, Perso-Arabic, Sharada)
- Typographical variations and partial prefix matches.
"""

from typing import List, Dict, Any, Optional
import re
import difflib

# Regex patterns for stripping diacritical marks
_ARABIC_DIACRITICS = re.compile(r"[\u064B-\u065F\u0670\u06D6-\u06DC\u06DF-\u06E4\u06E7\u06E8\u06EA-\u06ED\u0656\u0657\u065A\u065B]")
_DEVANAGARI_SIGNS = re.compile(r"[\u0901\u0902\u0903\u093C\u093E-\u094F\u0951-\u0957\u0962\u0963\u0953\u0954]")
_SHARADA_SIGNS = re.compile(r"[\U00011180-\U00011182\U000111B3-\U000111C4\U000111C9-\U000111CC]")

def strip_kashmiri_diacritics(text: str) -> str:
    """
    Strips all diacritical marks across Perso-Arabic, Devanagari, Sharada,
    and Romanized Kashmiri to produce a normalized search key.
    """
    if not text:
        return ""

    t = text.strip()
    # Strip Arabic harakat & diacritics
    t = _ARABIC_DIACRITICS.sub("", t)
    # Normalize Arabic alef variants
    t = re.sub(r"[آإأٱ]", "ا", t)
    # Strip Devanagari nuktas, matras, anusvara, candrabindu
    t = _DEVANAGARI_SIGNS.sub("", t)
    # Strip Sharada vowel signs and viramas
    t = _SHARADA_SIGNS.sub("", t)

    # Roman diacritic folding
    replacements = [
        ("ā", "a"), ("ē", "e"), ("ī", "i"), ("ō", "o"), ("ū", "u"),
        ("ə̄", "a"), ("ə", "a"), ("ɨ̄", "i"), ("ɨ", "i"),
        ("ṭ", "t"), ("ḍ", "d"), ("ṣ", "s"), ("ñ", "n"), ("ṅ", "n"),
        ("ç", "s"), ("é", "e"), ("è", "e"), ("á", "a"), ("í", "i"),
        ("ó", "o"), ("ú", "u"), ("ö", "o"), ("ü", "u")
    ]
    t_lower = t.lower()
    for src, dst in replacements:
        t_lower = t_lower.replace(src, dst)

    # Clean whitespace and punctuation
    return "".join(c for c in t_lower if c.isalnum() or c.isspace()).strip()

class KoshurSearchIndex:
    """
    Fast in-memory multi-script inverted search index for web apps,
    providing prefix autocomplete and ranked multi-script fuzzy search.
    """

    def __init__(self):
        self.documents: Dict[str, Dict[str, Any]] = {}
        self.normalized_keys: Dict[str, List[str]] = {} # doc_id -> list of normalized terms

    def add_document(self, doc_id: str, title: str, text: str, metadata: Optional[Dict[str, Any]] = None):
        """Add a document/entry to the search index."""
        meta = metadata or {}
        self.documents[doc_id] = {
            "id": doc_id,
            "title": title,
            "text": text,
            "metadata": meta,
        }

        # Build search tokens
        search_blob = f"{title} {text} {meta.get('lemma', '')} {meta.get('devanagari', '')} {meta.get('persoarabic', '')} {meta.get('sharada', '')} {' '.join(meta.get('aliases', []))}"
        raw_words = search_blob.split()
        norm_tokens = set()
        for w in raw_words:
            k = strip_kashmiri_diacritics(w)
            if k:
                norm_tokens.add(k)
        self.normalized_keys[doc_id] = list(norm_tokens)

    def search(self, query: str, limit: int = 10, fuzzy: bool = True) -> List[Dict[str, Any]]:
        """
        Search documents matching query with relevance scoring.
        Matches across all scripts and normalized forms.
        """
        if not query or not query.strip():
            return []

        q_norm = strip_kashmiri_diacritics(query)
        q_raw = query.strip().lower()
        scored_results = []

        for doc_id, doc in self.documents.items():
            score = 0.0
            title_lower = doc["title"].lower()
            text_lower = doc["text"].lower()

            # Exact raw substring in title or text
            if q_raw in title_lower:
                score += 5.0
            if q_raw in text_lower:
                score += 2.0

            # Normalized token match
            tokens = self.normalized_keys.get(doc_id, [])
            for tok in tokens:
                if tok == q_norm:
                    score += 4.0
                elif tok.startswith(q_norm) or q_norm.startswith(tok):
                    score += 2.5
                elif q_norm in tok:
                    score += 1.5
                elif fuzzy and len(q_norm) >= 3:
                    ratio = difflib.SequenceMatcher(None, q_norm, tok).ratio()
                    if ratio >= 0.70:
                        score += ratio * 2.5

            if score > 0.0:
                scored_results.append({
                    "score": round(score, 2),
                    "document": doc,
                })

        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:limit]

    def autocomplete(self, prefix: str, limit: int = 5) -> List[Dict[str, str]]:
        """
        Autocomplete search suggestion for web search inputs.
        Returns matching titles and lemmas.
        """
        if not prefix or not prefix.strip():
            return []

        norm_pfx = strip_kashmiri_diacritics(prefix)
        raw_pfx = prefix.strip().lower()
        matches = []
        seen = set()

        for doc_id, doc in self.documents.items():
            title = doc["title"]
            title_norm = strip_kashmiri_diacritics(title)
            lemma = doc["metadata"].get("lemma", "")
            lemma_norm = strip_kashmiri_diacritics(lemma)
            aliases = [strip_kashmiri_diacritics(a) for a in doc["metadata"].get("aliases", [])]

            if (
                title.lower().startswith(raw_pfx)
                or title_norm.startswith(norm_pfx)
                or lemma_norm.startswith(norm_pfx)
                or any(a.startswith(norm_pfx) for a in aliases)
            ):
                key = f"{title}_{lemma}"
                if key not in seen:
                    seen.add(key)
                    matches.append({
                        "title": title,
                        "lemma": lemma,
                        "meaning": doc["text"][:80],
                        "script_text": doc["metadata"].get("devanagari", "") or doc["metadata"].get("persoarabic", "")
                    })
                    if len(matches) >= limit:
                        break

        return matches

    @classmethod
    def get_default_lexicon_index(cls) -> "KoshurSearchIndex":
        """Builds and returns pre-populated search index for the entire Kashmiri lexicon."""
        from koshur.lexicon.words_data import WORDS_DATA

        idx = cls()
        for i, entry in enumerate(WORDS_DATA):
            doc_id = f"word_{i}_{entry['lemma']}"
            title = f"{entry['lemma']} / {entry['devanagari']} / {entry['persoarabic']}"
            text = f"{entry['meaning_en']} | {entry['meaning_hi']}"
            idx.add_document(doc_id, title, text, metadata=entry)
        return idx
