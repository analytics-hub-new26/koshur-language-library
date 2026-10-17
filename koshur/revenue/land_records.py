"""
Jammu & Kashmir Revenue Records & Land Governance Lexicon:
A complete computational reference for deciphering, preserving, and converting
historical and official land revenue terms used across Jammu & Kashmir
(Patwari registers, Jamabandi, Khasra, Intiqal, Shikasta dastavezat, and traditional land measurements).

Sources:
- J&K Revenue Department Land Records Manual & SRO Regulations
- 'Majmua Khat-i-Shikast: Kaghazat-i-Karrawai' (Maulvi Mohammad Ashfaq Siddiqi)
- Imperial Gazetteer of India: Provincial Series (Kashmir & Jammu)
"""

from typing import Dict, Any, List, Optional

# Traditional J&K Land Area Equivalents
# 1 Karam = 5.5 ft
# 1 Sersai = 1 Karam x 1 Karam = 30.25 sq ft
# 1 Marla = 9 Sersai = 272.25 sq ft
# 1 Kanal = 20 Marlas = 5,445 sq ft
# 1 Ghumaon (Acre) = 8 Kanals = 43,560 sq ft
SQ_FEET_PER_MARLA = 272.25
SQ_FEET_PER_KANAL = 5445.0
SQ_FEET_PER_GHUMAON = 43560.0
SQ_METERS_PER_SQ_FOOT = 0.092903

