"""
Kishtwari Dialect Module:
Kishtwari (किश्तवाड़ी / کشتواڑی) is spoken in the Kishtwar Valley of Jammu & Kashmir.
Linguistically recognized by Sir George Grierson and modern scholars as the most archaic
dialect of Kashmiri, preserving historical consonant clusters and ancient grammatical
forms that have evolved or simplified in standard Valley Kashmiri.
"""

from typing import Dict, Any, List

KISHTWARI_INFO: Dict[str, Any] = {
    "name": "Kishtwari (Kashtawari)",
    "native_name": "किश्तवाड़ी / کشتواڑی",
    "region": "Kishtwar District, Jammu & Kashmir",
    "classification": "Indo-Aryan -> Northwestern / Dardic -> Kashmiri group",
    "endangerment_status": "Vulnerable / Under-documented",
    "key_phonological_traits": [
        "Retention of archaic consonant clusters that were simplified in standard Kashmiri.",
        "Preservation of final unstressed vowels.",
        "Less extensive vowel mutation (ablaut) compared to Valley Kashmiri.",
        "Retention of archaic dental affricates."
    ],
    "sample_vocabulary": [{'standard_kashmiri': 'bōi (brother)', 'kishtwari': 'bhrāu', 'sanskrit': 'bhrātṛ'}, {'standard_kashmiri': 'māj (mother)', 'kishtwari': 'mātā / māj', 'sanskrit': 'mātṛ'}, {'standard_kashmiri': 'mōl (father)', 'kishtwari': 'bāp / mōl', 'sanskrit': 'mūla / pitṛ'}, {'standard_kashmiri': 'beni (sister)', 'kishtwari': 'bhēn', 'sanskrit': 'bhaginī'}, {'standard_kashmiri': 'nēchuv (son)', 'kishtwari': 'pōtru', 'sanskrit': 'putra'}, {'standard_kashmiri': 'kōr (daughter)', 'kishtwari': 'kōrī', 'sanskrit': 'kumārī'}, {'standard_kashmiri': 'achh (eye)', 'kishtwari': 'achhī', 'sanskrit': 'akṣi'}, {'standard_kashmiri': 'kān (ear)', 'kishtwari': 'kann', 'sanskrit': 'karṇa'}, {'standard_kashmiri': 'athə (hand)', 'kishtwari': 'hāth', 'sanskrit': 'hasta'}, {'standard_kashmiri': 'khōr (foot)', 'kishtwari': 'khōr', 'sanskrit': 'khora'}, {'standard_kashmiri': 'shīn (snow)', 'kishtwari': 'hīm / shīn', 'sanskrit': 'śīna / hima'}, {'standard_kashmiri': 'āb (water)', 'kishtwari': 'pānī', 'sanskrit': 'pānīya'}, {'standard_kashmiri': 'rūd (rain)', 'kishtwari': 'barshāt', 'sanskrit': 'varṣā'}, {'standard_kashmiri': 'chhu (is)', 'kishtwari': 'thu', 'sanskrit': 'asti'}, {'standard_kashmiri': 'khyun (to eat)', 'kishtwari': 'khān', 'sanskrit': 'khādana'}, {'standard_kashmiri': 'chāwun (to drink)', 'kishtwari': 'pīwan', 'sanskrit': 'pāna'}, {'standard_kashmiri': 'gatsun (to go)', 'kishtwari': 'gatshun', 'sanskrit': 'gamana'}, {'standard_kashmiri': 'yun (to come)', 'kishtwari': 'īwan', 'sanskrit': 'āgamana'}, {'standard_kashmiri': 'parun (to read)', 'kishtwari': 'parhun', 'sanskrit': 'paṭhana'}, {'standard_kashmiri': 'lekhun (to write)', 'kishtwari': 'likhun', 'sanskrit': 'lekhana'}, {'standard_kashmiri': 'bod (big)', 'kishtwari': 'baṛo', 'sanskrit': 'vṛddha'}, {'standard_kashmiri': 'lokhuk (small)', 'kishtwari': 'chhoṭo', 'sanskrit': 'laghuka'}, {'standard_kashmiri': 'vyeth (jhelum river)', 'kishtwari': 'vyath', 'sanskrit': 'vitastā'}]
}

def get_kishtwari_info() -> Dict[str, Any]:
    """Returns sociolinguistic and linguistic details for Kishtwari."""
    return KISHTWARI_INFO
