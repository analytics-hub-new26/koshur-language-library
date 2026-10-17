"""
Corpus & Dataset Exporters for Computational Linguistics & Digital Humanities.
Supports:
1. CoNLL-U format (Universal Dependencies standard for parsing and NLP training).
2. TEI-XML format (Text Encoding Initiative standard for digital scholarly archives).
3. JSON-LD format (W3C Linked Open Data OntoLex-Lemon schema).
"""

from typing import List, Dict, Any, Optional
import xml.etree.ElementTree as ET
import json

def export_conllu(sentences: List[Dict[str, Any]], filepath: Optional[str] = None) -> str:
    """
    Export annotated Kashmiri sentences into Universal Dependencies CoNLL-U format.

    Each sentence is a dict with:
        'sent_id': str,
        'text': str,
        'tokens': List[Dict] with fields:
            'id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc'
    """
    lines = []
    for sent in sentences:
        lines.append(f"# sent_id = {sent.get('sent_id', 'sent_1')}")
        lines.append(f"# text = {sent.get('text', '')}")
        tokens = sent.get("tokens", [])
        for tok in tokens:
            t_id = str(tok.get("id", 1))
            t_form = tok.get("form", "_")
            t_lemma = tok.get("lemma", "_")
            t_upos = tok.get("upos", "_")
            t_xpos = tok.get("xpos", "_")
            t_feats = tok.get("feats", "_")
            t_head = str(tok.get("head", 0))
            t_deprel = tok.get("deprel", "_")
            t_deps = tok.get("deps", "_")
            t_misc = tok.get("misc", "_")
            lines.append(f"{t_id}\t{t_form}\t{t_lemma}\t{t_upos}\t{t_xpos}\t{t_feats}\t{t_head}\t{t_deprel}\t{t_deps}\t{t_misc}")
        lines.append("")

    content = "\n".join(lines)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return content

def export_tei_xml(entries: List[Dict[str, Any]], title: str = "Koshur Lexicon", filepath: Optional[str] = None) -> str:
    """
    Export lexicon entries to Text Encoding Initiative (TEI-XML) P5 format for digital lexicography.
    """
    root = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")

    # Header
    teiHeader = ET.SubElement(root, "teiHeader")
    fileDesc = ET.SubElement(teiHeader, "fileDesc")
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    t = ET.SubElement(titleStmt, "title")
    t.text = title
    publicationStmt = ET.SubElement(fileDesc, "publicationStmt")
    p = ET.SubElement(publicationStmt, "p")
    p.text = "Koshur Computational Linguistics Toolkit"
    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    p_src = ET.SubElement(sourceDesc, "p")
    p_src.text = "Indigenous Kashmiri linguistic tradition and scholarship"

    # Text Body
    text = ET.SubElement(root, "text")
    body = ET.SubElement(text, "body")
    entry_list = ET.SubElement(body, "entryFree")

    for e in entries:
        entry_elem = ET.SubElement(entry_list, "entry")
        # Form
        form = ET.SubElement(entry_elem, "form", type="lemma")
        orth_rom = ET.SubElement(form, "orth", type="latin")
        orth_rom.text = e.get("roman", e.get("lemma", ""))
        orth_deva = ET.SubElement(form, "orth", type="devanagari")
        orth_deva.text = e.get("devanagari", "")
        orth_arab = ET.SubElement(form, "orth", type="persoarabic")
        orth_arab.text = e.get("persoarabic", "")
        orth_shrd = ET.SubElement(form, "orth", type="sharada")
        orth_shrd.text = e.get("sharada", "")

        # Grammar
        gramGrp = ET.SubElement(entry_elem, "gramGrp")
        pos = ET.SubElement(gramGrp, "pos")
        pos.text = e.get("pos", "noun")

        # Sense
        sense = ET.SubElement(entry_elem, "sense")
        def_en = ET.SubElement(sense, "def", lang="en")
        def_en.text = e.get("meaning_en", "")
        def_hi = ET.SubElement(sense, "def", lang="hi")
        def_hi.text = e.get("meaning_hi", "")

        # Etymology
        if e.get("etymology"):
            etym = ET.SubElement(entry_elem, "etym")
            etym.text = e.get("etymology")

    xml_str = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_str)
    return xml_str

def export_jsonld(entries: List[Dict[str, Any]], filepath: Optional[str] = None) -> str:
    """
    Export lexicon entries to W3C JSON-LD Linked Data standard (OntoLex-Lemon ontology).
    """
    graph = []
    for e in entries:
        item = {
            "@id": f"urn:koshur:lexicon:{e.get('lemma', '').replace(' ', '_')}",
            "@type": "ontolex:LexicalEntry",
            "canonicalForm": {
                "@type": "ontolex:Form",
                "writtenRep": [
                    {"@value": e.get("roman", ""), "@language": "ks-Latn"},
                    {"@value": e.get("devanagari", ""), "@language": "ks-Deva"},
                    {"@value": e.get("persoarabic", ""), "@language": "ks-Arab"},
                    {"@value": e.get("sharada", ""), "@language": "ks-Shrd"},
                ]
            },
            "partOfSpeech": e.get("pos", "noun"),
            "sense": {
                "@type": "ontolex:LexicalSense",
                "definition": [
                    {"@value": e.get("meaning_en", ""), "@language": "en"},
                    {"@value": e.get("meaning_hi", ""), "@language": "hi"},
                ]
            },
            "etymology": e.get("etymology", "")
        }
        graph.append(item)

    data = {
        "@context": {
            "ontolex": "http://www.w3.org/ns/lemon/ontolex#",
            "lexinfo": "http://www.lexinfo.net/ontology/3.0/lexinfo#",
            "writtenRep": "ontolex:writtenRep",
            "canonicalForm": "ontolex:canonicalForm",
            "partOfSpeech": "lexinfo:partOfSpeech",
            "sense": "ontolex:sense",
            "definition": "http://www.w3.org/2004/02/skos/core#definition"
        },
        "@graph": graph
    }

    res = json.dumps(data, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(res)
    return res
