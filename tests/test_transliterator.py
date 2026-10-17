import pytest
import koshur

def test_detect_script():
    assert koshur.detect_script("व्यथ्") == "devanagari"
    assert koshur.detect_script("ویٚتھ") == "persoarabic"
    assert koshur.detect_script("𑆯𑆳𑆫𑆢𑆳") == "sharada"
    assert koshur.detect_script("koshur") == "latin"

def test_devanagari_to_sharada():
    sh = koshur.to_sharada("कश्मीरी")
    assert any(koshur.scripts.sharada.is_sharada(c) for c in sh)

def test_devanagari_to_latin():
    lat = koshur.to_latin("व्यथ्")
    assert "vy" in lat or "v" in lat

def test_devanagari_to_persoarabic():
    ar = koshur.to_persoarabic("व्यथ्")
    assert any(koshur.scripts.persoarabic.is_persoarabic(c) for c in ar)

def test_latin_to_sharada():
    sh = koshur.to_sharada("Vyeth")
    assert any(koshur.scripts.sharada.is_sharada(c) for c in sh)

def test_latin_to_devanagari():
    dev = koshur.to_devanagari("koshur")
    assert any(koshur.scripts.devanagari.is_devanagari(c) for c in dev)

def test_latin_to_persoarabic():
    ar = koshur.to_persoarabic("Vyeth")
    assert any(koshur.scripts.persoarabic.is_persoarabic(c) for c in ar)

def test_roundtrip_transliteration():
    sample = "नमस्कार"
    sh = koshur.to_sharada(sample)
    back_to_dev = koshur.to_devanagari(sh)
    assert "न" in back_to_dev