REVENUE_TERMS: Dict[str, Dict[str, Any]] = {
    # -----------------------------------------------------------------------
    # 1. CORE REGISTERS & MAPS
    # -----------------------------------------------------------------------
    "jamabandi": {
        "term_urdu": "جمع بندی",
        "term_dev": "जमाबंदी",
        "meaning_en": "Record of Rights (ROR) containing complete details of land owners, cultivators, area, and revenue assessments.",
        "meaning_hi": "अधिकार अभिलेख (रकबा, मालिकाना हक और लगान का मुख्य रजिस्टर)",
        "frequency": "Revised every 4 or 5 years in Jammu & Kashmir.",
        "category": "Register"
    },
    "khasra": {
        "term_urdu": "خسرہ",
        "term_dev": "खसरा",
        "meaning_en": "A unique survey number assigned to a specific plot or parcel of land.",
        "meaning_hi": "भूखंड संख्या (सर्वेक्षण नंबर)",
        "category": "Survey"
    },
    "girdawari": {
        "term_urdu": "گرداوری",
        "term_dev": "गिरदावरी",
        "meaning_en": "Harvest inspection conducted bi-annually (Kharif and Rabi) by the Patwari to record crop cultivation and possession.",
        "meaning_hi": "फसल पड़ताल (खरीफ व रबी फसलों और काश्तकार के कब्जे का ब्यौरा)",
        "category": "Inspection"
    },
    "khasra_girdawari": {
        "term_urdu": "خسرہ گرداوری",
        "term_dev": "खसरा गिरदावरी",
        "meaning_en": "Harvest inspection register showing seasonal crops, tenure, changes in possession, and soil status.",
        "meaning_hi": "फसल गिरदावरी रजिस्टर",
        "category": "Register"
    },
    "shajra_kishtwar": {
        "term_urdu": "شجرہ کشتوار",
        "term_dev": "शजरा किश्तवार",
        "meaning_en": "The village cadastral field map showing field boundaries, khasra numbers, and geographical features.",
        "meaning_hi": "गाँव का भू-नक्शा (खेतों की सीमाएं व खसरा संख्या)",
        "category": "Map"
    },
    "shajra_nasab": {
        "term_urdu": "شجرہ نسب",
        "term_dev": "शजरा नसब",
        "meaning_en": "Genealogical / ancestral family tree of land-owning families showing lineage and hereditary shares.",
        "meaning_hi": "वंशावली (भूमि-स्वामियों का पारिवारिक वृक्ष)",
        "category": "Genealogy"
    },
    "intiqal": {
        "term_urdu": "انتقال",
        "term_dev": "इंतक़ाल",
        "meaning_en": "Mutation of land ownership resulting from sale, inheritance, gift, mortgage, or partition.",
        "meaning_hi": "दाखिल-खारिज / नामांतरण (स्वामित्व हस्तांतरण)",
        "category": "Transaction"
    },
    "fard": {
        "term_urdu": "فرد",
        "term_dev": "फ़र्द",
        "meaning_en": "Certified extract or copy of the Jamabandi indicating ownership, area, and cultivation rights.",
        "meaning_hi": "भूमि स्वामित्व का आधिकारिक उद्धरण",
        "category": "Document"
    },
    "latha": {
        "term_urdu": "لٹھہ",
        "term_dev": "लट्ठा",
        "meaning_en": "Field map traced onto starched tracing cloth carried by the Patwari during field inspections.",
        "meaning_hi": "कपड़े पर बना कार्यवाहक गाँव का नक्शा",
        "category": "Map"
    },
    "musavi": {
        "term_urdu": "مساوی",
        "term_dev": "मुसावी",
        "meaning_en": "The master original cadastral map preserved on heavy paper in the district revenue archives.",
        "meaning_hi": "मूल स्थायी भू-नक्शा (जिला अभिलेखागार में सुरक्षित)",
        "category": "Map"
    },
    "roznamcha_waqiati": {
        "term_urdu": "روزنامچہ واقعات",
        "term_dev": "रोज़नामचा वाक़ियाती",
        "meaning_en": "Patwari's daily diary recording official inspections, hail/rain damages, local disputes, and administrative events.",
        "meaning_hi": "पटवारी की दैनिक कार्य-डायरी",
        "category": "Diary"
    },
    "misal_haqiat": {
        "term_urdu": "مِسل حقیقت",
        "term_dev": "मिसल हक़ीक़त",
        "meaning_en": "Record of Rights prepared at the initial or regular land settlement (Bandobast).",
        "meaning_hi": "बंदोबस्त के समय तैयार किया गया मूल अधिकार अभिलेख",
        "category": "Settlement"
    },
    "wajib_ul_arz": {
        "term_urdu": "واجب العرض",
        "term_dev": "वाजिब-उल-अर्जी",
        "meaning_en": "Statement of village customs, irrigation rights, common land usage, and water distribution rules.",
        "meaning_hi": "ग्राम्य रीति-रिवाज व शामलात जमीन के अधिकारों का घोषणा-पत्र",
        "category": "Customs"
    },
    "lal_kitab": {
        "term_urdu": "لال کتاب",
        "term_dev": "लाल किताब",
        "meaning_en": "Village statistical notebook containing village-level data on crops, land revenue, cattle, and wells.",
        "meaning_hi": "ग्राम सांख्यिकी पुस्तिका (गाँव का सांख्यिकीय रजिस्टर)",
        "category": "Statistics"
    },
    "khewat": {
        "term_urdu": "کھیوٹ",
        "term_dev": "खेवट",
        "meaning_en": "Account number of owners in a revenue estate showing joint or individual proprietary holdings.",
        "meaning_hi": "मालिकों का खाता नंबर",
        "category": "Cadastral Index"
    },
    "khatoni": {
        "term_urdu": "کھتونی",
        "term_dev": "खतौनी",
        "meaning_en": "Account number of cultivators/tenants holding land under a specific Khewat owner.",
        "meaning_hi": "काश्तकारों का खाता नंबर",
        "category": "Cadastral Index"
    },
    "minjumla": {
        "term_urdu": "منجملہ",
        "term_dev": "मिंजुमला",
        "meaning_en": "Part of / extracted out of a parent survey plot (e.g., fractional holding within a larger Khasra).",
        "meaning_hi": "मूल खसरे में से हिस्सा / कुल में से",
        "category": "Survey"
    },
    "tatima": {
        "term_urdu": "تتمہ شجرہ",
        "term_dev": "ततीमा शजरा",
        "meaning_en": "Supplementary field map showing newly subdivided survey plots created by partition or sale.",
        "meaning_hi": "विभाजन के पश्चात बना पूरक नक्शा",
        "category": "Map"
    },
    "aks_shajra": {
        "term_urdu": "عکس شجرہ",
        "term_dev": "अक्स शजरा",
        "meaning_en": "Certified traced replica of a specific parcel's field boundary extracted from the village latha map.",
        "meaning_hi": "खेत की सीमा का प्रमाणित ट्रेस नक्शा",
        "category": "Map"
    },
    "nishan_dehi": {
        "term_urdu": "نشان دہی",
        "term_dev": "निशानदेही",
        "meaning_en": "On-site demarcation of field boundaries carried out by revenue officials using measuring chain/total station.",
        "meaning_hi": "मौके पर ज़मीन की सीमा का निर्धारण / पैमाइश",
        "category": "Survey"
    },
    "seh_hadda": {
        "term_urdu": "سہ حدہ",
        "term_dev": "सहहद्दा",
        "meaning_en": "Masonry stone or boundary pillar erected at the meeting point of three village boundaries.",
        "meaning_hi": "तीन गाँवों की सीमा का मिलन बिंदु (स्तंभ)",
        "category": "Survey"
    },
    "burj": {
        "term_urdu": "برج",
        "term_dev": "बुर्ज",
        "meaning_en": "Triangulation pillar or permanent cadastral boundary survey mark in a revenue estate.",
        "meaning_hi": "सर्वेक्षण बुर्ज / स्थायी सीमा निशान",
        "category": "Survey"
    },
    "dhal_bachh": {
        "term_urdu": "ڈھال باچھ",
        "term_dev": "ढाल बाछ",
        "meaning_en": "Statement of apportionment showing individual revenue demand payable by co-sharers.",
        "meaning_hi": "सह-स्वामियों में लगान के वितरण का रजिस्टर",
        "category": "Assessment"
    },
    "tauzi": {
        "term_urdu": "توضیح",
        "term_dev": "तौज़ीह",
        "meaning_en": "Monthly collection and demand ledger of land revenue maintained by the tehsil office.",
        "meaning_hi": "मासिक लगान वसूली एवं बकाया रजिस्टर",
        "category": "Register"
    },

    # -----------------------------------------------------------------------
    # 2. LAND TENURE & STATUS OF HOLDINGS
    # -----------------------------------------------------------------------
    "malik_ala": {
        "term_urdu": "مالک اعلیٰ",
        "term_dev": "मालिक आला",
        "meaning_en": "Superior proprietary landholder entitled to receive quit-rent (Haq Malikana) from the inferior owner.",
        "meaning_hi": "उच्च भू-स्वामी (सर्वोच्च मालिक)",
        "category": "Tenure"
    },
    "malik_adna": {
        "term_urdu": "مالک ادنیٰ",
        "term_dev": "मालिक अदना",
        "meaning_en": "Inferior proprietary landholder having full rights of occupation, sale, and inheritance subject to quit-rent.",
        "meaning_hi": "अधीनस्थ भू-स्वामी",
        "category": "Tenure"
    },
    "dakhilkar": {
        "term_urdu": "دخلکار",
        "term_dev": "दखलकार",
        "meaning_en": "Occupancy tenant with permanent, hereditary rights of cultivation protected by tenancy law (Maurusi).",
        "meaning_hi": "स्थायी / मौरूसी काश्तकार",
        "category": "Tenure"
    },
    "ghair_dakhilkar": {
        "term_urdu": "غیر دخلکار",
        "term_dev": "गैर दखलकार",
        "meaning_en": "Tenant-at-will cultivating land without hereditary rights, subject to annual lease renewal or ejectment.",
        "meaning_hi": "अस्थायी काश्तकार (इच्छानुसार काश्त)",
        "category": "Tenure"
    },
    "khudkasht": {
        "term_urdu": "خود کاشت",
        "term_dev": "खुदकाश्त",
        "meaning_en": "Land cultivated directly by the owner through their own labor, household, or hired servants.",
        "meaning_hi": "मालिक द्वारा स्वयं जोती जाने वाली भूमि",
        "category": "Cultivation Status"
    },
    "maqbooza": {
        "term_urdu": "مقبوضہ",
        "term_dev": "मक़बूज़ा",
        "meaning_en": "Land held under actual physical possession and operational occupation of a named person or institution.",
        "meaning_hi": "कब्ज़ाधीन भूमि",
        "category": "Cultivation Status"
    },
    "muzarra": {
        "term_urdu": "مزارع",
        "term_dev": "मुज़ारे",
        "meaning_en": "Agricultural cultivator / tenant farming land owned by another on lease or share.",
        "meaning_hi": "काश्तकार / किसान",
        "category": "Tenure"
    },
    "bataidar": {
        "term_urdu": "بٹائی دار",
        "term_dev": "बटाईदार",
        "meaning_en": "Sharecropping cultivator who pays land rent as a fixed proportion of the crop yield (Batai).",
        "meaning_hi": "बटाई पर खेती करने वाला किसान",
        "category": "Tenure"
    },
    "hissadar": {
        "term_urdu": "حصہ دار",
        "term_dev": "हिस्सेदार",
        "meaning_en": "Co-sharer / shareholder possessing an undivided fractional interest in a joint revenue estate.",
        "meaning_hi": "संयुक्त खातेदार / हिस्सेदार",
        "category": "Tenure"
    },

    # -----------------------------------------------------------------------
    # 3. LEGAL DEEDS & AGREEMENTS (DASTAVEZAT / اسناد و دستاویزات)
    # -----------------------------------------------------------------------
    "bainama": {
        "term_urdu": "بیع نامہ",
        "term_dev": "बैनामा",
        "meaning_en": "Absolute registered deed of sale conveying proprietary land title from seller to purchaser.",
        "meaning_hi": "विक्रय-पत्र (ज़मीन बेचने का रजिस्टर्ड दस्तावेज़)",
        "category": "Deed"
    },
    "rahannama": {
        "term_urdu": "رہن نامہ",
        "term_dev": "रहननामा",
        "meaning_en": "Mortgage deed pledging agricultural land as collateral for borrowed money (with or without possession).",
        "meaning_hi": "बंधक-पत्र / गिरवीनामा",
        "category": "Deed"
    },
    "fak_ur_rahan": {
        "term_urdu": "فک الرہن",
        "term_dev": "फक-उर-रहन",
        "meaning_en": "Deed of mortgage redemption formally releasing pledged land after full repayment of mortgage debt.",
        "meaning_hi": "बंधक-मुक्ति पत्र (गिरवी छुड़ाने का दस्तावेज़)",
        "category": "Deed"
    },
    "hibanama": {
        "term_urdu": "ہبہ نامہ",
        "term_dev": "हिबानामा",
        "meaning_en": "Deed of gift transferring property ownership voluntarily without financial consideration.",
        "meaning_hi": "दान-पत्र (उपहार स्वरूप ज़मीन देने का दस्तावेज़)",
        "category": "Deed"
    },
    "wasiyatnama": {
        "term_urdu": "وصیت نامہ",
        "term_dev": "वसीयतनामा",
        "meaning_en": "Last will and testament specifying testamentary devolution of land upon the testator's demise.",
        "meaning_hi": "वसीयत-पत्र",
        "category": "Deed"
    },
    "patta_araziyat": {
        "term_urdu": "پٹہ اراضیات",
        "term_dev": "पट्टा अराज़ियात",
        "meaning_en": "Agricultural land lease deed setting out duration, rent (Lagan), and terms of agrarian tenancy.",
        "meaning_hi": "कृषि पट्टा / लीज डीड",
        "category": "Deed"
    },
    "kirayanama": {
        "term_urdu": "کرایہ نامہ",
        "term_dev": "किरायानामा",
        "meaning_en": "Written tenancy contract or lease agreement specifying monthly/annual rent payments.",
        "meaning_hi": "किराया-पत्र / लीज एग्रीमेंट",
        "category": "Deed"
    },
    "iqrarnama": {
        "term_urdu": "اقرار نامہ",
        "term_dev": "इकरारनामा",
        "meaning_en": "Formal written agreement, contract of undertaking, or mutual covenant executed by parties.",
        "meaning_hi": "सहमति-पत्र / अनुबंध",
        "category": "Deed"
    },
    "tamassuk": {
        "term_urdu": "تمسک",
        "term_dev": "तमस्सुक",
        "meaning_en": "Promissory debt bond or written acknowledgment of monetary obligation with interest stipulation.",
        "meaning_hi": "ऋण-पत्र / प्रतिज्ञा-पत्र",
        "category": "Financial Instrument"
    },
    "farigh_khati": {
        "term_urdu": "فارغ خطی",
        "term_dev": "फ़ारिग़-ख़ती",
        "meaning_en": "Deed of complete release, discharge of liability, or written acquittance of financial claim.",
        "meaning_hi": "भार-मुक्ति प्रमाण-पत्र / बेबाक़ी-नामा",
        "category": "Deed"
    },
    "razinama": {
        "term_urdu": "راضی نامہ",
        "term_dev": "राज़ीनामा",
        "meaning_en": "Mutual compromise agreement or amicable settlement deed settling disputes out of court.",
        "meaning_hi": "सुलहनामा / राजीनामा",
        "category": "Deed"
    },
    "mukhtarnama_aam": {
        "term_urdu": "مختار نامہ عام",
        "term_dev": "मुख़्तारनामा आम",
        "meaning_en": "General Power of Attorney (GPA) authorizing an agent to manage, sell, and litigate on principal's behalf.",
        "meaning_hi": "सामान्य मुख्तारनामा (जनरल पावर ऑफ अटॉर्नी)",
        "category": "Power of Attorney"
    },
    "mukhtarnama_khas": {
        "term_urdu": "مختار نامہ خاص",
        "term_dev": "मुख़्तारनामा ख़ास",
        "meaning_en": "Special Power of Attorney (SPA) authorizing an agent for a single specific transaction or court case.",
        "meaning_hi": "विशेष मुख्तारनामा (स्पेशल पावर ऑफ अटॉर्नी)",
        "category": "Power of Attorney"
    },
    "dastavezat_taqseem": {
        "term_urdu": "دستاویز تقسیم",
        "term_dev": "दस्तावेज़ तक़सीम",
        "meaning_en": "Family partition deed dividing joint ancestral landed property into specific individual shares.",
        "meaning_hi": "बँटवारा-नामा (पारिवारिक भूमि बँटवारा दस्तावेज़)",
        "category": "Deed"
    },

    # -----------------------------------------------------------------------
    # 4. REVENUE JUDICIAL & COURT PROCEDURES
    # -----------------------------------------------------------------------
    "arzi_dawa_lagan": {
        "term_urdu": "عرضی دعویٰ لگان",
        "term_dev": "अर्ज़ी दावा लगान",
        "meaning_en": "Plaint / legal suit filed in revenue court by landowner against tenant for recovery of rent arrears.",
        "meaning_hi": "लगान वसूली का वाद-पत्र",
        "category": "Revenue Court"
    },
    "notice_wasoolyabi_lagan": {
        "term_urdu": "نوٹس وصولیابی لگان",
        "term_dev": "नोटिस वसूलीयाबी लगान",
        "meaning_en": "Formal statutory notice issued to a tenant demanding liquidation of outstanding agricultural rent.",
        "meaning_hi": "लगान भुगतान का वैधानिक नोटिस",
        "category": "Revenue Court"
    },
    "notice_alahidgi_kasht": {
        "term_urdu": "نوٹس علیحدگی کاشت",
        "term_dev": "नोटिस अलहदगी काश्त",
        "meaning_en": "Statutory notice of ejectment or determination of tenancy served upon a tenant-at-will.",
        "meaning_hi": "बेदखली का नोटिस / काश्त समाप्ति सूचना",
        "category": "Revenue Court"
    },
    "saman_haziri": {
        "term_urdu": "سمن حاضری",
        "term_dev": "समन हाज़िरी",
        "meaning_en": "Official summons requiring appearance of a party or witness before the Assistant Collector / Revenue Court.",
        "meaning_hi": "अदालती हाज़िरी समन",
        "category": "Revenue Court"
    },
    "wakalatnama": {
        "term_urdu": "وکالت نامہ",
        "term_dev": "वकालतनामा",
        "meaning_en": "Document authorizing an advocate or pleader to appear, plead, and act in revenue proceedings.",
        "meaning_hi": "अधिवक्ता नियुक्ति-पत्र",
        "category": "Revenue Court"
    },
    "hukmnama": {
        "term_urdu": "حکم نامہ",
        "term_dev": "हुक्मनामा",
        "meaning_en": "Official revenue court decree, warrant, or formal administrative order.",
        "meaning_hi": "न्यायिक / प्रशासनिक आदेश-पत्र",
        "category": "Revenue Court"
    },

    # -----------------------------------------------------------------------
    # 5. REVENUE ADMINISTRATION HIERARCHY
    # -----------------------------------------------------------------------
    "patwari": {
        "term_urdu": "پٹواری",
        "term_dev": "पटवारी",
        "meaning_en": "Village registrar and primary field revenue officer maintaining land records and conducting harvest inspections.",
        "meaning_hi": "ग्राम लेखपाल / पटवारी",
        "category": "Administration"
    },
    "girdawar": {
        "term_urdu": "گرداور (قانونگو)",
        "term_dev": "गिरदावर (क़ानूनगो)",
        "meaning_en": "Revenue field supervisor inspecting and verifying work of multiple Patwaris in a Girdawar circle.",
        "meaning_hi": "राजस्व निरीक्षक / कानूनगो",
        "category": "Administration"
    },
    "naib_tehsildar": {
        "term_urdu": "نائب تحصیلدار",
        "term_dev": "नायब तहसीलदार",
        "meaning_en": "Assistant Collector 2nd Grade empowered to attest mutations and decide undisputed tenancy matters.",
        "meaning_hi": "उप-तहसीलदार (सहायक कलेक्टर द्वितीय श्रेणी)",
        "category": "Administration"
    },
    "tehsildar": {
        "term_urdu": "تحصیلدار",
        "term_dev": "तहसीलदार",
        "meaning_en": "Head of Tehsil revenue administration; Assistant Collector 1st Grade trying contested revenue cases.",
        "meaning_hi": "तहसीलदार (सहायक कलेक्टर प्रथम श्रेणी)",
        "category": "Administration"
    },
    "collector": {
        "term_urdu": "کلکٹر (ڈپٹی کمشنر)",
        "term_dev": "कलेक्टर (उपायुक्त)",
        "meaning_en": "District Magistrate and chief revenue authority of the district hearing revenue appeals.",
        "meaning_hi": "ज़िला कलेक्टर / उपायुक्त",
        "category": "Administration"
    },
    "lambardar": {
        "term_urdu": "نمبردار",
        "term_dev": "नंबरदार",
        "meaning_en": "Village headman assisting revenue staff in land tax collection and boundary identification (Muqaddam).",
        "meaning_hi": "ग्राम मुखिया / लंबरदार",
        "category": "Administration"
    },
    "wasil_baqi_nawis": {
        "term_urdu": "واصل باقی نویس",
        "term_dev": "वासिल बाकी नवीस",
        "meaning_en": "Revenue accountant / ledger officer at the Tehsil headquarters keeping accounts of demands and arrears.",
        "meaning_hi": "तहसील राजस्व लेखाकार (मांग व बकाया मुंशी)",
        "category": "Administration"
    },

    # -----------------------------------------------------------------------
    # 6. MEASUREMENTS & AREA UNITS
    # -----------------------------------------------------------------------
    "kanal": {
        "term_urdu": "کنال",
        "term_dev": "कनाल",
        "meaning_en": "Standard unit of land area in J&K equal to 20 Marlas (5,445 sq ft or ~505.85 sq m).",
        "meaning_hi": "कनाल (20 मरले = 5445 वर्ग फुट)",
        "category": "Measurement"
    },
    "marla": {
        "term_urdu": "مرلہ",
        "term_dev": "मरला",
        "meaning_en": "Sub-unit of land area equal to 9 Sersai (272.25 sq ft or ~25.29 sq m).",
        "meaning_hi": "मरला (9 सरसाही = 272.25 वर्ग फुट)",
        "category": "Measurement"
    },
    "karam": {
        "term_urdu": "کرم",
        "term_dev": "करम",
        "meaning_en": "Linear measure equal to 5.5 feet (66 inches) used to pace and measure field dimensions.",
        "meaning_hi": "करम (कदम = 5.5 फुट या 66 इंच)",
        "category": "Measurement"
    },
    "sersai": {
        "term_urdu": "سرسائی",
        "term_dev": "सरसाही",
        "meaning_en": "Square measure of 1 Karam x 1 Karam = 30.25 sq ft. 9 Sersai make 1 Marla.",
        "meaning_hi": "सरसाही (1 करम × 1 करम = 30.25 वर्ग फुट)",
        "category": "Measurement"
    },
    "ghumaon": {
        "term_urdu": "گھماؤں",
        "term_dev": "घुमाऊं",
        "meaning_en": "Traditional acre unit in northern revenue systems equal to 8 Kanals (43,560 sq ft).",
        "meaning_hi": "घुमाऊं / एकड़ (8 कनाल = 43,560 वर्ग फुट)",
        "category": "Measurement"
    },
    "jarib": {
        "term_urdu": "جریب",
        "term_dev": "जरीब",
        "meaning_en": "Surveyor chain of iron links used to measure agricultural fields (traditionally 66 ft / 10 Karams).",
        "meaning_hi": "जरीब (ज़मीन नापने की लोहे की ज़ंजीर)",
        "category": "Measurement"
    },

    # -----------------------------------------------------------------------
    # 7. SOIL CLASSIFICATION & IRRIGATED ESTATES
    # -----------------------------------------------------------------------
    "abi": {
        "term_urdu": "آبی",
        "term_dev": "आबी",
        "meaning_en": "Irrigated land receiving perennial or seasonal water from rivers, streams, or springs.",
        "meaning_hi": "सिंचित भूमि",
        "category": "Soil Classification"
    },
    "abi_awal": {
        "term_urdu": "آبی اول",
        "term_dev": "आबी अव्वल",
        "meaning_en": "First-class perennially irrigated agricultural land with assured irrigation producing superior crops.",
        "meaning_hi": "प्रथम श्रेणी सिंचित भूमि (उत्तम जलापूर्ति)",
        "category": "Soil Classification"
    },
    "abi_doyum": {
        "term_urdu": "آبی دوئم",
        "term_dev": "आबी दोयम",
        "meaning_en": "Second-class seasonally irrigated land with intermittent or limited water access.",
        "meaning_hi": "द्वितीय श्रेणी सिंचित भूमि",
        "category": "Soil Classification"
    },
    "khushki": {
        "term_urdu": "خشکی",
        "term_dev": "खुश्کی",
        "meaning_en": "Non-irrigated or dry agricultural land dependent strictly on rain (Barani).",
        "meaning_hi": "असिंचित / बारानी भूमि",
        "category": "Soil Classification"
    },
    "chahi": {
        "term_urdu": "چاہی",
        "term_dev": "चाही",
        "meaning_en": "Land irrigated by wells or tube-wells.",
        "meaning_hi": "कुओं या नलकूपों द्वारा सिंचित भूमि",
        "category": "Soil Classification"
    },
    "nehri": {
        "term_urdu": "نہری",
        "term_dev": "नहरी",
        "meaning_en": "Agricultural land irrigated directly by government or community canals.",
        "meaning_hi": "नहर द्वारा सिंचित भूमि",
        "category": "Soil Classification"
    },
    "sailabi": {
        "term_urdu": "سیلابی",
        "term_dev": "सैलाबी",
        "meaning_en": "Land irrigated or replenished naturally by river floods or seasonal inundation.",
        "meaning_hi": "नदियों की बाढ़ से सिंचित भूमि",
        "category": "Soil Classification"
    },
    "banjar_qadeem": {
        "term_urdu": "بنجر قدیم",
        "term_dev": "बंजर क़दीम",
        "meaning_en": "Old fallow land that has remained uncultivated for eight or more consecutive harvests.",
        "meaning_hi": "पुरानी परती भूमि (लगातार 8 फसलों से असिंचित/खाली)",
        "category": "Soil Classification"
    },
    "banjar_jadeed": {
        "term_urdu": "بنجر جدید",
        "term_dev": "बंजर जदीद",
        "meaning_en": "New fallow land that has remained uncultivated for 4 to 7 harvests.",
        "meaning_hi": "नवीन परती भूमि (4 से 7 फसलों से खाली पड़ी जमीन)",
        "category": "Soil Classification"
    },
    "gair_mumkin": {
        "term_urdu": "غیر ممکن",
        "term_dev": "गैर मुमकिन",
        "meaning_en": "Barren or uncultivable land (rocks, pathways, ravines, riverbeds, habitation sites).",
        "meaning_hi": "अकृष्य / बंजर भूमि (रास्ता, खड्ड, मकान आदि)",
        "category": "Soil Classification"
    },
    "karewa": {
        "term_urdu": "کریوہ (وڈّر)",
        "term_dev": "करेवा (वुडुर)",
        "meaning_en": "Elevated lacustrine plateaus unique to Kashmir Valley (Wudur in Kashmiri) ideal for saffron and almond orchards.",
        "meaning_hi": "करेवा पठार (कश्मीर घाटी का विशिष्ट उपजाऊ पठार)",
        "category": "Topography"
    },
    "bagh": {
        "term_urdu": "باغ",
        "term_dev": "बाग़",
        "meaning_en": "Horticultural orchard land under apple, almond, walnut, pear, or cherry cultivation.",
        "meaning_hi": "फलों का बगीचा (सेब, बादाम, अखरोट आदि)",
        "category": "Horticulture"
    },
    "zafran_zamin": {
        "term_urdu": "زعفران زمین",
        "term_dev": "ज़ाफ़रान ज़मीन",
        "meaning_en": "Specialized Karewa land dedicated to saffron (Crocus sativus) cultivation, particularly in Pampore.",
        "meaning_hi": "केसर की खेती योग्य भूमि (पाम्पोर आदि)",
        "category": "Special Agriculture"
    }
}

