"""
Unit tests for koshur.search diacritic-insensitive indexer and fuzzy engine.
"""

import pytest
import koshur
from koshur.search import strip_kashmiri_diacritics, KoshurSearchIndex

def test_strip_diacritics():
    # Perso-Arabic harakat
    raw_arab = "کٲشُر"
    stripped_arab = strip_kashmiri_diacritics(raw_arab)
    assert len(stripped_arab) <= len(raw_arab)

    # Devanagari matras
    raw_deva = "कॉशुर"
    stripped_deva = strip_kashmiri_diacritics(raw_deva)
    assert "क" in stripped_deva

    # Roman macrons
    raw_rom = "Phēran"
    assert strip_kashmiri_diacritics(raw_rom) == "pheran"

def test_koshur_search_index():
    idx = KoshurSearchIndex()
    idx.add_document("doc1", "Samovar", "Traditional copper tea urn for brewing Kehwa", {"lemma": "Samōvar", "tags": ["tea"]})
    idx.add_document("doc2", "Pheran", "Long woolen traditional cloak", {"lemma": "Phēran", "tags": ["clothing"]})

    # Search with diacritic variation
    results = idx.search("samowar")
    assert len(results) > 0
    assert results[0]["document"]["id"] == "doc1"

    # Search by tag or partial
    res_cloth = idx.search("cloak")
    assert len(res_cloth) > 0
    assert res_cloth[0]["document"]["id"] == "doc2"

def test_search_autocomplete():
    idx = KoshurSearchIndex.get_default_lexicon_index()
    suggestions = idx.autocomplete("phe", limit=5)
    assert len(suggestions) > 0
    assert any("pheran" in strip_kashmiri_diacritics(s["lemma"]) for s in suggestions)
