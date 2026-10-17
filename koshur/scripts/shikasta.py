"""
Khat-i-Shikast (خطِ شکستہ) Palaeography, Decipherment & Orthography Engine:
Computational reference for reading, analyzing, and transcribing historical cursive
Shikasta calligraphy used across Jammu & Kashmir and Northern Indian administrative,
judicial, revenue, and epistolary records.

Sources:
- 'A Text-Book of Khat-i-Shikast or Maktoobat-i-Akhgar' (Mohammad Tahir Faruqi & Sayed Tawakkul Husain Rizvi)
- 'Majmua Khat-i-Shikast: Kaghazat-i-Karrawai' (Maulvi Mohammad Ashfaq Siddiqi, Board of High School & Intermediate Education UP)
- J&K Revenue Department Historical Archives & Patwari Manual
"""

from typing import Dict, Any, List, Optional
from datetime import date

# ---------------------------------------------------------------------------
# 1. SHIKASTA ORTHOGRAPHIC RULES & LETTER LIGATURES
# ---------------------------------------------------------------------------

SHIKASTA_RULES: Dict[str, Dict[str, Any]] = {
    "alif": {
        "letter": "ا (Alif)",
        "standard_rule": "In standard Nasta'liq, Alif never joins to subsequent letters on the left.",
        "shikasta_rule": "In Shikasta, Alif frequently connects continuously to following letters even at the beginning of words to maintain fluid speed without lifting the pen.",
        "examples": [
            {"word": "اکبر", "meaning": "Akbar", "note": "Alif joins directly into Kaaf"},
            {"word": "آباد", "meaning": "Abad (Inhabited / Town)", "note": "Madd/Alif sweeps into Be"},
            {"word": "آج", "meaning": "Aaj (Today)", "note": "Alif links smoothly into Jeem"},
            {"word": "ادا", "meaning": "Ada (Payment / Performance)", "note": "Alif links into Dal"},
            {"word": "ابتدا", "meaning": "Ibtida (Commencement)", "note": "Alif links into Be"}
        ],
        "subsequent_rule": "When Alif follows Dal or Re, standard Nasta'liq writes it disconnected; in Shikasta it is merged directly into Dal/Re (e.g. بوجا، بوڑا، ذاتا)."
    },
    "be_series": {
        "letter": "ب، پ، ت، ٹ، ث، ن، ی (Be, Pe, Te, Tte, Se, Noon, Ye)",
        "standard_rule": "Written with distinct initial teeth (dandana) and full dots (nuqtas).",
        "shikasta_rule": "Can appear in three distinct cursive forms: (1) an erect vertical notch at the beginning whose identity relies entirely on nuqtas (بست، پست، تست); (2) a flattened, minute wave where dots are rapidly combined or reduced to dashes (بیدار، پرورش، ترمیم); (3) terminal forms elongated into sweeping horizontal baselines.",
        "examples": [
            {"word": "بست", "meaning": "Tied / Closed"},
            {"word": "پست", "meaning": "Low / Depressed"},
            {"word": "ترمیم", "meaning": "Amendment / Revision (revenue/law)"},
            {"word": "ثبوت", "meaning": "Evidence / Proof"},
            {"word": "نقل", "meaning": "Copy / Extract (e.g. Naql Jamabandi)"}
        ]
    },
    "jeem_series": {
        "letter": "ج، چ، ح، خ (Jeem, Che, He, Khe)",
        "standard_rule": "Formed with a sharp triangular crest and distinct semi-circular descent.",
        "shikasta_rule": "Represented by fluid rounded loops (huroof-i-mudawwar). At the start of words, the head is rounded into an oval without a distinct break; in medial positions, the head merges into a continuous loop; at the end, the tail is either rounded or flicked horizontally.",
        "examples": [
            {"word": "جرم", "meaning": "Offence / Crime"},
            {"word": "چراغ", "meaning": "Lamp"},
            {"word": "حساب", "meaning": "Account / Calculation"},
            {"word": "خراب", "meaning": "Damaged / Waste land"},
            {"word": "مجبور", "meaning": "Compelled / Helpless"},
            {"word": "سخاوت", "meaning": "Generosity"}
        ]
    },
    "dal_series": {
        "letter": "د، ڈ، ذ (Dal, Daal, Zal)",
        "standard_rule": "Non-connector letters that never join to the following letter on the left.",
        "shikasta_rule": "In Shikasta, Dal/Zal connect seamlessly from the right and often merge directly with subsequent letters like Alif, Laam, or Re without pen elevation (e.g., دادا، ذاکر). When Dal occurs medially, it resembles a tiny upward hook or terminal Re.",
        "examples": [
            {"word": "دل", "meaning": "Heart"},
            {"word": "دماغ", "meaning": "Mind"},
            {"word": "دادا", "meaning": "Grandfather"},
            {"word": "رسید", "meaning": "Receipt (Dal connects continuously from Ye)"},
            {"word": "لذت", "meaning": "Pleasure / Taste"}
        ]
    },
    "re_series": {
        "letter": "ر، ڑ، ز، ژ (Re, Rre, Ze, Zhe)",
        "standard_rule": "Non-connectors, written as distinct angled strokes on the baseline.",
        "shikasta_rule": "Can connect rightwards and leftwards in fast hand. Initial Re is written as an abbreviated diagonal dash; medial and terminal Re are often drawn as long graceful downward descending strokes without lift.",
        "examples": [
            {"word": "راز", "meaning": "Secret"},
            {"word": "زار", "meaning": "Wretched / Garden"},
            {"word": "شریر", "meaning": "Mischievous / Malicious"},
            {"word": "سزا", "meaning": "Punishment"},
            {"word": "پژمردہ", "meaning": "Withered"}
        ]
    },
    "seen_sheen": {
        "letter": "س، ش (Seen, Sheen)",
        "standard_rule": "Written with three distinct notched teeth (dandaane).",
        "shikasta_rule": "Crucial hallmark of Shikasta: the three teeth are completely eliminated and replaced by a smooth, uninterrupted horizontal or slanting kashish (unspooled sweep). Nuqtas of Sheen are often reduced to a single line or triangular flick.",
        "examples": [
            {"word": "سحاب", "meaning": "Cloud"},
            {"word": "سرخاب", "meaning": "Ruddy shelduck"},
            {"word": "شتاب", "meaning": "Haste / Swiftly"},
            {"word": "بساط", "meaning": "Capacity / Chessboard"},
            {"word": "بسیار", "meaning": "Numerous / Abundant"},
            {"word": "آتش", "meaning": "Fire"}
        ]
    },
    "swad_zwad": {
        "letter": "ص، ض (Swad, Zwad)",
        "standard_rule": "Requires a looped head followed by a small characteristic tooth (dandana).",
        "shikasta_rule": "The tooth is omitted; the loop is compressed into an elliptical knot flowing directly into the next letter.",
        "examples": [
            {"word": "صبح", "meaning": "Morning"},
            {"word": "صبر", "meaning": "Patience"},
            {"word": "حاضر", "meaning": "Present (in court)"},
            {"word": "قبضہ", "meaning": "Possession / Tenure (revenue)"}
        ]
    },
    "toye_zoye": {
        "letter": "ط، ظ (Toye, Zoye)",
        "standard_rule": "Composed of a straight vertical Alif stroke connected to a rounded base.",
        "shikasta_rule": "The vertical stroke is tilted forward and blends directly into the base loop in a single rapid pen gesture.",
        "examples": [
            {"word": "طالب", "meaning": "Seeker / Student"},
            {"word": "ظاہر", "meaning": "Evident / Apparent"},
            {"word": "خط", "meaning": "Letter / Boundary line"},
            {"word": "شرط", "meaning": "Condition / Covenant"}
        ]
    },
    "ain_ghain": {
        "letter": "ع، غ (Ain, Ghain)",
        "standard_rule": "Initial Ain has an open crescent beak; medial Ain is a closed inverted triangle.",
        "shikasta_rule": "Initial Ain is rounded into a closed loop or soft hook; medial Ain is drawn as a tiny closed circle or flat knot; final Ain sweeps into a broad loop.",
        "examples": [
            {"word": "عدالت", "meaning": "Court of Law"},
            {"word": "عرضی", "meaning": "Petition / Plaint"},
            {"word": "دعویٰ", "meaning": "Lawsuit / Claim"},
            {"word": "مبیعہ", "meaning": "Sold property"}
        ]
    },
    "kaaf_gaaf": {
        "letter": "ک، گ (Kaaf, Gaaf)",
        "standard_rule": "Composed of a vertical stem, horizontal base, and distinct upper markaz bar.",
        "shikasta_rule": "The markaz bar and base loop are drawn in one continuous cursive circular stroke. In initial and medial positions, Kaaf resembles an open lasso or oval flowing immediately into the following consonant.",
        "examples": [
            {"word": "کامل", "meaning": "Complete / Competent"},
            {"word": "کاتب", "meaning": "Scribe / Clerk"},
            {"word": "گلاب", "meaning": "Rose"},
            {"word": "مکمل", "meaning": "Completed"},
            {"word": "کاشتکار", "meaning": "Cultivator / Tenant farmer"}
        ]
    },
    "laam": {
        "letter": "ل (Laam)",
        "standard_rule": "Long vertical ascent followed by lower semi-circular bowl.",
        "shikasta_rule": "Initial and medial Laam merge directly with the next letter with a shortened vertical; terminal Laam flattens into an extended bottom sweep.",
        "examples": [
            {"word": "لطف", "meaning": "Kindness / Delight"},
            {"word": "لذیذ", "meaning": "Delicious"},
            {"word": "گلستان", "meaning": "Flower garden"},
            {"word": "جاہل", "meaning": "Ignorant / Illiterate"}
        ]
    },
    "meem": {
        "letter": "م (Meem)",
        "standard_rule": "Small round head with a descending vertical tail.",
        "shikasta_rule": "Contracted into a tiny compact dot or downward slash. In rapid revenue scripts, medial Meem is virtually a flat bump on the ligature string.",
        "examples": [
            {"word": "معمول", "meaning": "Customary / Habitual"},
            {"word": "مجہول", "meaning": "Unknown / Obscure"},
            {"word": "تمیز", "meaning": "Discernment"},
            {"word": "قدیم", "meaning": "Ancient / Long-standing (e.g. Banjar Qadeem)"}
        ]
    },
    "chhoti_he": {
        "letter": "ہ (Chhoti He)",
        "standard_rule": "Hook or round eye shape.",
        "shikasta_rule": "Appears in multiple rapid variants: (1) suspended hook below the consonant (ہمدم، ہموطن); (2) medial downward loop (انتہا، تہذیب، اشتہار); (3) terminal Alif-like upward stroke when vocalized as 'a' (مرتبہ، درجہ، ہرجہ، خرچہ); (4) terminal downward curl (پناہ، رفاہ، نگاہ).",
        "examples": [
            {"word": "ہمدم", "meaning": "Companion"},
            {"word": "اشتہار", "meaning": "Public Notice / Proclamation"},
            {"word": "درجہ", "meaning": "Grade / Category"},
            {"word": "خرچہ", "meaning": "Expenses / Costs"}
        ]
    },
    "do_chashmi_he": {
        "letter": "ھ (Do-chashmi He / Aspirated marker)",
        "standard_rule": "Two distinct circular eyes (butterfly loop).",
        "shikasta_rule": "Compressed into a single flattened wavy oval or elongated loop across the baseline.",
        "examples": [
            {"word": "جھانجھ", "meaning": "Cymbal / Clamour"},
            {"word": "بانجھ", "meaning": "Barren"},
            {"word": "متھرا", "meaning": "Mathura"},
            {"word": "جھانسی", "meaning": "Jhansi"}
        ]
    },
    "ye": {
        "letter": "ی، ے (Chhoti Ye / Badi Ye)",
        "standard_rule": "Distinct round bowl for Chhoti Ye (ī), and long flat return stroke for Badi Ye (ē).",
        "shikasta_rule": "Terminal Ye often contracts into a quick backward loop or straight downward flick. In classical words written with Alif Maqsoora (عیسیٰ، موسیٰ، مصطفےٰ، اعلیٰ، ادنیٰ), the dagger alif is integrated directly into the cursive terminal crest.",
        "examples": [
            {"word": "اعلیٰ", "meaning": "Superior / Higher"},
            {"word": "ادنیٰ", "meaning": "Inferior / Lower"},
            {"word": "مصطفیٰ", "meaning": "Mustafa"},
            {"word": "عدالتی", "meaning": "Judicial / Pertaining to court"}
        ]
    }
}

