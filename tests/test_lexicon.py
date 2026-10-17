import pytest
import koshur

def test_lookup_word():
    entry = koshur.lookup("Vyeth")
    assert entry is not None
    assert "Jhelum" in entry["meaning_en"]
    assert entry["devanagari"] == "व्यथ्"

def test_fuzzy_and_alias_lookup():
    # Test normalized / alias / fuzzy resolution
    res_phoran = koshur.lookup("phoran")
    assert res_phoran is not None
    assert res_phoran["lemma"] == "Phēran"

    res_pheran = koshur.lookup("pheran")
    assert res_pheran is not None
    assert res_pheran["lemma"] == "Phēran"

    res_kangri = koshur.lookup("kangri")
    assert res_kangri is not None
    assert res_kangri["lemma"] == "Kāngrī"

    res_vitasta = koshur.lookup("vitasta")
    assert res_vitasta is not None
    assert res_vitasta["lemma"] == "Vyeth"

    res_snow = koshur.lookup("snow")
    assert res_snow is not None
    assert res_snow["lemma"] == "Sheen"

def test_search_words():
    results = koshur.search_words("tea")
    assert len(results) > 0
    lemmas = [r["lemma"] for r in results]
    assert any("Qahwah" in l or "Chāi" in l for l in lemmas)

def test_tags_filtering():
    cuisine_words = koshur.get_words_by_tag("cuisine")
    assert len(cuisine_words) >= 5
    tags = koshur.get_all_tags()
    assert "geography" in tags
    assert "cuisine" in tags
    assert "culture" in tags

def test_proverbs():
    p = koshur.get_proverb(1)
    assert p is not None
    assert "reap" in p["translation_en"]

def test_expanded_proverbs():
    all_p = koshur.get_all_proverbs()
    assert len(all_p) >= 30
    nund = koshur.search_proverbs("Nund Rishi")
    assert len(nund) >= 1
    lal = koshur.search_proverbs("Lalleshwari")
    assert len(lal) >= 1
    knowles = koshur.search_proverbs("Knowles")
    assert len(knowles) >= 1

def test_large_lexicon_size():
    assert koshur.get_lexicon_size() >= 1000
    # Check newly added items from Grierson and Elmslie
    wular = koshur.lookup("wular")
    assert wular is not None
    assert "Mahapadmasaras" in wular["meaning_en"] or "Wular" in wular["lemma"]
    
    kandur = koshur.lookup("kandur")
    assert kandur is not None
    assert "baker" in kandur["meaning_en"].lower()

    # Check newly added ethnobotany, anatomy, and craft words
    apricot = koshur.lookup("tsher")
    assert apricot is not None
    assert "apricot" in apricot["meaning_en"].lower()

    khatamband = koshur.lookup("khatamband")
    assert khatamband is not None
    assert "ceiling" in khatamband["meaning_en"].lower()

    # Check newly extracted authentic terms from Toshakhani & Elmslie
    trawun = koshur.lookup("trawun")
    assert trawun is not None
    assert "abandon" in trawun["meaning_en"].lower()

    galun = koshur.lookup("galun")
    assert galun is not None
    assert "melt" in galun["meaning_en"].lower()

    sungal = koshur.lookup("sungal")
    assert sungal is not None
    assert "spruce" in sungal["meaning_en"].lower()

    # Check terms extracted from newly acquired historical volumes
    radh = koshur.lookup("radh")
    assert radh is not None
    assert "floating" in radh["meaning_en"].lower()

    kruh = koshur.lookup("kruh")
    assert kruh is not None
    assert "distance" in kruh["meaning_en"].lower() or "league" in kruh["meaning_en"].lower()

    pravarapura = koshur.lookup("pravarapura")
    assert pravarapura is not None
    assert "srinagar" in pravarapura["meaning_en"].lower()

def test_random_proverb():
    p = koshur.random_proverb()
    assert "translation_en" in p

def test_number_to_koshur():
    assert koshur.number_to_koshur(1) == "akh"
    assert koshur.number_to_koshur(2) == "zə"
    assert koshur.number_to_koshur(10) == "dəh"
    assert koshur.number_to_koshur(100) == "hath"

def test_koshur_to_number():
    assert koshur.koshur_to_number("akh") == 1
    assert koshur.koshur_to_number("hath") == 100
