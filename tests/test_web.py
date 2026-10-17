"""
Unit tests for koshur.web UI localization, HTML helpers, and virtual keyboards.
"""

import pytest
import koshur
from koshur.web import (
    get_ui_string,
    get_all_ui_keys,
    export_i18n_json,
    get_script_attributes,
    generate_webfont_css,
    wrap_html_text,
    get_keyboard_layout,
    transcribe_keystrokes
)

def test_ui_strings_coverage():
    keys = get_all_ui_keys()
    assert len(keys) >= 30
    assert "home" in keys
    assert "search" in keys
    assert "save" in keys
    assert "login" in keys
    assert "delete" in keys

def test_get_ui_string_scripts():
    deva = get_ui_string("home", script="devanagari")
    arab = get_ui_string("home", script="persoarabic")
    shrd = get_ui_string("home", script="sharada")
    rom = get_ui_string("home", script="roman")
    en = get_ui_string("home", script="english")

    assert deva == "सादर"
    assert arab == "سادُر"
    assert "𑆱" in shrd
    assert rom == "Sadur"
    assert en == "Home"

def test_export_i18n_json():
    data = export_i18n_json(script="devanagari")
    assert isinstance(data, dict)
    assert data["home"] == "सादर"
    assert data["search"] == "खोज़"

def test_get_script_attributes():
    arab_attrs = get_script_attributes("persoarabic")
    assert arab_attrs["dir"] == "rtl"
    assert arab_attrs["lang"] == "ks-Arab"

    deva_attrs = get_script_attributes("devanagari")
    assert deva_attrs["dir"] == "ltr"
    assert deva_attrs["lang"] == "ks-Deva"

    shrd_attrs = get_script_attributes("sharada")
    assert shrd_attrs["dir"] == "ltr"
    assert shrd_attrs["lang"] == "ks-Shrd"

def test_generate_webfont_css():
    css = generate_webfont_css()
    assert "Noto+Nastaliq+Urdu" in css
    assert "Noto+Sans+Devanagari" in css
    assert "Noto+Sans+Sharada" in css
    assert ".koshur-persoarabic" in css
    assert ".koshur-devanagari" in css
    assert ".koshur-sharada" in css

def test_wrap_html_text():
    html = wrap_html_text("کٲشُر", script="persoarabic")
    assert 'dir="rtl"' in html
    assert 'lang="ks-Arab"' in html
    assert 'class="koshur-persoarabic"' in html
    assert "کٲشُر" in html

def test_keyboard_layouts():
    kb_arab = get_keyboard_layout("persoarabic")
    assert kb_arab["direction"] == "rtl"
    assert len(kb_arab["rows"]) >= 4

    kb_deva = get_keyboard_layout("devanagari")
    assert kb_deva["direction"] == "ltr"
    assert len(kb_deva["rows"]) >= 5

def test_transcribe_keystrokes():
    res = transcribe_keystrokes("koshur", target_script="devanagari")
    assert "कश" in res or "कोश" in res

    res_shrd = transcribe_keystrokes("Vyeth", target_script="sharada")
    assert "𑆮" in res_shrd