# ---------------------------------------------------------------------------
# 2. SHIKASTA SCRIBAL FORMULAS & EPIGRAPHIC ABBREVIATIONS
# ---------------------------------------------------------------------------

SHIKASTA_ABBREVIATIONS: Dict[str, Dict[str, Any]] = {
    "al_abd": {
        "arabic": "العبد",
        "transliteration": "Al-'Abd",
        "meaning_en": "The Servant / Signatory / Executant",
        "usage": "Written at the top of the signatory slot above the person's signature or seal in legal and revenue deeds.",
        "context": "Found in Bainama, Tamassuk, Rehnnama, and judicial confessions."
    },
    "marqooma": {
        "arabic": "مرقومہ",
        "transliteration": "Marqooma",
        "meaning_en": "Recorded on / Dated",
        "usage": "Prefix introducing the calendar date, month, and year of execution at the foot of deeds.",
        "context": "e.g., 'مرقومہ ۲۵ ماہِ اگست سنہ ۱۹۱۲ عیسوی'"
    },
    "faqat": {
        "arabic": "فقط",
        "transliteration": "Faqat",
        "meaning_en": "Finis / Only / Thus ends",
        "usage": "Affixed at the absolute end of the deed or register entry to prevent fraudulent additions.",
        "context": "Universal concluding mark in Patwari registers and court depositions."
    },
    "manka": {
        "arabic": "منکہ",
        "transliteration": "Manka",
        "meaning_en": "Whereas I / The undersigned",
        "usage": "Standard legal opening recital of deeds identifying the first-person executant.",
        "context": "e.g., 'منکہ رام چندر ولد گوپی ناتھ ساکن سرینگر...'"
    },
    "dastkhat": {
        "arabic": "دستخط",
        "transliteration": "Dastkhat",
        "meaning_en": "Signature",
        "usage": "Indicates the formal signing by a party or revenue official.",
        "context": "Official execution marker."
    },
    "gawah_shud": {
        "arabic": "گواہ شد",
        "transliteration": "Gawah Shud",
        "meaning_en": "Witnessed / Attested",
        "usage": "Written above each attesting witness's signature on conveyance deeds, mortgages, and bonds.",
        "context": "Minimum two witnesses required on registered instruments."
    },
    "naql_mutabiq_asl": {
        "arabic": "نقل مطابق اصل",
        "transliteration": "Naql Mutabiq Asl",
        "meaning_en": "Certified True Copy",
        "usage": "Official certification stamp on Fard Jamabandi, Khasra extracts, or court decrees.",
        "context": "Affixed by the Tehsildar, Naib Tehsildar, or Sadar Qanungo."
    },
    "algoothi_ba_qalam_khud": {
        "arabic": "الگوتھی بقلم خود",
        "transliteration": "Algoothi ba-qalam-i-khud",
        "meaning_en": "Thumb impression affixed by executant's own hand",
        "usage": "Recorded beside the left thumb impression of an illiterate executant.",
        "context": "Standard authentication in land sale and mortgaging records."
    },
    "ba_half": {
        "arabic": "بحلف",
        "transliteration": "Ba-half",
        "meaning_en": "On solemn oath / Sworn",
        "usage": "Prefix heading formal witness depositions and revenue affidavits.",
        "context": "Used in revenue inquiries and judicial trials."
    },
    "aizan": {
        "arabic": "ایضاً",
        "transliteration": "Aizan",
        "meaning_en": "Ditto / As above / Likewise",
        "usage": "Scribal abbreviation used in tabular Khasra and Khatauni columns to avoid repeating names.",
        "context": "Extensively used across Patwari land registers."
    },
    "al_mutawaffi": {
        "arabic": "المتوفی",
        "transliteration": "Al-Mutawaffi",
        "meaning_en": "The deceased / Late",
        "usage": "Inserted after the name of a deceased landholder during Intiqal (mutation of inheritance).",
        "context": "e.g., 'غلام رسول المتوفی'"
    },
    "juzwan_o_kullan": {
        "arabic": "جزو کلاً",
        "transliteration": "Juzwan o Kullan",
        "meaning_en": "In part and in full / Entirely",
        "usage": "Conveyance term assuring transfer of all title, rights, and appurtenances without reservation.",
        "context": "Found in Bainama (sale deed) and Hibanama (gift deed)."
    },
    "manqoola_o_ghair_manqoola": {
        "arabic": "منقولہ و غیر منقولہ",
        "transliteration": "Manqoola o Ghair-manqoola",
        "meaning_en": "Movable and immovable property",
        "usage": "Legal formula defining all assets mortgaged, gifted, or partitioned.",
        "context": "Universal asset scope in deeds."
    },
    "sikka_raij_ul_waqt": {
        "arabic": "سکہ رائج الوقت",
        "transliteration": "Sikka Raij-ul-Waqt",
        "meaning_en": "Current legal tender / Current coin of the realm",
        "usage": "Denotes valid official currency in cash sales, mortgages, or loans.",
        "context": "Used in Tamassuk and Bainama clauses."
    },
    "bila_uzr_o_heela": {
        "arabic": "بلا عذر و حیلہ",
        "transliteration": "Bila Uzr o Heela",
        "meaning_en": "Without pretext, objection, or evasion",
        "usage": "Unconditional covenant undertaken by a debtor or seller.",
        "context": "Core promissory language in debt bonds and rent agreements."
    },
    "hashiya": {
        "arabic": "حاشیہ",
        "transliteration": "Hashiya",
        "meaning_en": "Marginal note / Endorsement in the margin",
        "usage": "Additions, corrections, or field notes entered along the margins of Patwari maps and registers.",
        "context": "Used for boundary corrections and mutation references."
    }
}

