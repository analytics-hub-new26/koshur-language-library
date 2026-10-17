"""
Domain-Specific Cadastral & Legal Entity Extraction Engine:
Extracts structured administrative metadata, survey plot identifiers (Khasra, Khewat, Khatoni),
parties/signatories, land measurements with automated metric/imperial conversions,
soil classifications, pre-decimal currency, historical calendar dates, and Shikasta scribal formulas.
"""

import re
from typing import Dict, Any, List, Optional
from datetime import date
from koshur.revenue.land_records import convert_land_area, lookup_revenue_term
from koshur.scripts.shikasta import (
    lookup_shikasta_abbreviation,
    list_shikasta_abbreviations,
    calculate_fasli_year
)

# Eastern Arabic to Western digit mapping
ARABIC_DIGITS_MAP = {
    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
    '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9',
    '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
    '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
}

def normalize_digits(text: str) -> str:
    """Converts Eastern Arabic/Persian numerals to standard Western digits (0-9)."""
    for ar, w in ARABIC_DIGITS_MAP.items():
        text = text.replace(ar, w)
    return text

DOC_TYPE_PATTERNS = [
    ("jamabandi", [r"جمع\s*بندی", r"چہار\s*سالہ", r"record\s*of\s*rights", r"ror"], "Jamabandi (Record of Rights)"),
    ("khasra_girdawari", [r"خسرہ\s*گرداوری", r"گرداوری", r"فصل\s*پڑتال", r"harvest\s*inspection"], "Khasra Girdawari (Harvest Inspection Register)"),
    ("intiqal", [r"انتقال", r"وراثت", r"فوتیدگی", r"mutation", r"داخل\s*خارج"], "Intiqal (Mutation Order)"),
    ("bainama", [r"بیع\s*نامہ", r"بیع\s*قطعی", r"زر\s*بیع", r"بائع", r"فروخت\s*قطعی", r"sale\s*deed"], "Bainama (Deed of Absolute Sale)"),
    ("rahannama", [r"رہن\s*نامہ", r"رہن\s*بالقبض", r"مرتہن", r"راہن", r"زر\s*رہن", r"mortgage\s*deed"], "Rahannama (Mortgage Deed)"),
    ("hibanama", [r"ہبہ\s*نامہ", r"واہب", r"موہوب", r"gift\s*deed"], "Hibanama (Deed of Gift)"),
    ("wasiyatnama", [r"وصیت\s*نامہ", r"موصی", r"will"], "Wasiyatnama (Last Will and Testament)"),
    ("patta_araziyat", [r"پٹہ\s*اراضیات", r"اجارہ", r"lease\s*deed"], "Patta Araziyat (Agricultural Lease)"),
    ("kirayanama", [r"کرایہ\s*نامہ", r"tenancy\s*agreement"], "Kirayanama (Rent / Tenancy Agreement)"),
    ("tamassuk", [r"تمسک", r"قرضہ", r"promissory\s*bond"], "Tamassuk (Promissory Debt Bond)"),
    ("arzi_dawa_lagan", [r"عرضی\s*دعویٰ", r"بقایا\s*لگان", r"مدعی", r"مدعا\s*علیہ"], "Arzi Dawa Lagan (Plaint for Rent Arrears)"),
    ("fard", [r"فرد\s*ملکیت", r"فرد\s*حقیقت", r"نقل\s*فرد", r"fard"], "Fard (Certified Title Extract)")
]

def classify_document(text: str) -> Dict[str, Any]:
    """Classifies legal/revenue document type based on domain keyword frequency and regex."""
    text_norm = normalize_digits(text.lower())
    best_type = "official_revenue_record"
    best_name = "Government Revenue & Land Record"
    max_score = 0

    for code, patterns, display_name in DOC_TYPE_PATTERNS:
        score = sum(len(re.findall(p, text_norm, re.IGNORECASE)) for p in patterns)
        if score > max_score:
            max_score = score
            best_type = code
            best_name = display_name

    confidence = min(0.99, max(0.40, max_score * 0.25)) if max_score > 0 else 0.40
    return {
        "doc_type": best_type,
        "display_name": best_name,
        "score": max_score,
        "confidence": round(confidence, 2)
    }

