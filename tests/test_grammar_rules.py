"""
Unit tests for extended Kashmiri grammar rules and paradigms.
"""

import pytest
import koshur
from koshur.grammar import (
    decline_noun,
    form_plural,
    conjugate_verb,
    get_imperative,
    get_converb,
    NOUN_PARADIGMS,
    VERB_LEXICON
)

def test_noun_declensions():
    gur = decline_noun("gur", gender="masculine")
    assert gur["singular"]["direct"] == "gur (गुर / گُر)"
    assert "gərʲ" in gur["plural"]["direct"]

    kour = decline_noun("kour", gender="feminine")
    assert "kōr" in kour["singular"]["direct"]
    assert "kōrē" in kour["plural"]["direct"]

def test_form_plural():
    assert form_plural("kour", "feminine") == "kōrē (कूरे / کُوٗرے)"
    assert "gərʲ" in form_plural("gur", "masculine")

def test_verb_conjugation_and_ergativity():
    par = conjugate_verb("parun")
    assert par["is_transitive"] is True
    assert par["past_tense_agreement"]["masculine_singular_object"] == "por"
    assert par["past_tense_agreement"]["feminine_singular_object"] == "pər"

def test_verb_imperatives_and_converbs():
    imp_sg = get_imperative("parun", is_plural=False)
    assert "par" in imp_sg

    imp_pl = get_imperative("parun", is_plural=True)
    assert "pariv" in imp_pl

    cvb = get_converb("parun")
    assert "parith" in cvb