# ---------------------------------------------------------------------------
# 3. RAQOOM & SIYAQ TRADITIONAL FINANCIAL NOTATIONS
# ---------------------------------------------------------------------------

# Traditional Indian & J&K Currency Subdivisions:
# 1 Rupee (روپیہ) = 16 Annas (آنہ)
# 1 Anna = 4 Paisas (پیسہ)
# 1 Paisa = 3 Pais (پائی)
# Total: 1 Rupee = 64 Paisas = 192 Pais

RAQOOM_CURRENCY: Dict[str, Dict[str, Any]] = {
    "1_anna": {"symbol": "۔/", "name": "Yak Aana", "fraction_rupee": 1 / 16, "paisas": 4},
    "2_annas": {"symbol": "=/ ", "name": "Do Aana", "fraction_rupee": 2 / 16, "paisas": 8},
    "3_annas": {"symbol": "≡/ ", "name": "Seh Aana", "fraction_rupee": 3 / 16, "paisas": 12},
    "4_annas": {"symbol": "۱/ ", "name": "Chow Aana (Chavanni / Pao Rupee)", "fraction_rupee": 4 / 16, "paisas": 16},
    "8_annas": {"symbol": "۲/ ", "name": "Aath Aana (Athanni / Adheli)", "fraction_rupee": 8 / 16, "paisas": 32},
    "12_annas": {"symbol": "۳/ ", "name": "Baarah Aana (Paun Rupee)", "fraction_rupee": 12 / 16, "paisas": 48},
    "16_annas": {"symbol": "۱//", "name": "Yak Rupaya (Full Rupee)", "fraction_rupee": 1.0, "paisas": 64},
}

