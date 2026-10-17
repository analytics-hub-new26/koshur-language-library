# coding: utf-8
"""
Tests for Koshur Folklore, Song Repertoire, and Sacred Kashmiri Pantheon.
"""

import pytest
import koshur
from koshur.folklore import (
    FOLKLORE_GENRES,
    get_folklore_genre,
    get_all_folklore_genres,
    KASHMIRI_DEITIES,
    ASHTA_BHAIRAVAS,
    lookup_deity,
    get_all_deities,
    get_guardian_bhairavas,
    TRADITIONAL_SONGS,
    get_song,
    search_songs,
    get_all_songs,
)


def test_folklore_genres_retrieval():
    genres = get_all_folklore_genres()
    assert len(genres) >= 8
    genre_ids = [g["id"] for g in genres]
    assert "wanvun" in genre_ids
    assert "rouf" in genre_ids
    assert "chakri" in genre_ids
    assert "sufiyana_kalam" in genre_ids
    assert "ladishah" in genre_ids
    assert "bhand_pather" in genre_ids

    # Test individual lookup
    w = get_folklore_genre("wanvun")
    assert w is not None
    assert w["name"] == "Wanvun"
    assert "sample_verse" in w
    assert "kashmiri_sharada" in w["sample_verse"]

    # Test case insensitive lookup
    r = get_folklore_genre("ROUF")
    assert r is not None
    assert r["id"] == "rouf"

    # Test invalid genre
    assert get_folklore_genre("unknown_genre_xyz") is None


def test_sacred_deities_and_tirthas():
    deities = get_all_deities()
    assert len(deities) >= 10

    # Test Sharika lookup by name and alias
    sharika = lookup_deity("sharika")
    assert sharika is not None
    assert "Chakreshwar" in sharika["name"]
    assert "Hari Parbat" in sharika["shrine_location"]

    # Test Kheer Bhawani lookup
    kb = lookup_deity("kheer bhawani")
    assert kb is not None
    assert "Maharagnya" in kb["name"]
    assert "Tulmulla" in kb["shrine_location"]

    # Test Nila Naga lookup
    nila = lookup_deity("nilanag")
    assert nila is not None
    assert "Nilamata Purana" in nila.get("mythological_origin", "") or "Nilamata" in nila.get("description", "")

    # Test Jwalamukhi Khrew lookup
    jwala = lookup_deity("khrew")
    assert jwala is not None
    assert "Jwala" in jwala["name"]


def test_ashta_bhairavas():
    bhairavas = get_guardian_bhairavas()
    assert len(bhairavas) == 8
    directions = [b["direction"] for b in bhairavas]
    assert "South" in directions
    assert "East" in directions
    assert "North" in directions
    assert "West" in directions

    # Check Maisuma and Rainawari locations
    locations = [b["location"] for b in bhairavas]
    assert any("Maisuma" in loc for loc in locations)
    assert any("Rainawari" in loc for loc in locations)
    assert any("Habba Kadal" in loc for loc in locations)


def test_traditional_songs_catalog():
    songs = get_all_songs()
    assert len(songs) >= 5

    # Test Habba Khatoon song lookup
    hk = get_song("habba_khatoon_roshe")
    assert hk is not None
    assert "Habba Khatoon" in hk["poet"]
    assert "kashmiri_sharada" in hk
    assert "kashmiri_dev" in hk
    assert "kashmiri_arabic" in hk
    assert "kashmiri_roman" in hk
    assert "translation_en" in hk

    # Test Rasul Mir song lookup
    rm = get_song("rasul_mir_posh_mal")
    assert rm is not None
    assert "Rasul Mir" in rm["poet"]

    # Test search songs
    search_res = search_songs("Habba")
    assert len(search_res) >= 1
    assert search_res[0]["id"] == "habba_khatoon_roshe"

    # Test searching by lyric word
    search_lyric = search_songs("kasturi")
    assert len(search_lyric) >= 1
    assert search_lyric[0]["id"] == "rasul_mir_posh_mal"


def test_folklore_and_deity_vocabulary_integration():
    # Verify overall lexicon size is expanded
    lex_size = koshur.get_lexicon_size()
    assert lex_size >= 550, f"Expected at least 550 words, got {lex_size}"

    # Verify musical instruments
    tumbak = koshur.lookup("tumbaknari")
    assert tumbak is not None
    assert "drum" in tumbak["meaning_en"].lower() or "goblet" in tumbak["meaning_en"].lower()
    assert tumbak["sharada"] != ""

    santoor = koshur.lookup("santoor")
    assert santoor is not None
    assert "dulcimer" in santoor["meaning_en"].lower()

    # Verify folklore creatures and deities
    shahmar = koshur.lookup("shahmar")
    assert shahmar is not None
    assert "serpent" in shahmar["meaning_en"].lower() or "dragon" in shahmar["meaning_en"].lower()

    yachh = koshur.lookup("yachh")
    assert yachh is not None
    assert "yaksha" in yachh["aliases"] or "sprite" in yachh["aliases"]

    # Verify literature verbs from Hatim's tales
    watun = koshur.lookup("watun")
    assert watun is not None
    assert watun["pos"] == "verb"

    trawun = koshur.lookup("trawun")
    assert trawun is not None
    assert trawun["pos"] == "verb"
