"""
Kashmiri Local Deities, Tīrthas & Guardian Spirits:
Comprehensive pantheon of Kashmiri Shakta Devi shrines, Shiva tirthas,
the Nilamata Purana sacred Nagas, Ashta Bhairavas of the Valley, and Resh Vaer saints.
"""

from typing import List, Dict, Any, Optional
import unicodedata

KASHMIRI_DEITIES: List[Dict[str, Any]] = [
    {
        "id": "sharika_devi",
        "name": "Sharika Devi (Chakreshwar)",
        "devanagari": "शारिका देवी (चक्रेश्वर)",
        "persoarabic": "شارِکا دیوی (چَکریشنوَر)",
        "sharada": "𑆯𑆳𑆫𑆴𑆑𑆳 𑆢𑆼𑆮𑆵 (𑆖𑆑𑇀𑆫𑆼𑆯𑇀𑆮𑆫)",
        "epithets": ["Chakreshwari", "Tripurasundari", "Hari Parbat Devi"],
        "shrine_location": "Hari Parbat (Koh-i-Maran), Srinagar",
        "iconography": "Swayambhu (self-manifested) 18-armed mystic Sri Chakra carved on a vertical rock smeared with sindoor.",
        "mythological_origin": "According to the Nilamata Purana, when the demon Jalodbhava submerged Kashmir under water (Satisaras), Goddess Parvati assumed the form of a mythical Myna bird (Hāri) and dropped a celestial pebble that crushed the demon, forming the hill of Hari Parbat.",
        "annual_festival": "Navreh (New Year) and Har Navami (Ashadha Shukla Navami).",
        "category": "shakta_presiding_deity"
    },
    {
        "id": "maharagnya_kheer_bhawani",
        "name": "Maharagnya Bhagwati (Kheer Bhawani)",
        "devanagari": "महाराज्ञा भगवती (खीर भवानी)",
        "persoarabic": "مَہاراگِیا بھَگوَتی (کھِیر بھَوانی)",
        "sharada": "𑆩𑆲𑆳𑆫𑆳𑆘𑇀𑆚𑆵 𑆪𑆔𑆮𑆠𑆵 (𑆒𑆵𑆫 𑆪𑆮𑆳𑆤𑆵)",
        "epithets": ["Ragnya Devi", "Kheer Bhawani", "Tulmul Devi", "Maharagnya"],
        "shrine_location": "Tulmulla, Ganderbal (Kashmir Valley)",
        "iconography": "Sacred spring pool (Nag) surrounded by Chinar groves. Offerings of milk, kheer, and puffed candy.",
        "miraculous_phenomenon": "The waters of the sacred spring pool change colors (milky white, rose pink, azure blue, emerald green, and slate dark), traditionally seen as omens regarding the welfare of the Valley.",
        "annual_festival": "Jyeshtha Ashtami (May-June), drawing thousands of pilgrims from across the globe.",
        "category": "shakta_presiding_deity"
    },
    {
        "id": "jwala_ji",
        "name": "Jwala Ji (Jwalamukhi Khrew)",
        "devanagari": "ज्वाला जी (ख्रेव)",
        "persoarabic": "جوالا جی (کھریو)",
        "sharada": "𑆘𑇀𑆮𑆳𑆬𑆳 𑆘𑆵 (𑆒𑇀𑆫𑆼𑆮)",
        "epithets": ["Jwalamukhi", "Jwala Devi", "Khrew Tirtha"],
        "shrine_location": "Khrew, Pulwama (amidst the saffron fields of Pampore)",
        "iconography": "Sanctified volcanic stone outcrop representing the living flame of Goddess Shakti.",
        "annual_festival": "Ashadha Shukla Chaturdashi (Jwala Chaturdashi).",
        "category": "shakta_devi"
    },
    {
        "id": "jyeshtha_devi",
        "name": "Jyeshtha Devi (Zeashta / Zeathyar)",
        "devanagari": "ज्येष्ठा देवी (ज़ेष्ठयार)",
        "persoarabic": "زیٹھا دیوی (زیٹھیار)",
        "sharada": "𑆘𑇀𑆪𑆼𑆰𑇀𑆜𑆳 𑆢𑆼𑆮𑆵 (𑆘𑆼𑆰𑇀𑆜𑆪𑆳𑆫)",
        "epithets": ["Zeashta", "Zeathyar", "Jyeshtha Bhagwati"],
        "shrine_location": "Zeathyar, Srinagar (near Cheshma Shahi on the foothills of Zabarwan range)",
        "description": "Ancient protector goddess propitiated against sickness, misfortune, and evil planetary influences. Surrounded by freshwater springs.",
        "category": "shakta_devi"
    },
    {
        "id": "sureshwari_devi",
        "name": "Sureshwari (Durga Peak)",
        "devanagari": "सुरेश्वरी देवी",
        "persoarabic": "سُریشوَری دیوی",
        "sharada": "𑆱𑆶𑆫𑆼𑆯𑇀𑆮𑆫𑆵 𑆢𑆼𑆮𑆵",
        "epithets": ["Sureshwari", "Durga Peak"],
        "shrine_location": "High craggy mountain peak overlooking Dal Lake and Nishat / Gupt Ganga",
        "description": "Fierce guardian form of Goddess Durga invoked in Kalhana's Rajatarangini.",
        "category": "shakta_devi"
    },
    {
        "id": "bala_tripurasundari",
        "name": "Bala Tripurasundari",
        "devanagari": "बाला त्रिपुरासुंदरी",
        "persoarabic": "بالا تریپُرا سُندَری",
        "sharada": "𑆧𑆳𑆬𑆳 𑆠𑇀𑆫𑆴𑆥𑆶𑆫𑆳𑆱𑆶𑆤𑇀𑆢𑆫𑆵",
        "epithets": ["Bala Devi", "Bhuvaneshwari"],
        "shrine_location": "Khonmoh (Bhuvaneshwari) / Bawan / Mattan",
        "description": "The youthful, radiant aspect of the Divine Mother presiding over supreme wisdom and Sri Vidya esoteric knowledge.",
        "category": "shakta_devi"
    },
    {
        "id": "vitasta_devi",
        "name": "Vitasta Devi (Goddess of the Jhelum)",
        "devanagari": "वितस्ता देवी",
        "persoarabic": "وِتَستا دیوی",
        "sharada": "𑆮𑆴𑆠𑆱𑇀𑆠𑆳 𑆢𑆼𑆮𑆵",
        "epithets": ["Vyeth", "Vitasta", "Jhelum Goddess"],
        "shrine_location": "Verinag spring pool & the entire course of the Vyeth (Jhelum) river",
        "mythological_origin": "The Nilamata Purana records that Lord Shiva pierced the earth with his trident (shula) at Verinag, causing Parvati to descend as the river Vitasta to purify the valley.",
        "annual_festival": "Vitasta Truwah (Bhadrapada Shukla Trayodashi), celebrated with illuminated lamps (Dīpa-dāna) floated down the river.",
        "category": "river_goddess"
    },
    {
        "id": "nila_naga",
        "name": "Nila Naga (Lord of Kashmiri Nagas)",
        "devanagari": "नील नाग",
        "persoarabic": "نیل ناگ",
        "sharada": "𑆤𑆵𑆬 𑆤𑆳𑆔",
        "epithets": ["Nilnag", "Nilanag", "Nila Naga", "King of Nagas"],
        "shrine_location": "Nilnag Lake, Budgam / Yusmarg pine forests",
        "mythological_origin": "Son of Sage Kashyapa and the sovereign deity of all subterranean and aquatic serpentine guardian spirits (Nāgas) of Kashmir. Prolocutor of the Nilamata Purana.",
        "description": "Son of Sage Kashyapa and sovereign king of all Kashmiri Nagas as established in the Nilamata Purana.",
        "category": "naga_deity"
    },
    {
        "id": "amarnath_shiva",
        "name": "Amarnath (Swayambhu Ice Lingam)",
        "devanagari": "अमरनाथ (हिम शिवलिंग)",
        "persoarabic": "اَمَر ناتھ (ہِم شِولِنگ)",
        "sharada": "𑆃𑆩𑆫𑆤𑆳𑆡 (𑆲𑆴𑆩 𑆯𑆴𑆮𑆬𑆴𑆕𑇀𑆔)",
        "epithets": ["Amreshwar", "Amarnath", "Ice Lingam"],
        "shrine_location": "Amarnath Holy Cave (3,888 m / 12,756 ft), Lidder Valley",
        "mythological_origin": "The high Himalayan cave sanctuary where Lord Shiva revealed the secret of immortality (Amara-katha) to Goddess Parvati.",
        "annual_festival": "Shravana Purnima (Raksha Bandhan).",
        "category": "shiva_tirtha"
    },
    {
        "id": "kapal_mochan",
        "name": "Kapal Mochan Tirtha",
        "devanagari": "कपाल मोचन तीर्थ",
        "persoarabic": "کَپال موچَن تیرتھ",
        "sharada": "𑆑𑆥𑆳𑆬 𑆩𑆾𑆖𑆤 𑆠𑆵𑆫𑇀𑆡",
        "epithets": ["Kapalmochan", "Shopian Tirtha"],
        "shrine_location": "Degam, Shopian",
        "description": "Sacred spring tirtha for pitri-tarpana and ancestral liberation rites, sanctified where Shiva cleansed Himself of the sin of severance of Brahma's fifth skull.",
        "category": "shiva_tirtha"
    }
]

