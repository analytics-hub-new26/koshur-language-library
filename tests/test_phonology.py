import pytest
import koshur
from koshur.phonology.vowels import KASHMIRI_VOWEL_INVENTORY, get_vowel_info
from koshur.phonology.palatalization import palatalize_consonant, apply_kashmiri_plural_mutation

def test_vowel_inventory_count():
    assert len(KASHMIRI_VOWEL_INVENTORY) >= 16

def test_central_vowels_present():
    symbols = [v["symbol"] for v in KASHMIRI_VOWEL_INVENTORY]
    assert "ə" in symbols
    assert "ə̄" in symbols
    assert "ɨ" in symbols
    assert "ɨ̄" in symbols

def test_palatalization():
    assert palatalize_consonant("t") == "ts"
    assert palatalize_consonant("th") == "tsh"
    assert palatalize_consonant("d") == "j"
    assert palatalize_consonant("m") == "mʲ"

def test_plural_mutation():
    mut = apply_kashmiri_plural_mutation("gōr")
    assert "ə̄" in mut or "ʲ" in mut

def test_to_ipa():
    ipa = koshur.to_ipa("व्यथ्")
    assert len(ipa) > 0
