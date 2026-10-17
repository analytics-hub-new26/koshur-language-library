"""
Kashmiri Web & Mobile UI Localization (i18n) Engine.
Provides comprehensive translation of standard user interface strings across:
- Kashmiri Devanagari (कश्मीरी देवनागरी)
- Kashmiri Perso-Arabic (کٲشُر نستعلیق)
- Sharada (𑆯𑆳𑆫𑆢𑆳)
- Romanized Kashmiri (Latin phonetic)
- English (Reference fallback)

Supports direct integration with react-i18next, vue-i18n, Next.js, Flutter, Android, iOS.
"""

from typing import Dict, Any, List, Optional
import json

UI_STRINGS: Dict[str, Dict[str, str]] = {
    # Navigation
    "home": {
        "devanagari": "सादर",
        "persoarabic": "سادُر",
        "sharada": "𑆱𑆳𑆢𑆶𑆫",
        "roman": "Sadur",
        "english": "Home",
    },
    "search": {
        "devanagari": "खोज़",
        "persoarabic": "کھوج",
        "sharada": "𑆒𑆾𑆘",
        "roman": "Khōj",
        "english": "Search",
    },
    "menu": {
        "devanagari": "फेहरिस्त",
        "persoarabic": "فِہرِست",
        "sharada": "𑆦𑆼𑆲𑆫𑆴𑆱𑇀𑆠",
        "roman": "Fihrist",
        "english": "Menu",
    },
    "back": {
        "devanagari": "पतुह",
        "persoarabic": "پَتُہ",
        "sharada": "𑆥𑆠𑆶𑆲",
        "roman": "Patuh",
        "english": "Back",
    },
    "next": {
        "devanagari": "ब्रुंह",
        "persoarabic": "برونٛہہ",
        "sharada": "𑆧𑇀𑆫𑆶𑆁𑆲",
        "roman": "Brunh",
        "english": "Next",
    },
    "previous": {
        "devanagari": "पतुमक",
        "persoarabic": "پَتُمُک",
        "sharada": "𑆥𑆠𑆶𑆩𑆶𑆑",
        "roman": "Patumuk",
        "english": "Previous",
    },
    "settings": {
        "devanagari": "तरतीब",
        "persoarabic": "تَرتیب",
        "sharada": "𑆠𑆫𑇀𑆠𑆵𑆧",
        "roman": "Tartīb",
        "english": "Settings",
    },
    "help": {
        "devanagari": "मदथ",
        "persoarabic": "مَدَتھ",
        "sharada": "𑆩𑆢𑆡",
        "roman": "Madath",
        "english": "Help",
    },
    "about": {
        "devanagari": "मालूमात",
        "persoarabic": "معلومات",
        "sharada": "𑆩𑆳𑆬𑆷𑆩𑆳𑆠",
        "roman": "Mālūmāt",
        "english": "About",
    },
    "contact": {
        "devanagari": "राब्तॳ",
        "persoarabic": "رابِطہ",
        "sharada": "𑆫𑆳𑆧𑇀𑆠",
        "roman": "Rābtah",
        "english": "Contact",
    },

    # Actions
    "save": {
        "devanagari": "रछुन्",
        "persoarabic": "رَچھُن",
        "sharada": "𑆫𑆗𑆶𑆤𑇀",
        "roman": "Rachhun",
        "english": "Save",
    },
    "cancel": {
        "devanagari": "मंसूख़",
        "persoarabic": "مَنسوٗخ",
        "sharada": "𑆩𑆤𑇀𑆱𑆷𑆒",
        "roman": "Mansūkh",
        "english": "Cancel",
    },
    "delete": {
        "devanagari": "मेटुन",
        "persoarabic": "میٹُن",
        "sharada": "𑆩𑆼𑆛𑆶𑆤",
        "roman": "Mētun",
        "english": "Delete",
    },
    "edit": {
        "devanagari": "बदल",
        "persoarabic": "بَدَل",
        "sharada": "𑆧𑆢𑆬",
        "roman": "Badal",
        "english": "Edit",
    },
    "submit": {
        "devanagari": "सोज़ुन",
        "persoarabic": "سوزُن",
        "sharada": "𑆱𑆾𑆘𑆶𑆤",
        "roman": "Sōzun",
        "english": "Submit",
    },
    "send": {
        "devanagari": "सोज़ुन",
        "persoarabic": "سوزُن",
        "sharada": "𑆱𑆾𑆘𑆶𑆤",
        "roman": "Sōzun",
        "english": "Send",
    },
    "login": {
        "devanagari": "दाख़िल",
        "persoarabic": "داخِل",
        "sharada": "𑆢𑆳𑆒𑆴𑆬",
        "roman": "Dākhil",
        "english": "Login",
    },
    "logout": {
        "devanagari": "नेबर",
        "persoarabic": "نیبَر",
        "sharada": "𑆤𑆼𑆧𑆫",
        "roman": "Nēbar",
        "english": "Logout",
    },
    "sign_up": {
        "devanagari": "नव्युव खातॳ",
        "persoarabic": "نَویُک کھاتہ",
        "sharada": "𑆤𑆮𑇀𑆪𑆶𑆮 𑆒𑆳𑆠",
        "roman": "Navyuv Khātah",
        "english": "Sign Up",
    },
    "share": {
        "devanagari": "बागुन",
        "persoarabic": "باگُن",
        "sharada": "𑆧𑆳𑆓𑆶𑆤",
        "roman": "Bāgun",
        "english": "Share",
    },
    "download": {
        "devanagari": "बोन् अनन्",
        "persoarabic": "بۄن اَنُن",
        "sharada": "𑆧𑆾𑆤𑇀 𑆃𑆤𑆤𑇀",
        "roman": "Bōn Anan",
        "english": "Download",
    },
    "upload": {
        "devanagari": "हेर् च़ावुन",
        "persoarabic": "ہیر ژاوُن",
        "sharada": "𑆲𑆼𑆫𑇀 𑆖𑆳𑆮𑆶𑆤",
        "roman": "Hēr Tsāwun",
        "english": "Upload",
    },
    "refresh": {
        "devanagari": "ताज़ा करुन",
        "persoarabic": "تازَہ کَرُن",
        "sharada": "𑆠𑆳𑆘𑆳 𑆑𑆫𑆶𑆤",
        "roman": "Tāzah Karun",
        "english": "Refresh",
    },
    "close": {
        "devanagari": "बंद",
        "persoarabic": "بَند",
        "sharada": "𑆧𑆤𑇀𑆢",
        "roman": "Band",
        "english": "Close",
    },
    "open": {
        "devanagari": "उठ्यावुन",
        "persoarabic": "اُٹھاوُن",
        "sharada": "𑆇𑆜𑇀𑆪𑆳𑆮𑆶𑆤",
        "roman": "Uṭhyāwun",
        "english": "Open",
    },
    "view": {
        "devanagari": "वुछुन",
        "persoarabic": "وُچھُن",
        "sharada": "𑆮𑆶𑆗𑆶𑆤",
        "roman": "Wuchhun",
        "english": "View",
    },
    "click": {
        "devanagari": "दबाव",
        "persoarabic": "دَبَن",
        "sharada": "𑆢𑆧𑆳𑆮",
        "roman": "Dabāv",
        "english": "Click",
    },

    # Forms & Fields
    "name": {
        "devanagari": "नाव",
        "persoarabic": "ناو",
        "sharada": "𑆤𑆳𑆮",
        "roman": "Nāv",
        "english": "Name",
    },
    "email": {
        "devanagari": "ईमेल",
        "persoarabic": "ایمیل",
        "sharada": "𑆅𑆩𑆼𑆬",
        "roman": "Īmēl",
        "english": "Email",
    },
    "password": {
        "devanagari": "राज़-लफ़्ज़",
        "persoarabic": "راز لَفظ",
        "sharada": "𑆫𑆳𑆘 𑆬𑆦𑇀𑆘",
        "roman": "Rāz-Lafz",
        "english": "Password",
    },
    "phone": {
        "devanagari": "फ़ोन",
        "persoarabic": "فون",
        "sharada": "𑆦𑆾𑆤",
        "roman": "Phōn",
        "english": "Phone",
    },
    "address": {
        "devanagari": "पताह",
        "persoarabic": "پَتاہ",
        "sharada": "𑆥𑆠𑆳𑆲",
        "roman": "Patāh",
        "english": "Address",
    },
    "date": {
        "devanagari": "तारीख़",
        "persoarabic": "تاریخ",
        "sharada": "𑆠𑆳𑆫𑆵𑆒",
        "roman": "Tārīkh",
        "english": "Date",
    },
    "message": {
        "devanagari": "संदेश",
        "persoarabic": "سندیش",
        "sharada": "𑆱𑆁𑆢𑆼𑆯",
        "roman": "Sandēsh",
        "english": "Message",
    },
    "language": {
        "devanagari": "ज़ेव",
        "persoarabic": "زیو",
        "sharada": "𑆘𑆼𑆮",
        "roman": "Zēv",
        "english": "Language",
    },
    "country": {
        "devanagari": "मुल्क",
        "persoarabic": "مُلک",
        "sharada": "𑆩𑆶𑆬𑇀𑆑",
        "roman": "Mulk",
        "english": "Country",
    },
    "city": {
        "devanagari": "शहर",
        "persoarabic": "شَہَر",
        "sharada": "𑆯𑆲𑆫",
        "roman": "Shahar",
        "english": "City",
    },
    "account": {
        "devanagari": "खातॳ",
        "persoarabic": "کھاتہ",
        "sharada": "𑆒𑆳𑆠",
        "roman": "Khātah",
        "english": "Account",
    },
    "profile": {
        "devanagari": "पहचान",
        "persoarabic": "پَہچان",
        "sharada": "𑆥𑆲𑆖𑆳𑆤",
        "roman": "Pahchān",
        "english": "Profile",
    },

    # Status & Feedback
    "success": {
        "devanagari": "कामयाब",
        "persoarabic": "کامیاب",
        "sharada": "𑆑𑆳𑆩𑇀𑆪𑆳𑆧",
        "roman": "Kāmyāb",
        "english": "Success",
    },
    "error": {
        "devanagari": "ग़लत / नुक्सान",
        "persoarabic": "غَلَط",
        "sharada": "𑆓𑆳𑆬𑆠",
        "roman": "Galat",
        "english": "Error",
    },
    "warning": {
        "devanagari": "होशियार",
        "persoarabic": "ہوشیار",
        "sharada": "𑆲𑆾𑆯𑆴𑆪𑆳𑆫",
        "roman": "Hōshyār",
        "english": "Warning",
    },
    "loading": {
        "devanagari": "बोन् च़लान छु...",
        "persoarabic": "چَلان چھُ...",
        "sharada": "𑆖𑆬𑆳𑆤 𑆗𑆶...",
        "roman": "Chalān chhu...",
        "english": "Loading...",
    },
    "no_results": {
        "devanagari": "कांह नतीजा नी लब्याव",
        "persoarabic": "کانٛہہ نَتیجَہ نَہ لَبیاو",
        "sharada": "𑆑𑆳𑆁𑆲 𑆤𑆠𑆵𑆘𑆳 𑆤 𑆬𑆧𑇀𑆪𑆳𑆮",
        "roman": "Kānh natījah na labyāv",
        "english": "No results found",
    },
    "saved_successfully": {
        "devanagari": "अस्ल पाठी रछुन् कामयाब गोव",
        "persoarabic": "اَصٕل پاٹھؠ رَچھُن کامیاب گَو",
        "sharada": "𑆃𑆱𑆬 𑆥𑆳𑆜𑆴 𑆫𑆗𑆶𑆤𑇀 𑆑𑆳𑆩𑇀𑆪𑆳𑆧 𑆓𑆾𑆮",
        "roman": "Asul pāṭh' rachhun kāmyāb gow",
        "english": "Saved successfully",
    },
    "try_again": {
        "devanagari": "दोबारा कोशिश करिव",
        "persoarabic": "دوبارَہ کوشِش کَرِو",
        "sharada": "𑆢𑆾𑆧𑆳𑆫𑆳 𑆑𑆾𑆯𑆴𑆯 𑆑𑆫𑆴𑆮",
        "roman": "Dōbārah kōshish kariv",
        "english": "Try again",
    },
    "confirm_delete": {
        "devanagari": "क्या तोही छुवा पज़ मेटुन?",
        "persoarabic": "کیاہ تُہؠ چِھوا پَز میٹُن؟",
        "sharada": "𑆑𑇀𑆪𑆳 𑆠𑆾𑆲𑆵 𑆗𑆶𑆮𑆳 𑆥𑆘 𑆩𑆼𑆛𑆶𑆤?",
        "roman": "Kyāh toh' chhivā paz mētun?",
        "english": "Are you sure you want to delete?",
    },
    "notifications": {
        "devanagari": "ख़बरॳ",
        "persoarabic": "خَبَر",
        "sharada": "𑆒𑆧𑆫",
        "roman": "Khabarah",
        "english": "Notifications",
    },
    "welcome": {
        "devanagari": "ख़ुश आमदीद / नमस्कार",
        "persoarabic": "خوش آمدید",
        "sharada": "𑆒𑆶𑆯 𑆄𑆩𑆢𑆵𑆢 / 𑆤𑆩𑆱𑇀𑆑𑆳𑆫",
        "roman": "Khush Āmadīd / Namaskār",
        "english": "Welcome",
    },
}