# ---------------------------------------------------------------------------
# 4. TRADITIONAL WEIGHTS & MEASURES (اوزانِ ہند و کشمیر)
# ---------------------------------------------------------------------------

# Hierarchy:
# 1 Ratti = 0.1215 grams
# 1 Masha = 8 Ratti = 0.972 grams
# 1 Tola = 12 Masha = 11.664 grams
# 1 Chhatank = 5 Tolas = 58.32 grams
# 1 Pao = 4 Chhatanks = 20 Tolas = 233.28 grams
# 1 Ser = 4 Pao = 16 Chhatanks = 80 Tolas = 933.12 grams (approx 0.933 kg)
# 1 Maund (Man) = 40 Sers = 37.3248 kg
#
# Kashmiri Traditional Agricultural Measure:
# 1 Trak = 6 Kashmiri Seers = approx 5 kg
# 1 Kharwar (Khirwar / Ass-load) = 16 Trak = approx 80 kg unhusked paddy (shali)

GRAMS_PER_RATTI = 0.1215
GRAMS_PER_MASHA = 0.972
GRAMS_PER_TOLA = 11.664
GRAMS_PER_CHHATANK = 58.32
GRAMS_PER_PAO = 233.28
GRAMS_PER_SER = 933.12
GRAMS_PER_MAUND = 37324.8

