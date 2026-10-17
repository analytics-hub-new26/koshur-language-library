"""
Leipzig Glossing Rules Engine for Kashmiri Linguistic Fieldwork & Research.
Follows the international Leipzig Glossing Rules standard established by the
Max Planck Institute for Evolutionary Anthropology and Department of Linguistics.

Generates interlinear morpheme-by-morpheme glosses in:
- Plain Text (standard 3-line interlinear format)
- LaTeX format using the standard `gb4e` / `covington` / `expex` macros (\\gll)
- Markdown Table format for academic papers and digital humanities reports.
"""

from typing import List, Dict, Any, Optional

GLOSSING_TAGS: Dict[str, str] = {
    # Cases
    "NOM": "Nominative (Direct / Absolutive)",
    "ERG": "Ergative (Agent of past transitive verb)",
    "DAT": "Dative (Recipient / experiencer subject)",
    "ABL": "Ablative (Source / origin / instrument)",
    "GEN": "Genitive (Possession / relation)",
    "LOC": "Locative (Location in space/time)",
    "VOC": "Vocative (Direct address)",

    # Gender & Number
    "M": "Masculine",
    "F": "Feminine",
    "SG": "Singular",
    "PL": "Plural",

    # Person
    "1": "First Person",
    "2": "Second Person",
    "3": "Third Person",

    # Tense, Aspect, Mood
    "PRS": "Present Tense",
    "PST": "Past Tense",
    "FUT": "Future Tense",
    "IPFV": "Imperfective Aspect",
    "PFV": "Perfective Aspect",
    "PROG": "Progressive Aspect",
    "COND": "Conditional Mood",
    "IMP": "Imperative Mood",
    "INF": "Infinitive",
    "PTCP": "Participle",
    "CVB": "Converb / Conjunctive Participle (-ith)",

    # Kashmiri Specialized Typological Markers
    "V2": "Verb-Second Clitic Placement",
    "CLIT": "Pronominal Clitic Suffix",
    "HON": "Honorific Particle (e.g. haz)",
    "REFL": "Reflexive Pronoun (pana)",
    "NEG": "Negative Particle (na / ne)",
    "Q": "Interrogative Marker (e.g. -ā)",
    "COP": "Copula / Auxiliary (chhu / os)",
}

def generate_leipzig_gloss(
    source_words: List[str],
    gloss_tokens: List[str],
    free_translation: str,
    output_format: str = "text"
) -> str:
    """
    Generate standard interlinear gloss following Leipzig rules.

    Parameters:
        source_words: List of source words / morphemes (e.g. ['aslam-an', 'por', 'akhavbar'])
        gloss_tokens: Morpheme gloss tags (e.g. ['Aslam-ERG', 'read.PST.M.SG', 'newspaper.NOM.M.SG'])
        free_translation: Idiomatic translation (e.g. 'Aslam read the newspaper.')
        output_format: 'text', 'latex', or 'markdown'
    """
    if len(source_words) != len(gloss_tokens):
        # Pad shorter list to avoid alignment breaks
        max_len = max(len(source_words), len(gloss_tokens))
        while len(source_words) < max_len:
            source_words.append("?")
        while len(gloss_tokens) < max_len:
            gloss_tokens.append("?")

    fmt = output_format.lower().strip()

    if fmt == "latex":
        src_line = " ".join(source_words)
        gls_line = " ".join(gloss_tokens)
        return f"""\\begin{{exe}}
\\ex
\\gll {src_line} \\\\
     {gls_line} \\\\
\\glt `{free_translation}'
\\end{{exe}}"""

    elif fmt == "markdown":
        header_src = " | ".join(source_words)
        header_gls = " | ".join(gloss_tokens)
        separators = " | ".join(["---"] * len(source_words))
        return f"""| {header_src} |
| {separators} |
| {header_gls} |

*Translation:* "{free_translation}"
"""

    else: # Plain Text
        col_widths = [max(len(w), len(g)) + 2 for w, g in zip(source_words, gloss_tokens)]
        line1 = "".join(w.ljust(cw) for w, cw in zip(source_words, col_widths)).rstrip()
        line2 = "".join(g.ljust(cw) for g, cw in zip(gloss_tokens, col_widths)).rstrip()
        line3 = f"'{free_translation}'"
        return f"{line1}\n{line2}\n{line3}"

def get_gloss_tag_description(tag: str) -> Optional[str]:
    """Retrieve official linguistic definition of a Leipzig glossing abbreviation."""
    return GLOSSING_TAGS.get(tag.upper().strip(), None)
