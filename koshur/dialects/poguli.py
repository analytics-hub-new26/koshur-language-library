"""
Poguli Dialect Module:
Poguli (पोगुली / پوگلی) is an endangered language/dialect spoken in the Pogal
and Paristan valleys in Ramban District, Jammu & Kashmir. It forms an essential
transitional link between Dardic Kashmiri and Western Pahari.
"""

from typing import Dict, Any, List

POGULI_INFO: Dict[str, Any] = {
    "name": "Poguli",
    "native_name": "पोगुली / پوگلی",
    "region": "Pogal-Paristan valleys, Ramban District, J&K",
    "classification": "Indo-Aryan -> Dardic / Pahari Transition",
    "endangerment_status": "Definitively Endangered (UNESCO)",
    "key_phonological_traits": [
        "Transitional morphology between Kashmiri V2 and Western Pahari SOV.",
        "Retention of distinct case endings and gender marking.",
        "Phonetic inventory intermediate between Kashmiri central vowels and Pahari back vowels."
    ],
    "sample_vocabulary": [{'standard_kashmiri': 'bōi (brother)', 'poguli': 'bhrāu', 'sanskrit': 'bhrātṛ'}, {'standard_kashmiri': 'māj (mother)', 'poguli': 'māy', 'sanskrit': 'mātṛ'}, {'standard_kashmiri': 'mōl (father)', 'poguli': 'bāp', 'sanskrit': 'pitṛ'}, {'standard_kashmiri': 'beni (sister)', 'poguli': 'bhēṇ', 'sanskrit': 'bhaginī'}, {'standard_kashmiri': 'nēchuv (son)', 'poguli': 'putru', 'sanskrit': 'putra'}, {'standard_kashmiri': 'kōr (daughter)', 'poguli': 'dhī', 'sanskrit': 'duhitṛ'}, {'standard_kashmiri': 'achh (eye)', 'poguli': 'achhī', 'sanskrit': 'akṣi'}, {'standard_kashmiri': 'kān (ear)', 'poguli': 'kann', 'sanskrit': 'karṇa'}, {'standard_kashmiri': 'athə (hand)', 'poguli': 'hāth', 'sanskrit': 'hasta'}, {'standard_kashmiri': 'khōr (foot)', 'poguli': 'pair', 'sanskrit': 'pāda'}, {'standard_kashmiri': 'shīn (snow)', 'poguli': 'shīn', 'sanskrit': 'śīna'}, {'standard_kashmiri': 'āb (water)', 'poguli': 'pānī', 'sanskrit': 'pānīya'}, {'standard_kashmiri': 'rūd (rain)', 'poguli': 'barshāt', 'sanskrit': 'varṣā'}, {'standard_kashmiri': 'chhu (is)', 'poguli': 'chhu', 'sanskrit': 'asti'}, {'standard_kashmiri': 'khyun (to eat)', 'poguli': 'khānu', 'sanskrit': 'khādana'}, {'standard_kashmiri': 'chāwun (to drink)', 'poguli': 'pīnu', 'sanskrit': 'pāna'}, {'standard_kashmiri': 'gatsun (to go)', 'poguli': 'gachhu', 'sanskrit': 'gamana'}, {'standard_kashmiri': 'yun (to come)', 'poguli': 'ēnu', 'sanskrit': 'āgamana'}, {'standard_kashmiri': 'parun (to read)', 'poguli': 'parhnu', 'sanskrit': 'paṭhana'}, {'standard_kashmiri': 'lekhun (to write)', 'poguli': 'likhnu', 'sanskrit': 'lekhana'}, {'standard_kashmiri': 'bod (big)', 'poguli': 'baṛā', 'sanskrit': 'vṛddha'}, {'standard_kashmiri': 'lokhuk (small)', 'poguli': 'lōku', 'sanskrit': 'laghuka'}, {'standard_kashmiri': 'vyeth (jhelum river)', 'poguli': 'vyath', 'sanskrit': 'vitastā'}]
}

def get_poguli_info() -> Dict[str, Any]:
    """Returns sociolinguistic and linguistic details for Poguli."""
    return POGULI_INFO
