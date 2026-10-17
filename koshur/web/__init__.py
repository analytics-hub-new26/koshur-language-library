"""
Koshur Web Development & UI Localization Toolkit.
Everything a developer needs to build websites, mobile apps, and user interfaces
in the Kashmiri language.
"""

from koshur.web.i18n import (
    UI_STRINGS,
    get_ui_string,
    get_all_ui_keys,
    export_i18n_json
)
from koshur.web.html_helper import (
    SCRIPT_METADATA,
    get_script_attributes,
    generate_webfont_css,
    wrap_html_text
)
from koshur.web.keyboard import (
    KEYBOARD_LAYOUTS,
    get_keyboard_layout,
    transcribe_keystrokes
)

__all__ = [
    "UI_STRINGS",
    "get_ui_string",
    "get_all_ui_keys",
    "export_i18n_json",
    "SCRIPT_METADATA",
    "get_script_attributes",
    "generate_webfont_css",
    "wrap_html_text",
    "KEYBOARD_LAYOUTS",
    "get_keyboard_layout",
    "transcribe_keystrokes",
]
