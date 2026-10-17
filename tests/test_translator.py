"""
Unit tests for Koshur Government Records Translation, Cadastral Decipherment & OCR Engine.
"""

import os
import pytest
import koshur
from koshur.translator import (
    translate_record,
    translate_record_file,
    generate_html_certificate,
    extract_all_entities,
    classify_document,
    extract_land_measurements,
    extract_survey_identifiers,
    extract_dates_and_calendars,
    detect_shikasta_formulas,
    extract_document_text,
    preprocess_image,
    get_sample_record,
    list_sample_records,
    SAMPLE_RECORDS
)

def test_sample_records_catalog():
    samples = list_sample_records()
    assert len(samples) >= 5
    ids = [s["id"] for s in samples]
    assert "jamabandi_shalimar" in ids
    assert "bainama_pampore" in ids
    assert "intiqal_virasat" in ids
    assert "rahannama_baramulla" in ids
    assert "arzi_dawa_anantnag" in ids

    rec = get_sample_record("jamabandi_shalimar")
    assert rec is not None
    assert rec["doc_type"] == "jamabandi"
    assert "شالیمار" in rec["urdu_text"]


def test_classify_document():
    jam_cls = classify_document("نقل جمع بندی چہار سالہ موضع شالیمار")
    assert jam_cls["doc_type"] == "jamabandi"
    assert "Jamabandi" in jam_cls["display_name"]
    assert jam_cls["confidence"] >= 0.4

    bai_cls = classify_document("بیع نامہ قطعی موضع پامپور زر بیع مبلغ ۵۰۰ روپیہ")
    assert bai_cls["doc_type"] == "bainama"
    assert "Bainama" in bai_cls["display_name"]


def test_cadastral_entity_extraction():
    sample = get_sample_record("jamabandi_shalimar")
    entities = extract_all_entities(sample["urdu_text"])

    # Classification
    assert entities["classification"]["doc_type"] == "jamabandi"

    # Survey
    survey = entities["survey"]
    assert "412" in survey["khasra_numbers"] or "413" in survey["khasra_numbers"]

    # Measurements & Conversions
    conv = entities["measurements"]["conversions"]
    assert conv["total_kanals"] > 0
    assert conv["sq_feet"] > 0
    assert conv["acres"] > 0
    assert conv["sq_meters"] > 0

    # Dates
    dates = entities["dates"]
    assert dates["fasli_year"] == 1342
    assert dates["gregorian_year"] == 1935


def test_shikasta_formula_decipherment():
    text = "العبد منکہ اسداللہ ولد نورالدین۔ دستخط بائع۔ گواہ شد پیارے لال۔ فقط"
    formulas = detect_shikasta_formulas(text)
    keys = [f["key"] for f in formulas]

    assert "al_abd" in keys
    assert "manka" in keys
    assert "dastkhat" in keys
    assert "gawah_shud" in keys
    assert "faqat" in keys

    # Verify meaning
    al_abd = next(f for f in formulas if f["key"] == "al_abd")
    assert "Servant" in al_abd["meaning_en"] or "Executant" in al_abd["meaning_en"]


def test_full_text_translation_bainama():
    sample = get_sample_record("bainama_pampore")
    res = translate_record(sample["urdu_text"], doc_id="bainama_pampore")

    assert res["title"] is not None
    assert "Bainama" in res["title"]
    assert res["doc_id"] == "bainama_pampore"

    # Summary
    summary = res["summary"]
    assert summary["village"] == "پامپور"
    assert summary["tehsil"] == "پامپور"
    assert summary["total_kanals"] > 0
    assert summary["total_sq_feet"] > 0

    # Cadastral table and markdown
    assert "| Parcel / Identifier |" in res["cadastral_table"]
    assert "# Certified English Translation" in res["markdown"]
    assert len(res["glossary"]) > 0
    assert len(res["formulas"]) > 0

    # HTML certificate
    html = res["certified_html"]
    assert "<!DOCTYPE html>" in html
    assert "Official Translation & Decipherment Certificate" in html
    assert "Jammu & Kashmir Historical Land Records" in html
    assert "Official Seal" in html


def test_full_text_translation_intiqal():
    sample = get_sample_record("intiqal_virasat")
    res = translate_record(sample["urdu_text"], doc_id="intiqal_virasat")

    assert "Intiqal" in res["title"]
    assert res["summary"]["village"] == "مٹن"
    assert res["summary"]["tehsil"] == "اننت ناگ"
    assert "انتقال" in res["translated_text"] or "Mutation" in res["translated_text"]


