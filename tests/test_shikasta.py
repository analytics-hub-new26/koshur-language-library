"""
Unit tests for Khat-i-Shikast Palaeography, Orthography, and Decipherment Engine.
"""

import pytest
import koshur
from datetime import date
from koshur.scripts.shikasta import (
    SHIKASTA_RULES,
    SHIKASTA_ABBREVIATIONS,
    explain_shikasta_rule,
    list_shikasta_rules,
    lookup_shikasta_abbreviation,
    list_shikasta_abbreviations,
    convert_traditional_weight,
    format_traditional_currency,
    calculate_fasli_year,
)

def test_list_and_explain_rules():
    rules = list_shikasta_rules()
    assert len(rules) >= 8
    assert "alif" in rules
    assert "dal_series" in rules
    assert "re_series" in rules

    alif_rule = explain_shikasta_rule("alif")
    assert alif_rule is not None
    assert "continuous" in alif_rule["shikasta_rule"].lower() or "connect" in alif_rule["shikasta_rule"].lower()
    assert len(alif_rule["examples"]) >= 3

def test_explain_invalid_rule():
    assert explain_shikasta_rule("non_existent_rule") is None

def test_shikasta_abbreviations():
    abbrevs = list_shikasta_abbreviations()
    assert len(abbrevs) >= 10

    # Look up well-known scribal abbreviations
    abd = lookup_shikasta_abbreviation("al_abd")
    assert abd is not None
    assert "servant" in abd["meaning_en"].lower() or "signatory" in abd["meaning_en"].lower()

    naql = lookup_shikasta_abbreviation("naql_mutabiq_asl")
    assert naql is not None
    assert "copy" in naql["meaning_en"].lower() or "original" in naql["meaning_en"].lower()

    dast = lookup_shikasta_abbreviation("dastkhat")
    assert dast is not None
    assert "signature" in dast["meaning_en"].lower()

def test_traditional_weights():
    # 1 Tola = 11.66 grams
    tola = convert_traditional_weight(tolas=1.0)
    assert tola["total_grams"] == pytest.approx(11.66, rel=1e-2)

    # 1 Ser = 80 Tolas = 933.12 grams
    ser = convert_traditional_weight(sers=1.0)
    assert ser["total_grams"] == pytest.approx(933.12, rel=1e-2)

    # 1 Maund = 40 Sers
    maund = convert_traditional_weight(maunds=1.0)
    assert maund["total_kg"] == pytest.approx(37.32, rel=1e-2)

def test_currency_formatting():
    # Rupees, Annas, Paisas
    curr = format_traditional_currency(rupees=10, annas=8, paisas=2)
    assert curr["rupees"] == 10
    assert curr["annas"] == 8
    assert curr["paisas"] == 2
    assert curr["decimal_rupees"] == pytest.approx(10.5312, rel=1e-3)
    assert "\u0631\u0648\u067e\u06cc\u06c1" in curr["urdu_text"]

def test_fasli_year_calculation():
    # Fasli year roughly = Gregorian year - 592/593
    dt = date(2026, 10, 9)
    fasli_info = calculate_fasli_year(dt)
    assert "fasli_year" in fasli_info
    assert fasli_info["fasli_year"] in [1433, 1434]
    assert "akbar" in fasli_info["explanation"].lower()

def test_top_level_exports():
    assert hasattr(koshur, "explain_shikasta_rule")
    assert hasattr(koshur, "lookup_shikasta_abbreviation")
    assert hasattr(koshur, "convert_traditional_weight")
    assert hasattr(koshur, "format_traditional_currency")
    assert hasattr(koshur, "calculate_fasli_year")
