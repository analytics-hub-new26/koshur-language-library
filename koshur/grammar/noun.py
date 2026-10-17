"""
Kashmiri Noun Morphology, Case Declension & Morphophonemics.
Kashmiri features a split-ergative case system with four principal cases:
1. Direct (Absolutive / Nominative)
2. Ergative (Agentive - marks the subject of past transitive verbs)
3. Dative (marks indirect objects, beneficiaries, and experiencer subjects)
4. Ablative (marks source, location, instrument)

Features morphophonemic consonant palatalization (*matsaryar*) and vowel shifts.
"""

from typing import Dict, Any, List

# Paradigm templates for representative noun classes
NOUN_PARADIGMS: Dict[str, Dict[str, Any]] = {
    "larka": { # Masculine ending in short vowel (Class II)
        "lemma": "लड़कॳ / لڑکَہ / larka",
        "noun_class": "Masculine Class II (Vowel-final)",
        "gender": "masculine",
        "singular": {
            "direct": "larkə (लड़कॳ / لڑکَہ)",
            "ergative": "larkan (लड़कन / لڑکَن)",
            "dative": "larkas (लड़कस / لڑکَس)",
            "ablative": "larki (लड़कि / لڑکِ)",
        },
        "plural": {
            "direct": "larkə (लड़कॳ / لڑکَہ)",
            "ergative": "larkav (लड़क्व / لڑکَو)",
            "dative": "larkan (लड़कन / لڑکَن)",
            "ablative": "larkyav (लड़क्यव / لڑکَیو)",
        }
    },
    "kour": { # Feminine consonant-final (Class I)
        "lemma": "कूर / کُوٗر / kōr",
        "noun_class": "Feminine Class I (Consonant-final with palatalization)",
        "gender": "feminine",
        "singular": {
            "direct": "kōr (कूर / کُوٗر)",
            "ergative": "kōri (कूरि / کُوٗرِ)",
            "dative": "kōre (कूरे / کُوٗرے)",
            "ablative": "kōri (कूरि / کُوٗرِ)",
        },
        "plural": {
            "direct": "kōrē (कूरे / کُوٗرے)",
            "ergative": "kōryav (कूय्र्व / کُوٗریَو)",
            "dative": "kōryan (कूय्र्न / کُوٗریَن)",
            "ablative": "kōryav (कूय्र्व / کُوٗریَو)",
        }
    },
    "gur": { # Masculine consonant-final (Class I)
        "lemma": "गुर / گُر / gur",
        "noun_class": "Masculine Class I (Consonant-final with vowel mutation)",
        "gender": "masculine",
        "singular": {
            "direct": "gur (गुर / گُر)",
            "ergative": "guri (गुरि / گُرِ)",
            "dative": "guras (गुरस / گُرَس)",
            "ablative": "guri (गुरि / गُرِ)",
        },
        "plural": {
            "direct": "gərʲ (गॴरʲ / گٲر)",
            "ergative": "guryav (गुय्र्व / گُریَو)",
            "dative": "guryan (गुय्र्न / گُریَن)",
            "ablative": "guryav (गुय्र्व / گُریَو)",
        }
    },
    "tsur": { # Thief (Masculine consonant-final)
        "lemma": "चूर / ژوٗر / tsūr",
        "noun_class": "Masculine Class I (Consonant-final)",
        "gender": "masculine",
        "singular": {
            "direct": "tsūr (चूर / ژوٗر)",
            "ergative": "tsūran (चूरन / ژوٗرَن)",
            "dative": "tsūras (चूरस / ژوٗرَس)",
            "ablative": "tsūri (चूरि / ژوٗرِ)",
        },
        "plural": {
            "direct": "tsīrʲ (चीरʲ / ژیٖر)",
            "ergative": "tsūrav (चूरव / ژوٗرَو)",
            "dative": "tsūran (चूरन / ژوٗرَن)",
            "ablative": "tsūryav (चूरियव / ژوٗریَو)",
        }
    },
    "gaab": { # Ewe / Sheep (Feminine)
        "lemma": "गाब / گاب / gāb",
        "noun_class": "Feminine Class II (-i plural)",
        "gender": "feminine",
        "singular": {
            "direct": "gāb (गाब / گاب)",
            "ergative": "gābi (गाबि / گابِ)",
            "dative": "gābe (गाबे / گابے)",
            "ablative": "gābi (गाबि / گابِ)",
        },
        "plural": {
            "direct": "gābi (गाबि / گابِ)",
            "ergative": "gābyav (गाब्यव / گابیَو)",
            "dative": "gābyan (गाब्यन / گابیَن)",
            "ablative": "gābyav (गाब्यव / گابیَو)",
        }
    },
    "khandaren": { # Wife (Feminine Class III in -en)
        "lemma": "ख़ानदारेन / خاندارؠن / khāndāren",
        "noun_class": "Feminine Class III (Kinship suffix -en)",
        "gender": "feminine",
        "singular": {
            "direct": "khāndāren (ख़ानदारेन / خاندارؠن)",
            "ergative": "khāndāreni (ख़ानदारेनि / خاندارؠنِ)",
            "dative": "khāndārene (ख़ानदारेने / خاندارؠنے)",
            "ablative": "khāndāreni (ख़ानदारेनि / خاندارؠنِ)",
        },
        "plural": {
            "direct": "khāndāren (ख़ानदारेन / خاندارؠن)",
            "ergative": "khāndārenyav (ख़ानदारेन्यव / خاندارؠنیَو)",
            "dative": "khāndārenyan (ख़ानदारेन्यन / خاندارؠنیَن)",
            "ablative": "khāndārenyav (ख़ानदारेन्यव / خاندارؠنیَو)",
        }
    }
}