def get_ui_string(key: str, script: str = "devanagari", fallback_to_en: bool = True) -> str:
    """
    Retrieve translated UI string for web/mobile apps.
    script options: 'devanagari', 'persoarabic', 'sharada', 'roman', 'english'.
    """
    k = key.lower().strip()
    if k not in UI_STRINGS:
        return key

    s = script.lower().strip()
    if s in ["dev", "deva", "devanagari"]:
        return UI_STRINGS[k]["devanagari"]
    elif s in ["arab", "arabic", "persoarabic", "nastaliq", "ur"]:
        return UI_STRINGS[k]["persoarabic"]
    elif s in ["sharda", "sharada", "shrd"]:
        return UI_STRINGS[k]["sharada"]
    elif s in ["roman", "latin", "en_phonetic"]:
        return UI_STRINGS[k]["roman"]
    elif s in ["en", "english"]:
        return UI_STRINGS[k]["english"]

    return UI_STRINGS[k]["devanagari"] if not fallback_to_en else UI_STRINGS[k]["english"]

def get_all_ui_keys() -> List[str]:
    """Return all registered UI dictionary keys."""
    return sorted(UI_STRINGS.keys())

def export_i18n_json(script: str = "devanagari", filepath: Optional[str] = None) -> Dict[str, str]:
    """
    Export all UI strings formatted as a key-value dictionary for JSON serialization.
    Compatible with React (i18next), Vue (vue-i18n), Next.js, and Android/iOS resource files.
    """
    res = {}
    for key in sorted(UI_STRINGS.keys()):
        res[key] = get_ui_string(key, script=script)

    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)

    return res
