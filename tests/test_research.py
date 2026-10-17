"""
Unit tests for koshur.research linguistic fieldwork, glossing, and corpus metrics.
"""

import pytest
import koshur
from koshur.research import (
    generate_leipzig_gloss,
    get_gloss_tag_description,
    export_conllu,
    export_tei_xml,
    export_jsonld,
    compute_lexical_metrics,
    verify_v2_word_order
)

def test_leipzig_glossing():
    src = ["aslam-an", "por", "akhavbar"]
    gls = ["Aslam-ERG", "read.PST.M.SG", "newspaper.NOM.M.SG"]
    trans = "Aslam read the newspaper."

    out_text = generate_leipzig_gloss(src, gls, trans, output_format="text")
    assert "aslam-an" in out_text
    assert "Aslam-ERG" in out_text
    assert "Aslam read the newspaper" in out_text

    out_latex = generate_leipzig_gloss(src, gls, trans, output_format="latex")
    assert "\\gll" in out_latex
    assert "\\glt" in out_latex

    out_md = generate_leipzig_gloss(src, gls, trans, output_format="markdown")
    assert "|" in out_md

def test_glossing_tag_lookup():
    assert "Ergative" in get_gloss_tag_description("ERG")
    assert "Dative" in get_gloss_tag_description("DAT")
    assert "Verb-Second" in get_gloss_tag_description("V2")

def test_lexical_metrics():
    sample = "सु छु किताब परान। सो छ़े चाय चवान। सु छु किताब परान।"
    metrics = compute_lexical_metrics(sample)
    assert metrics["tokens"] >= 10
    assert 0.0 < metrics["ttr"] <= 1.0
    assert metrics["hapax_count"] >= 1

def test_verify_v2_word_order():
    # V2 Compliant: Topic + Auxiliary in position 2
    v2_valid = verify_v2_word_order("राजू छु किताब परान")
    assert v2_valid["is_v2_compliant"] is True
    assert v2_valid["finite_verb_position"] == 2

    # V2 Non-compliant (finite verb at end)
    v2_invalid = verify_v2_word_order("राजू किताब परान छु")
    assert v2_invalid["is_v2_compliant"] is False

def test_corpus_export():
    entries = [
        {"lemma": "Vyeth", "roman": "Vyeth", "devanagari": "व्यथ्", "persoarabic": "ویٚتھ", "sharada": "𑆮𑇀𑆪𑆼𑆡𑇀", "meaning_en": "Jhelum River", "meaning_hi": "झेलम नदी", "pos": "noun"}
    ]
    tei = export_tei_xml(entries, title="Test Lexicon")
    assert "<TEI" in tei
    assert "Vyeth" in tei

    jld = export_jsonld(entries)
    assert "ontolex:LexicalEntry" in jld

def test_historical_sources_catalog():
    sources = koshur.get_research_sources()
    assert len(sources) >= 8
    
    # Check Grierson 1932 is cataloged
    grierson = koshur.search_research_sources("Grierson")
    assert len(grierson) >= 2
    assert any("Dictionary" in s["title"] for s in grierson)
    
    # Check 75129.pdf epigraphic corpus is cataloged
    epigraphia = koshur.search_research_sources("75129")
    assert len(epigraphia) == 1
    assert "Epigraphia Indica" in epigraphia[0]["title"]

def test_digital_library_corpus():
    stats = koshur.get_library_stats()
    assert stats["total_volumes"] >= 60
    assert stats["total_words"] >= 5_500_000
    
    # Check category filters
    books = koshur.get_sources_by_category("books")
    assert len(books) >= 30
    discourses = koshur.get_sources_by_category("discourses")
    assert len(discourses) >= 15
    catalogues = koshur.get_sources_by_category("catalogues")
    assert len(catalogues) >= 2
    papers = koshur.get_sources_by_category("papers")
    assert len(papers) >= 7

def test_library_full_text_search():
    results = koshur.search_library_text("vitasta", max_results=5)
    assert len(results) >= 1
    assert any("vitasta" in r["snippet"].lower() for r in results)
    
    # Read a sample source
    v2_paper = koshur.read_library_source("hook_koul_1996_v2", max_chars=200)
    assert v2_paper is not None
    assert "Verb-Second" in v2_paper or "V-2" in v2_paper

def test_library_learning_progression_levels():
    elem = koshur.get_sources_by_level("elementary")
    assert len(elem) >= 8
    assert any("Spoken Kashmiri" in s["title"] for s in elem)
    assert any("Kashur Grammar" in s["title"] for s in elem)
    
    inter = koshur.get_sources_by_level("intermediate")
    assert len(inter) >= 13
    assert any("Folk-Tales" in s["title"] for s in inter)
    assert any("Kaishrik" in s["title"] or "Kạ̄shrik" in s["title"] for s in inter)
    
    adv = koshur.get_sources_by_level("advanced")
    assert len(adv) >= 25
    assert any("Kashir Dictionary" in s["title"] for s in adv)
    assert any("Kāshīr" in s["title"] or "History" in s["title"] for s in adv)
    
    stats = koshur.get_library_stats()
    assert "level_counts" in stats
    assert stats["level_counts"]["elementary"] >= 8
    assert stats["level_counts"]["intermediate"] >= 13
    assert stats["level_counts"]["advanced"] >= 25