KG_PER_KASHMIRI_TRAK = 5.0
KG_PER_KASHMIRI_KHARWAR = 80.0


def convert_traditional_weight(
    maunds: float = 0.0,
    sers: float = 0.0,
    chhatanks: float = 0.0,
    tolas: float = 0.0
) -> Dict[str, Any]:
    """
    Converts historical Indian/Kashmiri weights into metric (kg, grams) and imperial (lbs),
    along with traditional Kashmiri paddy measures (Trak and Kharwar).
    """
    total_grams = (
        (maunds * GRAMS_PER_MAUND)
        + (sers * GRAMS_PER_SER)
        + (chhatanks * GRAMS_PER_CHHATANK)
        + (tolas * GRAMS_PER_TOLA)
    )
    total_kg = total_grams / 1000.0
    total_lbs = total_kg * 2.20462
    kashmiri_traks = total_kg / KG_PER_KASHMIRI_TRAK
    kashmiri_kharwar = total_kg / KG_PER_KASHMIRI_KHARWAR

    return {
        "input": {
            "maunds": maunds,
            "sers": sers,
            "chhatanks": chhatanks,
            "tolas": tolas,
        },
        "total_grams": round(total_grams, 2),
        "total_kg": round(total_kg, 3),
        "total_lbs": round(total_lbs, 3),
        "kashmiri_traks": round(kashmiri_traks, 2),
        "kashmiri_kharwar": round(kashmiri_kharwar, 3),
    }


