"""
Kashmiri Verb Conjugation, Split-Ergativity & Clitics Engine.
Generates present, past, and future inflections for Kashmiri verb stems,
along with pronominal suffix cliticization, imperative forms, and converbs.

Kashmiri demonstrates classic Split-Ergativity:
- Non-past tenses (Present, Future): Nominative-Accusative alignment (Verb agrees with Subject).
- Past tense of Transitive verbs: Ergative-Absolutive alignment (Verb agrees with Object in gender/number, Subject takes Ergative case suffix).
- Past tense of Intransitive verbs: Nominative alignment (Verb agrees with Subject).
"""

from typing import Dict, Any

# Expanded Kashmiri core verb database
VERB_LEXICON: Dict[str, Dict[str, Any]] = {
    "parun": {
        "infinitive": "parun (परुन / پَرُن)",
        "meaning": "to read / study",
        "root": "par",
        "transitive": True,
        "present_participle": "parān (परान / پَران)",
        "past_stems": {"m_sg": "por", "m_pl": "pərʲ", "f_sg": "pər", "f_pl": "pare"},
        "future_stem": "pari",
    },
    "khyun": {
        "infinitive": "khyun (ख्युन / کھؠن)",
        "meaning": "to eat",
        "root": "khe",
        "transitive": True,
        "present_participle": "khyavān (ख्यवान / کھؠوان)",
        "past_stems": {"m_sg": "khew", "m_pl": "khey", "f_sg": "kheyi", "f_pl": "kheye"},
        "future_stem": "kheyi",
    },
    "chāwun": {
        "infinitive": "chāwun (चावुन / چاوُن)",
        "meaning": "to drink",
        "root": "che",
        "transitive": True,
        "present_participle": "chavān (चवान / چَوان)",
        "past_stems": {"m_sg": "chew", "m_pl": "chey", "f_sg": "cheyi", "f_pl": "cheye"},
        "future_stem": "ceyi",
    },
    "karun": {
        "infinitive": "karun (करुन / کَرُن)",
        "meaning": "to do / make",
        "root": "kar",
        "transitive": True,
        "present_participle": "karān (करान / کَران)",
        "past_stems": {"m_sg": "kor", "m_pl": "kərʲ", "f_sg": "kər", "f_pl": "kare"},
        "future_stem": "kari",
    },
    "gatsun": {
        "infinitive": "gatsun (गछुन / گَژھُن)",
        "meaning": "to go",
        "root": "gatsh",
        "transitive": False,
        "present_participle": "gatshān (गछ़ान / گَژھان)",
        "past_stems": {"m_sg": "gow", "m_pl": "geyi", "f_sg": "gayi", "f_pl": "gaye"},
        "future_stem": "gatshi",
    },
    "yun": {
        "infinitive": "yun (यिन / یِن)",
        "meaning": "to come",
        "root": "yi",
        "transitive": False,
        "present_participle": "yivān (यिवान / یِوان)",
        "past_stems": {"m_sg": "aav", "m_pl": "aayi", "f_sg": "aayi", "f_pl": "aaye"},
        "future_stem": "yiyi",
    },
    "lēkhun": {
        "infinitive": "lēkhun (लेखुन / لیٚکھُن)",
        "meaning": "to write",
        "root": "lekh",
        "transitive": True,
        "present_participle": "lekhān (लेखान / لیٖکھان)",
        "past_stems": {"m_sg": "lyūkh", "m_pl": "līkhʲ", "f_sg": "līchhi", "f_pl": "lēchhe"},
        "future_stem": "lēkhi",
    },
    "wuchhun": {
        "infinitive": "wuchhun (वुछुन / وُچھُن)",
        "meaning": "to see / look",
        "root": "wuchh",
        "transitive": True,
        "present_participle": "wuchhān (वुछान / وُچھان)",
        "past_stems": {"m_sg": "wuchh", "m_pl": "wuchhʲ", "f_sg": "wuchh", "f_pl": "wuchhe"},
        "future_stem": "wuchhi",
    },
    "bōzun": {
        "infinitive": "bōzun (बोज़ुन / بوزُن)",
        "meaning": "to hear / understand",
        "root": "bōz",
        "transitive": True,
        "present_participle": "bozān (बोज़ान / بوزان)",
        "past_stems": {"m_sg": "būz", "m_pl": "būzʲ", "f_sg": "būzi", "f_pl": "būze"},
        "future_stem": "bōzi",
    },
    "shōngun": {
        "infinitive": "shōngun (शोंगुन / شونگُن)",
        "meaning": "to sleep",
        "root": "shong",
        "transitive": False,
        "present_participle": "shongān (शोंगान / شونگان)",
        "past_stems": {"m_sg": "shūt", "m_pl": "shūtʲ", "f_sg": "shūts", "f_pl": "shūtsē"},
        "future_stem": "shōngi",
    },
}

