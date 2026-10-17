"""
Virtual Keyboard & Phonetic Input Mappings for Kashmiri.
Provides:
1. Virtual on-screen keyboard layouts (row-by-row key definitions) for web apps.
2. Real-time QWERTY-to-Kashmiri keystroke transcriber for interactive inputs & search bars.
"""

from typing import Dict, List, Any
import koshur.scripts.transliterator as trans

# On-screen virtual keyboard layout definitions
KEYBOARD_LAYOUTS: Dict[str, Dict[str, Any]] = {
    "persoarabic": {
        "name": "Kashmiri Nastaliq Keyboard",
        "direction": "rtl",
        "rows": [
            ["١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩", "٠"],
            ["ض", "ص", "ث", "ق", "ف", "غ", "ع", "ہ", "خ", "ح", "ج", "چ", "ژ"],
            ["ش", "س", "ی", "ب", "ل", "ا", "ت", "ن", "م", "ک", "گ"],
            ["ظ", "ط", "ذ", "د", "ز", "ر", "و", "ۄ", "ؠ", "ٹ", "ڈ", "ڑ"],
            ["ٚ", "ٛ", "َ", "ِ", "ُ", "ْ", "ّ", "آ", "ء"]
        ]
    },
    "devanagari": {
        "name": "Kashmiri Devanagari Extended Keyboard",
        "direction": "ltr",
        "rows": [
            ["१", "२", "३", "४", "५", "६", "७", "८", "९", "०"],
            ["क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", "च़", "छ़", "ज़"],
            ["ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न"],
            ["प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह"],
            ["अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ", "ॳ", "ॴ", "ॶ", "ॷ"],
            ["ा", "ि", "ी", "ु", "ू", "े", "ै", "ो", "ौ", "ॅ", "ॉ", "ं", "ँ", "्"]
        ]
    },
    "sharada": {
        "name": "Sharada Classical Script Keyboard",
        "direction": "ltr",
        "rows": [
            ["𑇐", "𑇑", "𑇒", "𑇓", "𑇔", "𑇕", "𑇖", "𑇗", "𑇘", "𑇙"],
            ["𑆑", "𑆒", "𑆓", "𑆔", "𑆕", "𑆖", "𑆗", "𑆘", "𑆙", "𑆚"],
            ["𑆛", "𑆜", "𑆝", "𑆞", "𑆟", "𑆠", "𑆡", "𑆢", "𑆣", "𑆤"],
            ["𑆥", "𑆦", "𑆧", "𑆨", "𑆩", "𑆪", "𑆫", "𑆬", "𑆮", "𑆯", "𑆰", "𑆱", "𑆲"],
            ["𑆃", "𑆄", "𑆅", "𑆆", "𑆇", "𑆈", "𑆉", "𑆊", "𑆋", "𑆌", "𑆍", "𑆎", "𑆏", "𑆐"],
            ["𑆳", "𑆴", "𑆵", "𑆶", "𑆷", "𑆸", "𑆹", "𑆺", "𑆻", "𑆼", "𑆽", "𑆾", "𑆿", "𑇀", "𑆁", "𑆂"]
        ]
    }
}

def get_keyboard_layout(script: str = "persoarabic") -> Dict[str, Any]:
    """
    Returns virtual keyboard layout structure with rows of characters
    for frontend rendering.
    """
    s = script.lower().strip()
    if s in ["persoarabic", "arab", "arabic", "nastaliq"]:
        return KEYBOARD_LAYOUTS["persoarabic"]
    elif s in ["devanagari", "deva"]:
        return KEYBOARD_LAYOUTS["devanagari"]
    elif s in ["sharada", "sharda", "shrd"]:
        return KEYBOARD_LAYOUTS["sharada"]
    return KEYBOARD_LAYOUTS["devanagari"]

def transcribe_keystrokes(typed_ascii: str, target_script: str = "devanagari") -> str:
    """
    Real-time phonetic transcription engine for web search inputs and form fields.
    Allows users typing standard English QWERTY letters (e.g. 'koshur chhu asul')
    to be converted on the fly into native Kashmiri scripts.
    """
    if not typed_ascii:
        return ""

    target = target_script.lower().strip()
    if target in ["sharada", "sharda", "shrd"]:
        return trans.to_sharada(typed_ascii)
    elif target in ["persoarabic", "arab", "arabic", "nastaliq"]:
        return trans.to_persoarabic(typed_ascii)
    else:
        return trans.to_devanagari(typed_ascii)