ASHTA_BHAIRAVAS: List[Dict[str, Any]] = [
    {
        "name": "Anandeshwar Bhairava",
        "direction": "South",
        "location": "Maisuma, Srinagar (along Jhelum river bank)",
        "devanagari": "आनंदेश्वर भैरव",
        "persoarabic": "آنَندیشوَر بھَیرَو",
        "role": "Guardian of peace and delight, protector against calamities."
    },
    {
        "name": "Tukshak Bhairava",
        "direction": "South-East",
        "location": "Zewan, Srinagar",
        "devanagari": "तक्षक भैरव",
        "persoarabic": "تَکشَک بھَیرَو",
        "role": "Associated with Takshaka Naga, protector of subterranean energies."
    },
    {
        "name": "Bahukhatkeshwar Bhairava",
        "direction": "East",
        "location": "Rainawari / Naidyar, Srinagar",
        "devanagari": "बाहुखटकेश्वर भैरव",
        "persoarabic": "باہُوکھَٹکیشوَر بھَیرَو",
        "role": "Protector of waterways and lagoons entering Dal Lake."
    },
    {
        "name": "Vetal Bhairava",
        "direction": "North-East",
        "location": "Motiyar / Rainawari, Srinagar",
        "devanagari": "वेताल भैरव",
        "persoarabic": "ویتال بھَیرَو",
        "role": "Subduer of malevolent ghosts and master of occult mystical powers."
    },
    {
        "name": "Purushayar Bhairava",
        "direction": "South-West",
        "location": "Habba Kadal, Srinagar (Second Bridge)",
        "devanagari": "पुरुषयार भैरव",
        "persoarabic": "پُرُش یار بھَیرَو",
        "role": "Protector of historic downtown Srinagar cultural quarter."
    },
    {
        "name": "Seeta Bhairava",
        "direction": "North-West",
        "location": "Varmul (Baramulla)",
        "devanagari": "सीता भैरव",
        "persoarabic": "سیٖتا بھَیرَو",
        "role": "Guardian of the western gateway into the Kashmir Valley."
    },
    {
        "name": "Kamaleshwar Bhairava",
        "direction": "North",
        "location": "Chattabal / Veer, Srinagar",
        "devanagari": "कमलेश्वर भैरव",
        "persoarabic": "کَمَلیشوَر بھَیرَو",
        "role": "Protector of the northern river exit of the Vitasta."
    },
    {
        "name": "Bhairav Mandir Pokhribal",
        "direction": "West",
        "location": "Pokhribal / Hari Parbat foothill",
        "devanagari": "पोखरिबल भैरव",
        "persoarabic": "پوکھرِی بَل بھَیرَو",
        "role": "Guardian of the sacred spring pool below the Hari Parbat citadel."
    }
]