# Pronominal Clitics attached to Kashmiri verbs
PRONOMINAL_CLITICS = {
    "1s": {"clitic": "-(u)m", "meaning": "I / me / by me"},
    "2s": {"clitic": "-(u)th", "meaning": "thou / thee / by thee"},
    "3s": {"clitic": "-(u)n", "meaning": "he / she / him / by him"},
    "1p": {"clitic": "-i", "meaning": "we / us / by us"},
    "2p": {"clitic": "-iv", "meaning": "you (plural) / by you"},
    "3p": {"clitic": "-(a)kh", "meaning": "they / them / by them"},
}

def get_imperative(verb_name: str, is_plural: bool = False) -> str:
    """
    Generate the imperative (command) form of a Kashmiri verb.
    Singular: bare stem (e.g. 'par')
    Plural / Polite: stem + '-iv' (e.g. 'pariv')
    """
    key = verb_name.lower().strip()
    root = VERB_LEXICON[key]["root"] if key in VERB_LEXICON else key.rstrip("un")
    if is_plural:
        return f"{root}iv (पोरिव / پَرِو)"
    return f"{root} (पर / پَر)"

def get_converb(verb_name: str) -> str:
    """
    Generate the conjunctive participle (converb -ith: 'having done/read').
    e.g. 'parith' (having read), 'karith' (having done).
    """
    key = verb_name.lower().strip()
    root = VERB_LEXICON[key]["root"] if key in VERB_LEXICON else key.rstrip("un")
    return f"{root}ith (परिथ / پَرِتھ - having {key.rstrip('un')}ed)"

def conjugate_verb(verb_name: str) -> Dict[str, Any]:
    """Returns the conjugational paradigm for a Kashmiri verb."""
    key = verb_name.lower().strip()
    if key in VERB_LEXICON:
        info = VERB_LEXICON[key]
    else:
        root = key.rstrip("un") if key.endswith("un") else key
        info = {
            "infinitive": f"{root}un",
            "meaning": "custom verb",
            "root": root,
            "transitive": True,
            "present_participle": f"{root}ān",
            "past_stems": {"m_sg": f"{root}yow", "m_pl": f"{root}yeyi", "f_sg": f"{root}yayi", "f_pl": f"{root}yaye"},
            "future_stem": f"{root}i",
        }

    pres_part = info["present_participle"]
    pst = info.get("past_stems", {})

    return {
        "verb_info": info,
        "is_transitive": info.get("transitive", True),
        "present_tense": {
            "1st_sing_masc": f"bɨ chhus {pres_part} (I am reading/doing)",
            "1st_sing_fem": f"bɨ chhes {pres_part}",
            "2nd_sing_masc": f"tsɨ chhukh {pres_part} (Thou art)",
            "2nd_sing_fem": f"tsɨ chhekh {pres_part}",
            "3rd_sing_masc": f"su chhu {pres_part} (He is)",
            "3rd_sing_fem": f"so chhe {pres_part} (She is)",
            "1st_plur": f"əsʲ chhi {pres_part} (We are)",
            "2nd_plur": f"tohʲ chhiv {pres_part} (You are)",
            "3rd_plur": f"tim chhi {pres_part} (They are)",
        },
        "past_tense_agreement": {
            "rule": "Agrees with Object in gender/number (Split-Ergativity)" if info.get("transitive") else "Intransitive (agrees with Subject)",
            "masculine_singular_object": pst.get("m_sg", ""),
            "masculine_plural_object": pst.get("m_pl", ""),
            "feminine_singular_object": pst.get("f_sg", ""),
            "feminine_plural_object": pst.get("f_pl", ""),
        },
        "imperative": {
            "singular": get_imperative(key, is_plural=False),
            "plural_polite": get_imperative(key, is_plural=True),
        },
        "converb": get_converb(key),
        "pronominal_clitics": PRONOMINAL_CLITICS,
    }
