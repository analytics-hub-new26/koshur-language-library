import pytest
import koshur
from koshur.grammar.stemmer import stem_word

def test_v2_syntax_detection():
    # Kashmiri root clause: Raju is eating apple
    clause = ["राजू", "छु", "च्योन", "ख्यवान"]
    res = koshur.analyze_v2_syntax(clause)
    assert res["is_v2"] is True
    assert res["position"] == 2
    assert res["finite_verb"] == "छु"

def test_v2_syntax_adverb_fronting():
    # Kashmiri topicalized clause: Today is Raju reading
    clause = ["अज़", "छु", "राजू", "परान"]
    res = koshur.analyze_v2_syntax(clause)
    assert res["is_v2"] is True
    assert res["first_constituent"] == "अज़"
    assert res["finite_verb"] == "छु"

def test_noun_declension():
    dec = koshur.decline_noun("larka")
    assert "singular" in dec
    assert "ergative" in dec["singular"]
    assert "dative" in dec["singular"]

def test_verb_conjugation():
    conj = koshur.conjugate_verb("parun")
    assert "present_tense" in conj
    assert "1st_sing_masc" in conj["present_tense"]

def test_stemmer():
    assert stem_word("parān") == "par"
    assert stem_word("larkyav") == "lark"
