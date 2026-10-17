import pytest
import koshur

def test_dialect_info():
    kish = koshur.get_dialect_info("kishtwari")
    assert "Kishtwar" in kish["region"]

    pog = koshur.get_dialect_info("poguli")
    assert "Ramban" in pog["region"]

def test_compare_dialects():
    comp = koshur.compare_dialects("brother")
    assert len(comp) > 0
    assert "bhrāu" in comp[0]["kishtwari"]
    assert "bhrāu" in comp[0]["poguli"]
    assert "bhrā" in comp[0]["siraji"]

def test_compare_dialects_expansion():
    comp_v = koshur.compare_dialects("Vyeth")
    assert len(comp_v) > 0
    assert "vyath" in comp_v[0]["kishtwari"].lower()

    comp_w = koshur.compare_dialects("water")
    assert len(comp_w) > 0
    assert "pānī" in comp_w[0]["kishtwari"]
