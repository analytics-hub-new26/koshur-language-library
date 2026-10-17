"""
Kashmiri Corpus & Linguistic Text Analyzer:
Calculates lexical statistics, script distribution, and word frequencies.
"""

from typing import Dict, Any
from koshur.nlp.tokenizer import tokenize, sent_tokenize
from koshur.scripts.transliterator import detect_script

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Computes linguistic summary statistics for Kashmiri text.
    """
    if not text:
        return {"error": "Empty text"}

    sentences = sent_tokenize(text)
    words = tokenize(text)
    script = detect_script(text)
    
    unique_words = set(w.lower() for w in words if w.isalnum())
    
    return {
        "detected_script": script,
        "sentence_count": len(sentences),
        "token_count": len(words),
        "unique_word_count": len(unique_words),
        "lexical_diversity": round(len(unique_words) / max(1, len(words)), 3),
        "sample_sentences": sentences[:3],
    }