def extract_administrative_jurisdiction(text: str) -> Dict[str, Optional[str]]:
    """Extracts District, Tehsil, Village/Mouza, and Mahal from record."""
    jurisdiction = {
        "district": None,
        "tehsil": None,
        "village": None,
        "mahal": None
    }

    # Match District (ضلع)
    m_dist = re.search(r"ضلع\s*([^\s،,۔\r\n]+(?:\s+[^\s،,۔\r\n]+)?)", text)
    if m_dist:
        jurisdiction["district"] = m_dist.group(1).strip()

    # Match Tehsil (تحصیل)
    m_teh = re.search(r"تحصیل\s*([^\s،,۔\r\n]+(?:\s+[^\s،,۔\r\n]+)?)", text)
    if m_teh:
        jurisdiction["tehsil"] = m_teh.group(1).strip()

    # Match Village / Mouza (موضع / قصبہ / دیہہ)
    m_vil = re.search(r"(?:موضع|قصبہ|دیہہ)\s*([^\s،,۔\r\n]+(?:\s+[^\s،,۔\r\n]+)?)", text)
    if m_vil:
        jurisdiction["village"] = m_vil.group(1).strip()

    # Match Mahal / Patti (محل / پٹی)
    m_patti = re.search(r"(?:پٹی|محل)\s*[:/]?\s*([^\s،,۔\r\n]+)", text)
    if m_patti:
        jurisdiction["mahal"] = m_patti.group(1).strip()

    return jurisdiction

def extract_survey_identifiers(text: str) -> Dict[str, Any]:
    """Extracts Khasra, Khewat, and Khatoni numbers."""
    norm = normalize_digits(text)

    # Khasra numbers (خسرہ نمبر)
    khasras = re.findall(r"خسرہ\s*(?:نمبر)?\s*([0-9]+(?:/[0-9]+)?)", norm)

    # Khewat numbers (کھیوٹ نمبر)
    khewats = re.findall(r"کھیوٹ\s*(?:نمبر)?\s*([0-9]+)", norm)

    # Khatoni numbers (کھتونی نمبر)
    khatonis = re.findall(r"کھتونی\s*(?:نمبر)?\s*([0-9]+)", norm)

    is_minjumla = bool(re.search(r"منجملہ", text))
    is_tatima = bool(re.search(r"تتمہ", text))

    return {
        "khasra_numbers": sorted(list(set(khasras))),
        "khewat_numbers": sorted(list(set(khewats))),
        "khatoni_numbers": sorted(list(set(khatonis))),
        "is_minjumla": is_minjumla,
        "is_tatima": is_tatima
    }

def extract_land_measurements(text: str) -> Dict[str, Any]:
    """Extracts Kanals, Marlas, Sersai, and Karams with automated conversions and parcel breakdown."""
    norm = normalize_digits(text)
    total_kanals = 0.0
    total_marlas = 0.0
    total_sersai = 0.0
    parcels = []

    # Detect parcel-specific breakdown (e.g. خسرہ نمبر ۴۱۲: رقبہ ۳ کنال ۸ مرلہ — آبی اول)
    parcel_matches = re.findall(
        r"خسرہ\s*نمبر\s*([0-9]+(?:/[0-9]+)?)\s*[:/]?\s*رقبہ\s*([0-9]+(?:\.[0-9]+)?)\s*کنال\s*(?:معہ\s*)?([0-9]+(?:\.[0-9]+)?)\s*مرلہ(?:\s*—\s*([^\r\n]+))?",
        norm
    )
    for p_khasra, p_k, p_m, p_soil in parcel_matches:
        pk_f = float(p_k)
        pm_f = float(p_m)
        p_conv = convert_land_area(kanals=pk_f, marlas=pm_f)
        parcels.append({
            "khasra": p_khasra,
            "kanals": pk_f,
            "marlas": pm_f,
            "soil": p_soil.strip() if p_soil else "",
            "conversions": p_conv
        })

    # Check for explicit grand total (میزان کل رقبہ / میزان رقبہ / کل رقبہ)
    m_total = re.search(
        r"(?:میزان\s*کل\s*رقبہ|میزان\s*رقبہ|کل\s*رقبہ)\s*[:/]?\s*([0-9]+(?:\.[0-9]+)?)\s*کنال\s*(?:معہ\s*)?([0-9]+(?:\.[0-9]+)?)\s*مرلہ",
        norm
    )
    if m_total:
        total_kanals = float(m_total.group(1))
        total_marlas = float(m_total.group(2))
    elif parcel_matches:
        total_kanals = sum(p["kanals"] for p in parcels)
        total_marlas = sum(p["marlas"] for p in parcels)
    else:
        km_matches = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*کنال\s*(?:معہ\s*)?([0-9]+(?:\.[0-9]+)?)\s*مرلہ", norm)
        if km_matches:
            for k, m in km_matches:
                total_kanals += float(k)
                total_marlas += float(m)
        else:
            k_single = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*کنال", norm)
            m_single = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*مرلہ", norm)
            s_single = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*سرسائی", norm)

            if k_single:
                total_kanals = sum(float(x) for x in k_single[:2])
            if m_single:
                total_marlas = sum(float(x) for x in m_single[:2])
            if s_single:
                total_sersai = sum(float(x) for x in s_single[:2])

    conversions = convert_land_area(kanals=total_kanals, marlas=total_marlas, sersai=total_sersai)
    return {
        "parsed_units": {
            "kanals": total_kanals,
            "marlas": total_marlas,
            "sersai": total_sersai
        },
        "parcels": parcels,
        "conversions": conversions
    }

