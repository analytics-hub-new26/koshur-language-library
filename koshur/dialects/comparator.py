"""
Comparative Dialectology Engine:
Compares phonological, lexical, and morphological variations across Kashmiri dialects:
Standard Valley Kashmiri, Kishtwari, Poguli, Siraji, and Rambani.
"""

from typing import Dict, Any, List
from koshur.dialects.kishtwari import get_kishtwari_info, KISHTWARI_INFO
from koshur.dialects.poguli import get_poguli_info, POGULI_INFO
from koshur.dialects.siraji import get_siraji_info, get_rambani_info, SIRAJI_INFO, RAMBANI_INFO

DIALECT_REGISTRY = {
    "standard": {
        "name": "Standard Valley Kashmiri (Koshur)",
        "region": "Kashmir Valley (Srinagar, Anantnag, Baramulla, etc.)",
        "iso_code": "kas",
        "script_traditions": ["Sharada", "Perso-Arabic", "Devanagari"],
    },
    "kishtwari": KISHTWARI_INFO,
    "poguli": POGULI_INFO,
    "siraji": SIRAJI_INFO,
    "rambani": RAMBANI_INFO,
}

def get_dialect_info(dialect_name: str) -> Dict[str, Any]:
    """Retrieve linguistic facts, region, and traits for a specific dialect."""
    key = dialect_name.lower().strip()
    return DIALECT_REGISTRY.get(key, {"error": f"Dialect '{dialect_name}' not found."})

def compare_dialects(concept: str) -> List[Dict[str, str]]:
    """
    Compare how a core lexical item or concept is represented
    across Standard Kashmiri, Kishtwari, Poguli, and Siraji.
    Matches across word, meaning, or Sanskrit cognate.
    """
    results = []
    c = concept.lower().strip()
    for item in KISHTWARI_INFO.get("sample_vocabulary", []):
        sk = item["standard_kashmiri"].lower()
        sk_lemma = item["standard_kashmiri"].split()[0].lower()
        sk_meaning = ""
        if "(" in item["standard_kashmiri"] and ")" in item["standard_kashmiri"]:
            sk_meaning = item["standard_kashmiri"].split("(")[1].split(")")[0].lower()
        sans = item.get("sanskrit", "").lower()

        if c in sk or c in sk_lemma or c in sk_meaning or c in sans:
            p_val = "N/A"
            for p_item in POGULI_INFO.get("sample_vocabulary", []):
                if p_item["standard_kashmiri"].split()[0].lower() == sk_lemma:
                    p_val = p_item["poguli"]
                    break

            s_val = "N/A"
            for s_item in SIRAJI_INFO.get("sample_vocabulary", []):
                if s_item["standard_kashmiri"].split()[0].lower() == sk_lemma:
                    s_val = s_item["siraji"]
                    break

            results.append({
                "concept": item["standard_kashmiri"],
                "standard_kashmiri": item["standard_kashmiri"].split()[0],
                "kishtwari": item["kishtwari"],
                "poguli": p_val,
                "siraji": s_val,
                "sanskrit_cognate": item.get("sanskrit", "N/A")
            })
    return results