def _clean_deity_str(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower().replace(" ", "").replace("_", "").replace("-", "")

def lookup_deity(name_or_id: str) -> Optional[Dict[str, Any]]:
    """Look up a Kashmiri deity by name, ID, or epithet (diacritic & space-insensitive)."""
    raw_q = name_or_id.strip()
    q = _clean_deity_str(raw_q)
    for d in KASHMIRI_DEITIES:
        d_id = _clean_deity_str(d["id"])
        d_name = _clean_deity_str(d["name"])
        d_eps = [_clean_deity_str(ep) for ep in d.get("epithets", [])]
        d_loc = _clean_deity_str(d.get("shrine_location", ""))
        
        if (
            q in d_id
            or d_id in q
            or q in d_name
            or any(q in ep for ep in d_eps)
            or q in d_loc
            or raw_q in d.get("devanagari", "")
            or raw_q in d.get("persoarabic", "")
            or raw_q in d.get("sharada", "")
        ):
            return d
    return None

def get_all_deities() -> List[Dict[str, Any]]:
    """Return all cataloged Kashmiri deities and sacred shrines."""
    return KASHMIRI_DEITIES

def get_guardian_bhairavas() -> List[Dict[str, Any]]:
    """Return the Ashta Bhairavas (eight guardian directional deities) of Kashmir."""
    return ASHTA_BHAIRAVAS