def form_plural(noun: str, gender: str = "masculine") -> str:
    """
    Generate the direct plural form of a Kashmiri noun applying
    phonological rules and palatalization.
    """
    key = noun.lower().strip()
    if key in NOUN_PARADIGMS:
        return NOUN_PARADIGMS[key]["plural"]["direct"]

    if gender == "feminine":
        # Feminine consonant-final -> suffix -ē
        if not noun.endswith(("a", "i", "e", "u")):
            return noun + "ē"
        return noun
    else:
        # Masculine: short vowel final remains unchanged;
        # Consonant final often mutates vowel u -> ə or undergoes palatalization
        if noun.endswith(("a", "ə")):
            return noun
        if "u" in noun:
            return noun.replace("u", "ə") + "ʲ"
        return noun

def decline_noun(noun: str, gender: str = "masculine") -> Dict[str, Any]:
    """
    Returns declension paradigm for a noun across all four cases.
    If the noun is in the predefined paradigm lexicon, returns its exact forms.
    Otherwise, generates rule-based Kashmiri declensions.
    """
    key = noun.lower().strip()
    if key in NOUN_PARADIGMS:
        return NOUN_PARADIGMS[key]

    # Rule-based declension generator
    stem = noun
    if gender == "feminine":
        pl_dir = form_plural(noun, "feminine")
        return {
            "lemma": noun,
            "noun_class": "Feminine (Rule-generated)",
            "gender": "feminine",
            "singular": {
                "direct": stem,
                "ergative": stem + "i",
                "dative": stem + "e",
                "ablative": stem + "i",
            },
            "plural": {
                "direct": pl_dir,
                "ergative": stem + "yav",
                "dative": stem + "yan",
                "ablative": stem + "yav",
            }
        }
    else:
        pl_dir = form_plural(noun, "masculine")
        return {
            "lemma": noun,
            "noun_class": "Masculine (Rule-generated)",
            "gender": "masculine",
            "singular": {
                "direct": stem,
                "ergative": stem + "an",
                "dative": stem + "as",
                "ablative": stem + "i",
            },
            "plural": {
                "direct": pl_dir,
                "ergative": stem + "av",
                "dative": stem + "an",
                "ablative": stem + "yav",
            }
        }