def extract_soil_classifications(text: str) -> List[Dict[str, str]]:
    """Detects agricultural soil and irrigation types present in the record."""
    detected = []
    classes = [
        ("abi_awal", "آبی اول", "First-Class Perennially Irrigated"),
        ("abi_doyum", "آبی دوئم", "Second-Class Seasonally Irrigated"),
        ("abi", "آبی", "Irrigated Land"),
        ("khushki", "خشکی", "Dry Rain-fed Land (Barani)"),
        ("chahi", "چاہی", "Well-Irrigated Land"),
        ("nehri", "نہری", "Canal-Irrigated Land"),
        ("sailabi", "سیلابی", "Flood-Moistened Inundation Land"),
        ("banjar_qadeem", "بنجر قدیم", "Old Fallow Land (Over 8 seasons)"),
        ("banjar_jadeed", "بنجر جدید", "New Fallow Land (4-7 seasons)"),
        ("gair_mumkin", "غیر ممکن", "Uncultivable / Barren Land"),
        ("karewa", "کریوہ", "Karewa Lacustrine Plateau (Wudur)"),
        ("bagh", "باغ", "Horticultural Orchard (Apple/Walnut/Almond)"),
        ("zafran_zamin", "زعفران", "Saffron Land (Pampore Terrace)")
    ]

    for key, urdu_match, en_label in classes:
        if re.search(urdu_match, text):
            detected.append({
                "key": key,
                "urdu": urdu_match,
                "english": en_label
            })
    return detected

def extract_dates_and_calendars(text: str) -> Dict[str, Any]:
    """Extracts Fasli, Samvat/Bikrami, and Gregorian years from record."""
    norm = normalize_digits(text)
    dates_found = {
        "fasli_year": None,
        "samvat_year": None,
        "gregorian_year": None,
        "details": []
    }

    m_fasli = re.search(r"(?:سنہ\s*)?([0-9]{4})\s*فصلی", norm)
    if m_fasli:
        f_yr = int(m_fasli.group(1))
        dates_found["fasli_year"] = f_yr
        greg_est = f_yr + 593
        dates_found["details"].append(f"Fasli Year {f_yr} (~{greg_est} A.D.)")

    m_samvat = re.search(r"(?:سنہ\s*)?([0-9]{4})\s*(?:سمبت|بکرمی)", norm)
    if m_samvat:
        s_yr = int(m_samvat.group(1))
        dates_found["samvat_year"] = s_yr
        greg_est_samvat = s_yr - 57
        dates_found["details"].append(f"Samvat Year {s_yr} (~{greg_est_samvat} A.D.)")

    m_greg = re.search(r"([0-9]{4})\s*(?:ء|عیسوی|AD|A\.D\.)", norm)
    if m_greg:
        dates_found["gregorian_year"] = int(m_greg.group(1))
        dates_found["details"].append(f"Gregorian Year {m_greg.group(1)} A.D.")

    return dates_found