def format_traditional_currency(
    rupees: int = 0,
    annas: int = 0,
    paisas: int = 0
) -> Dict[str, Any]:
    """
    Normalizes and formats traditional Indian/J&K currency (Rupees, Annas, Paisas).
    Returns total decimal rupees, standard breakdown, and written Urdu representation.
    """
    # Normalize paisas to annas
    extra_annas, norm_paisas = divmod(paisas, 4)
    total_annas = annas + extra_annas
    extra_rupees, norm_annas = divmod(total_annas, 16)
    total_rupees = rupees + extra_rupees

    decimal_rupees = total_rupees + (norm_annas / 16.0) + (norm_paisas / 64.0)

    # Build Urdu wording
    parts = []
    if total_rupees:
        parts.append(f"{total_rupees} روپیہ")
    if norm_annas:
        parts.append(f"{norm_annas} آنہ")
    if norm_paisas:
        parts.append(f"{norm_paisas} پیسہ")
    urdu_text = " ".join(parts) if parts else "صفر روپیہ"

    return {
        "rupees": total_rupees,
        "annas": norm_annas,
        "paisas": norm_paisas,
        "decimal_rupees": round(decimal_rupees, 4),
        "urdu_text": urdu_text,
    }


# ---------------------------------------------------------------------------
# 5. REVENUE ERAS & CALENDARS (سالوں کا حساب)
# ---------------------------------------------------------------------------