def lookup_revenue_term(term: str) -> Optional[Dict[str, Any]]:
    """Look up a J&K revenue record term in English, Urdu, or Hindi."""
    if not term:
        return None
    key = term.lower().strip().replace(" ", "_").replace("-", "_")
    if key in REVENUE_TERMS:
        return REVENUE_TERMS[key]
    for k, v in REVENUE_TERMS.items():
        if (
            term in v.get("term_urdu", "")
            or term in v.get("term_dev", "")
            or term.lower() in v.get("meaning_en", "").lower()
            or term in v.get("meaning_hi", "")
        ):
            return v
    return None

def convert_land_area(kanals: float = 0.0, marlas: float = 0.0, sersai: float = 0.0) -> Dict[str, float]:
    """
    Converts Jammu & Kashmir traditional land units into standard measurements:
    Returns square feet, square meters, acres, and hectares.
    """
    total_marlas = (kanals * 20.0) + marlas + (sersai / 9.0)
    total_sq_ft = total_marlas * SQ_FEET_PER_MARLA
    total_sq_meters = total_sq_ft * SQ_METERS_PER_SQ_FOOT
    total_acres = total_sq_ft / SQ_FEET_PER_GHUMAON
    total_hectares = total_sq_meters / 10000.0

    return {
        "input": {"kanals": kanals, "marlas": marlas, "sersai": sersai},
        "total_marlas": round(total_marlas, 3),
        "total_kanals": round(total_marlas / 20.0, 3),
        "sq_feet": round(total_sq_ft, 2),
        "sq_meters": round(total_sq_meters, 2),
        "acres": round(total_acres, 4),
        "hectares": round(total_hectares, 4),
    }

