"""
HTML and CSS Utilities for Kashmiri Web Development.
Handles:
- Script directionality (RTL vs LTR tagging)
- BCP 47 language subtag assignment (`ks-Arab`, `ks-Deva`, `ks-Shrd`, `ks-Latn`)
- WebFont CSS loading snippets for Google Fonts / open web fonts
- Semantic HTML markup wrapper for Kashmiri text
"""

from typing import Dict, Any, Optional

SCRIPT_METADATA: Dict[str, Dict[str, str]] = {
    "persoarabic": {
        "dir": "rtl",
        "lang": "ks-Arab",
        "font_family": "'Noto Nastaliq Urdu', 'Gulzar', 'Jameel Noori Nastaleeq', serif",
        "google_font": "Noto+Nastaliq+Urdu:wght@400;700",
        "description": "Kashmiri Perso-Arabic (RTL Nastaliq)"
    },
    "devanagari": {
        "dir": "ltr",
        "lang": "ks-Deva",
        "font_family": "'Noto Sans Devanagari', 'Kohinoor Devanagari', sans-serif",
        "google_font": "Noto+Sans+Devanagari:wght@400;600;700",
        "description": "Kashmiri Devanagari (LTR with central vowel diacritics)"
    },
    "sharada": {
        "dir": "ltr",
        "lang": "ks-Shrd",
        "font_family": "'Noto Sans Sharada', sans-serif",
        "google_font": "Noto+Sans+Sharada",
        "description": "Sharada Brahmic Script (LTR historical)"
    },
    "latin": {
        "dir": "ltr",
        "lang": "ks-Latn",
        "font_family": "'Inter', 'Segoe UI', system-ui, sans-serif",
        "google_font": "Inter:wght@400;600",
        "description": "Roman / Latin Academic Phonetic"
    }
}

def get_script_attributes(script: str) -> Dict[str, str]:
    """
    Returns HTML attributes required for correct rendering of a Kashmiri script:
    - `dir`: 'rtl' or 'ltr'
    - `lang`: BCP-47 tag (e.g. 'ks-Arab', 'ks-Deva', 'ks-Shrd')
    - `font_family`: CSS font-family stack
    """
    s = script.lower().strip()
    if s in ["persoarabic", "arab", "arabic", "nastaliq"]:
        return SCRIPT_METADATA["persoarabic"].copy()
    elif s in ["devanagari", "deva", "dev"]:
        return SCRIPT_METADATA["devanagari"].copy()
    elif s in ["sharada", "sharda", "shrd"]:
        return SCRIPT_METADATA["sharada"].copy()
    else:
        return SCRIPT_METADATA["latin"].copy()

def generate_webfont_css(include_cdn: bool = True) -> str:
    """
    Generates ready-to-paste CSS snippet for embedding and rendering
    Kashmiri scripts in web applications.
    """
    fonts = [
        "https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Noto+Sans+Sharada&display=swap"
    ]

    imports = "\n".join(f'@import url("{f}");' for f in fonts) if include_cdn else "/* Embed local font files */"

    css = f"""{imports}

/* =======================================================
   Koshur Web Toolkit Typography Stylesheet
   ======================================================= */

.koshur-persoarabic {{
  direction: rtl;
  font-family: 'Noto Nastaliq Urdu', 'Gulzar', serif;
  line-height: 2.2;
  font-size: 1.15rem;
  text-align: right;
}}

.koshur-devanagari {{
  direction: ltr;
  font-family: 'Noto Sans Devanagari', sans-serif;
  line-height: 1.6;
}}

.koshur-sharada {{
  direction: ltr;
  font-family: 'Noto Sans Sharada', sans-serif;
  line-height: 1.6;
  letter-spacing: 0.05em;
}}

.koshur-latin {{
  direction: ltr;
  font-family: system-ui, -apple-system, sans-serif;
  line-height: 1.5;
}}
"""
    return css

def wrap_html_text(text: str, script: str = "devanagari", class_name: Optional[str] = None) -> str:
    """
    Wraps Kashmiri text inside a semantic HTML <span> with correct dir and lang tags.
    Example:
        wrap_html_text("کٲشُر", "persoarabic")
        -> '<span dir="rtl" lang="ks-Arab" class="koshur-persoarabic">کٲشُر</span>'
    """
    attrs = get_script_attributes(script)
    cls = class_name if class_name else f"koshur-{script.lower()}"
    return f'<span dir="{attrs["dir"]}" lang="{attrs["lang"]}" class="{cls}">{text}</span>'