def calculate_fasli_year(gregorian_dt: Optional[date] = None) -> Dict[str, Any]:
    """
    Calculates the Fasli Year (سالِ فصلی) used in J&K land revenue records.
    The Fasli agricultural year starts on October 1st and ends on September 30th.
    Historically, Fasli Year = Gregorian Year - 592 (or -593 if before October 1).
    """
    if gregorian_dt is None:
        gregorian_dt = date.today()

    yr = gregorian_dt.year
    if gregorian_dt.month >= 10:
        fasli_yr = yr - 592
        start_date = f"{yr}-10-01"
        end_date = f"{yr + 1}-09-30"
    else:
        fasli_yr = yr - 593
        start_date = f"{yr - 1}-10-01"
        end_date = f"{yr}-09-30"

    samvat_yr = yr + 57  # Vikrami Samvat approximation

    return {
        "gregorian_date": gregorian_dt.isoformat(),
        "fasli_year": fasli_yr,
        "fasli_year_urdu": f"سنہ {fasli_yr} فصلی",
        "fasli_period": f"{start_date} to {end_date}",
        "samvat_year": samvat_yr,
        "samvat_year_urdu": f"سنہ {samvat_yr} سمبت (بکرمی)",
        "explanation": (
            "The Fasli Era (سالِ فصلی) is the statutory revenue and crop accounting year "
            "originating from Emperor Akbar and preserved across Jammu & Kashmir Patwari registers. "
            "All Girdawari and Jamabandi quadrennial cycles are anchored to this agricultural calendar."
        ),
    }


# ---------------------------------------------------------------------------
# 6. PUBLIC API & LOOKUP HELPERS
# ---------------------------------------------------------------------------

def explain_shikasta_rule(letter_or_series: str) -> Optional[Dict[str, Any]]:
    """Look up the Shikasta writing and ligature rule for a letter or series."""
    key = letter_or_series.lower().strip().replace(" ", "_")
    if key in SHIKASTA_RULES:
        return SHIKASTA_RULES[key]
    for k, v in SHIKASTA_RULES.items():
        if key in k or key in v["letter"].lower():
            return v
    return None


def list_shikasta_rules() -> List[str]:
    """Return all letter rules cataloged in the Shikasta palaeography engine."""
    return list(SHIKASTA_RULES.keys())


def lookup_shikasta_abbreviation(term: str) -> Optional[Dict[str, Any]]:
    """Look up a Shikasta epigraphic scribal formula or legal abbreviation."""
    key = term.lower().strip().replace(" ", "_").replace("'", "")
    if key in SHIKASTA_ABBREVIATIONS:
        return SHIKASTA_ABBREVIATIONS[key]
    for k, v in SHIKASTA_ABBREVIATIONS.items():
        if (
            term in v["arabic"]
            or term.lower() in v["transliteration"].lower()
            or term.lower() in v["meaning_en"].lower()
        ):
            return v
    return None


def list_shikasta_abbreviations() -> List[str]:
    """Return all cataloged scribal formulas and abbreviations."""
    return list(SHIKASTA_ABBREVIATIONS.keys())