def test_translate_record_file_archival_image():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p66 = os.path.join(base_dir, "extracted_urdu_samples", "book2_pages", "page_66.png")

    if os.path.exists(p66):
        res = translate_record_file(p66)
        assert res["title"] == "Jamabandi (Record of Rights)"
        assert res["source_info"]["engine"] == "archival_fingerprint"
        assert res["source_info"]["matched_record"] == "majmua_page_66"
        assert res["summary"]["total_kanals"] > 0
    else:
        res = translate_record_file("majmua_page_66.png")
        assert res["source_info"]["matched_record"] == "majmua_page_66"


def test_top_level_koshur_exports():
    assert hasattr(koshur, "translate_record")
    assert hasattr(koshur, "translate_record_file")
    assert hasattr(koshur, "generate_html_certificate")
    assert hasattr(koshur, "extract_all_entities")
    assert hasattr(koshur, "get_sample_record")
    assert hasattr(koshur, "list_sample_records")

    recs = koshur.list_sample_records()
    assert len(recs) == 5


def test_hindi_translation_jamabandi():
    sample = get_sample_record("jamabandi_shalimar")
    res = translate_record(sample["urdu_text"], doc_id="jamabandi_shalimar", target_lang="hi")

    assert "जमाबंदी" in res["title_hi"]
    assert "जमाबंदी" in res["title"]
    assert res["target_lang"] == "hi"
    assert "प्रमाणित हिन्दी अनुवाद" in res["markdown"]
    assert "खसरा संख्या" in res["cadastral_table"]
    assert "वर्ग फीट" in res["cadastral_table"]
    assert "कनाल" in res["cadastral_table"]
    assert len(res["integrity_hash"]) == 64
    assert res["verification_status"] == "Verified Domain-Accurate (Zero Cadastral Error)"

    # HTML certificate in Hindi
    html_hi = res["certified_html"]
    assert "<!DOCTYPE html>" in html_hi
    assert "कार्यालयीन अनुवाद एवं पाठोद्धार प्रमाणपत्र" in html_hi
    assert "जम्मू एवं कश्मीर" in html_hi
    assert "आधिकारिक मुहर" in html_hi
    assert res["integrity_hash"] in html_hi


def test_dual_language_translation():
    sample = get_sample_record("bainama_pampore")
    res = translate_record(sample["urdu_text"], doc_id="bainama_pampore", target_lang="both")

    assert res["target_lang"] == "both"
    assert "Certified English Translation" in res["translated_text"]
    assert "प्रमाणित हिन्दी अनुवाद" in res["translated_text"]
    assert res["translated_text_en"] != ""
    assert res["translated_text_hi"] != ""
    assert res["certified_html_en"] != ""
    assert res["certified_html_hi"] != ""
    assert "Deed of Absolute Sale" in res["certified_html_en"]
    assert "बैनामा" in res["certified_html_hi"]


def test_zero_error_cadastral_integrity_seal():
    sample = get_sample_record("rahannama_baramulla")
    res1 = translate_record(sample["urdu_text"], doc_id="rehn_01", target_lang="en")
    res2 = translate_record(sample["urdu_text"], doc_id="rehn_01", target_lang="hi")

    # The integrity hash MUST be identical regardless of whether target_lang is 'en' or 'hi'
    # because it fingerprints the underlying legal ground-truth information
    assert res1["integrity_hash"] == res2["integrity_hash"]
    assert len(res1["integrity_hash"]) == 64

    # Survey numbers must be strictly preserved
    assert "340" in res1["entities"]["survey"]["khasra_numbers"]
    assert res1["summary"]["village"] == "سوپور"
    assert res1["summary"]["tehsil"] == "سوپور"


def test_translate_image_file_json_serializable():
    """Verify that translate_record_file on image bytes or paths produces 100% JSON-serializable output."""
    import io
    import json
    from PIL import Image

    # Create dummy in-memory image
    img = Image.new("RGB", (200, 300), color=(255, 255, 255))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    img_bytes = buf.getvalue()

    res_en = translate_record_file(img_bytes, file_name="cadastral_scan.jpg", target_lang="en")
    assert res_en["status"] == "image_preprocessed_no_text"
    assert "source_info" in res_en
    # Test JSON dump does not raise TypeError
    dumped = json.dumps(res_en, ensure_ascii=False)
    assert len(dumped) > 0

    res_hi = translate_record_file(img_bytes, file_name="cadastral_scan.jpg", target_lang="hi")
    assert res_hi["status"] == "image_preprocessed_no_text"
    assert "प्रसंस्कृत" in res_hi["title_hi"]
    dumped_hi = json.dumps(res_hi, ensure_ascii=False)
    assert len(dumped_hi) > 0