def extract_financial_consideration(text: str) -> Dict[str, Any]:
    """Extracts monetary consideration, sale price, or mortgage amounts."""
    norm = normalize_digits(text)
    financials = {
        "amount_rupees": None,
        "annas": 0,
        "paisas": 0,
        "text_detected": None
    }

    m_mabligh = re.search(r"مبلغ\s*([0-9]+)\s*روپیہ", norm)
    if m_mabligh:
        financials["amount_rupees"] = int(m_mabligh.group(1))
        financials["text_detected"] = f"Rs. {m_mabligh.group(1)}"

    m_annas = re.search(r"([0-9]+)\s*آنہ", norm)
    if m_annas:
        financials["annas"] = int(m_annas.group(1))

    m_paisas = re.search(r"([0-9]+)\s*پیسہ", norm)
    if m_paisas:
        financials["paisas"] = int(m_paisas.group(1))

    return financials

def detect_shikasta_formulas(text: str) -> List[Dict[str, Any]]:
    """Detects and decodes historical scribal and court abbreviations."""
    detected = []
    shikasta_keys = list_shikasta_abbreviations()

    for k in shikasta_keys:
        info = lookup_shikasta_abbreviation(k)
        if not info:
            continue
        arabic = info.get("arabic", "")
        if arabic and arabic in text:
            detected.append({
                "key": k,
                "formula": arabic,
                "transliteration": info.get("transliteration", ""),
                "meaning_en": info.get("meaning_en", ""),
                "context": info.get("context", "")
            })

    if "فقط" in text and not any(d["key"] == "faqat" for d in detected):
        detected.append({
            "key": "faqat",
            "formula": "فقط",
            "transliteration": "Faqat",
            "meaning_en": "End of Document / Concluded",
            "context": "Traditional concluding scribal stroke."
        })

    return detected

def extract_parties_and_roles(text: str) -> Dict[str, Any]:
    """Extracts parties, signatories, and witnesses."""
    parties = {
        "first_party": [],
        "second_party": [],
        "witnesses": [],
        "officials": []
    }

    witness_matches = re.findall(r"گواہ\s*شد\s*[:/]?\s*([^\r\n۔,]+)", text)
    for w in witness_matches:
        parties["witnesses"].append(w.strip())

    if re.search(r"پٹواری", text):
        parties["officials"].append("Patwari (Village Land Registrar)")
    if re.search(r"گرداور|قانونگو", text):
        parties["officials"].append("Girdawar / Qanoongo (Revenue Inspector)")
    if re.search(r"نائب\s*تحصیلدار", text):
        parties["officials"].append("Naib Tehsildar (Assistant Collector 2nd Grade)")
    elif re.search(r"تحصیلدار", text):
        parties["officials"].append("Tehsildar (Assistant Collector 1st Grade)")

    m_manka = re.search(r"منکہ\s*([^\r\n،,]+)", text)
    if m_manka:
        parties["first_party"].append(m_manka.group(1).strip())

    m_malik = re.search(r"نام\s*مالک[^\r\n:]*:\s*([^\r\n]+)", text)
    if m_malik:
        parties["first_party"].append(m_malik.group(1).strip())

    m_kasht = re.search(r"نام\s*کاشتکار[^\r\n:]*:\s*([^\r\n]+)", text)
    if m_kasht:
        parties["second_party"].append(m_kasht.group(1).strip())

    m_mushtari = re.search(r"(?:بحق\s*خریدار|خریدار)\s*([^\r\n،,]+)", text)
    if m_mushtari:
        parties["second_party"].append(m_mushtari.group(1).strip())

    m_murtahin = re.search(r"بحق\s*مرتہن\s*([^\r\n،,]+)", text)
    if m_murtahin:
        parties["second_party"].append(m_murtahin.group(1).strip())

    return parties

def extract_all_entities(text: str) -> Dict[str, Any]:
    """Master entity extractor combining all modules."""
    return {
        "classification": classify_document(text),
        "jurisdiction": extract_administrative_jurisdiction(text),
        "survey": extract_survey_identifiers(text),
        "measurements": extract_land_measurements(text),
        "soils": extract_soil_classifications(text),
        "dates": extract_dates_and_calendars(text),
        "financials": extract_financial_consideration(text),
        "formulas": detect_shikasta_formulas(text),
        "parties": extract_parties_and_roles(text)
    }