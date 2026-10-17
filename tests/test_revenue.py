"""
Unit tests for Jammu & Kashmir Land Revenue Records & Governance Lexicon.
"""

import pytest
import koshur

def test_lookup_revenue_terms():
    jam = koshur.lookup_revenue_term("jamabandi")
    assert jam is not None
    assert "Record of Rights" in jam["meaning_en"]
    assert jam["term_urdu"] == "جمع بندی"

    khas = koshur.lookup_revenue_term("khasra")
    assert khas is not None
    assert "survey number" in khas["meaning_en"].lower()

def test_land_area_converter():
    # 1 Kanal = 20 Marlas = 5445 sq ft
    conv = koshur.convert_land_area(kanals=1.0)
    assert conv["total_marlas"] == 20.0
    assert conv["sq_feet"] == 5445.0

    # 8 Kanals = 1 Ghumaon / Acre = 43560 sq ft
    conv8 = koshur.convert_land_area(kanals=8.0)
    assert conv8["acres"] == 1.0
    assert conv8["sq_feet"] == 43560.0

def test_enriched_revenue_deeds():
    # Test legal deeds and contracts
    bai = koshur.lookup_revenue_term("bainama")
    assert bai is not None
    assert "sale" in bai["meaning_en"].lower()
    assert bai["category"] == "Deed"

    rahan = koshur.lookup_revenue_term("rahannama")
    assert rahan is not None
    assert "mortgage" in rahan["meaning_en"].lower()

    fak = koshur.lookup_revenue_term("fak_ur_rahan")
    assert fak is not None
    assert "redemption" in fak["meaning_en"].lower()

    hiba = koshur.lookup_revenue_term("hibanama")
    assert hiba is not None
    assert "gift" in hiba["meaning_en"].lower()

def test_tenure_and_status():
    malik_ala = koshur.lookup_revenue_term("malik_ala")
    assert malik_ala is not None
    assert "superior" in malik_ala["meaning_en"].lower()

    dakhil = koshur.lookup_revenue_term("dakhilkar")
    assert dakhil is not None
    assert "occupancy" in dakhil["meaning_en"].lower()

    khud = koshur.lookup_revenue_term("khudkasht")
    assert khud is not None
    assert "directly by the owner" in khud["meaning_en"].lower()

def test_revenue_search_and_categories():
    categories = koshur.list_categories()
    assert len(categories) >= 6
    assert "Register" in categories
    assert "Deed" in categories
    assert "Administration" in categories

    deeds = koshur.get_terms_by_category("Deed")
    assert len(deeds) >= 8

    # Search keyword
    res = koshur.search_revenue_terms("mortgage")
    assert len(res) >= 2
    keys = [r["key"] for r in res]
    assert "rahannama" in keys or "fak_ur_rahan" in keys

def test_explain_record():
    explanation = koshur.explain_record_type("jamabandi")
    assert "Record of Rights" in explanation
    assert "Document:" in explanation