def explain_record_type(doc_name: str) -> str:
    """Provides a clear legal and historical explanation of a revenue record type."""
    entry = lookup_revenue_term(doc_name)
    if not entry:
        return f"Unknown document type '{doc_name}'."
    return "\n".join([
        f"Document: {entry.get('term_dev')} / {entry.get('term_urdu')}",
        f"Category: {entry.get('category')}",
        f"Explanation: {entry.get('meaning_en')}",
        f"Hindi: {entry.get('meaning_hi')}"
    ])

def list_revenue_terms() -> List[str]:
    """Return all cataloged revenue terms."""
    return list(REVENUE_TERMS.keys())

def get_terms_by_category(category: str) -> List[Dict[str, Any]]:
    """Return all revenue terms under a specified category."""
    cat_lower = category.lower().strip()
    return [
        {"key": k, **v}
        for k, v in REVENUE_TERMS.items()
        if v.get("category", "").lower() == cat_lower
    ]

def list_categories() -> List[str]:
    """Return distinct categories of revenue terms."""
    return sorted(list(set(v.get("category", "") for v in REVENUE_TERMS.values())))

def search_revenue_terms(query: str) -> List[Dict[str, Any]]:
    """Search revenue terms by keyword in English, Urdu, Hindi, or category."""
    q = query.lower().strip()
    results = []
    for k, v in REVENUE_TERMS.items():
        if (
            q in k
            or q in v.get("term_urdu", "").lower()
            or q in v.get("term_dev", "").lower()
            or q in v.get("meaning_en", "").lower()
            or q in v.get("meaning_hi", "").lower()
            or q in v.get("category", "").lower()
        ):
            results.append({"key": k, **v})
    return results