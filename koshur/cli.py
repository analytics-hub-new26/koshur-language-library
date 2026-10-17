"""
Command Line Interface (CLI) for Koshur:
Computational Linguistics, Web Application & Digital Preservation Toolkit
for the Kashmiri Language (कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳).

Usage Examples:
    koshur transliterate "व्यथ्" --to sharada
    koshur lookup "pheran"
    koshur search "tea" --tag cuisine
    koshur i18n --script devanagari --all
    koshur i18n --export app_locales.json --script persoarabic
    koshur date --script devanagari
    koshur date --relative -3600 --script persoarabic
    koshur keyboard --type "koshur chhu asul" --to devanagari
    koshur webfonts
    koshur gloss "aslam-an por akhavbar" --gloss "Aslam-ERG read.PST newspaper.NOM" --trans "Aslam read the newspaper"
    koshur metrics "अमी पनॳ सोदरस नावि छस लमान।"
    koshur proverb --random
    koshur revenue --term jamabandi
    koshur area --kanals 2 --marlas 10
    koshur number 42 --script devanagari
    koshur dialect kishtwari
    koshur compare "brother"
    koshur grammar --noun "gur"
    koshur grammar --verb "parun"
    koshur phonology --ipa "कॉशुर"
    koshur version
"""

import sys
import argparse
import json

# Ensure UTF-8 output on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import koshur
from koshur.grammar.stemmer import stem_word
from koshur.phonology.vowels import KASHMIRI_VOWEL_INVENTORY
from koshur.nlp.analyzer import analyze_text

def main():
    parser = argparse.ArgumentParser(
        prog="koshur",
        description="Koshur: Computational Linguistics, App Development & Preservation Toolkit for Kashmiri (कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Transliterate command
    trans_p = subparsers.add_parser("transliterate", help="Transliterate text between scripts (Sharada, Devanagari, Perso-Arabic, Latin)")
    trans_p.add_argument("text", help="Text to transliterate")
    trans_p.add_argument("--to", required=True, choices=["sharada", "devanagari", "persoarabic", "latin"], help="Target script")

    # Lookup command
    lookup_p = subparsers.add_parser("lookup", help="Look up a Kashmiri word with multi-stage fuzzy matching")
    lookup_p.add_argument("word", help="Word to look up")

    # Search command
    search_p = subparsers.add_parser("search", help="Search the dictionary across translations, tags, and derivations")
    search_p.add_argument("query", nargs="?", default="", help="Query keyword")
    search_p.add_argument("--tag", type=str, default=None, help="Filter by semantic tag (e.g. ui, web, cuisine, geography, literature)")

    # i18n Web & UI Localization
    i18n_p = subparsers.add_parser("i18n", help="UI localization strings for websites and mobile applications")
    i18n_p.add_argument("--key", type=str, help="Specific UI string key (e.g. home, search, save, login)")
    i18n_p.add_argument("--script", choices=["devanagari", "persoarabic", "sharada", "roman", "english"], default="devanagari", help="Target script")
    i18n_p.add_argument("--all", action="store_true", help="List all UI localization strings")
    i18n_p.add_argument("--export", type=str, help="Export JSON dictionary to file path for react-i18next / vue-i18n")

    # Date and Calendar
    date_p = subparsers.add_parser("date", help="Kashmiri date, calendar and relative time formatting")
    date_p.add_argument("--script", choices=["devanagari", "persoarabic", "sharada", "roman"], default="devanagari", help="Target script")
    date_p.add_argument("--traditional", action="store_true", help="Use traditional Saptrishi/Navreh solar-lunar calendar")
    date_p.add_argument("--relative", type=float, help="Format relative time from seconds offset (e.g. -3600 for 1h ago)")

    # Keyboard & Phonetic Typing
    kb_p = subparsers.add_parser("keyboard", help="Virtual keyboard layouts and real-time phonetic typing")
    kb_p.add_argument("--type", dest="type_text", type=str, help="Transcribe ASCII QWERTY typing into Kashmiri script in real time")
    kb_p.add_argument("--to", choices=["devanagari", "persoarabic", "sharada"], default="devanagari", help="Target script")
    kb_p.add_argument("--layout", choices=["devanagari", "persoarabic", "sharada"], help="Display on-screen keyboard key layout rows")
    kb_p.add_argument("--script", choices=["devanagari", "persoarabic", "sharada"], help="Convenience alias for layout or transcription")

    # Webfonts helper
    wf_p = subparsers.add_parser("webfonts", help="Output CSS @font-face and typography stylesheets for web developers")
    wf_p.add_argument("--script", choices=["devanagari", "persoarabic", "sharada"], help="Filter font CSS for specific script")

    # Research: Interlinear Leipzig Glossing
    gloss_p = subparsers.add_parser("gloss", help="Generate linguistic interlinear gloss (Leipzig rules)")
    gloss_p.add_argument("source", help="Source Kashmiri sentence words (space-separated)")
    gloss_p.add_argument("--gloss", required=True, help="Morpheme gloss tags (space-separated, e.g. 'Aslam-ERG read.PST book.NOM')")
    gloss_p.add_argument("--trans", required=True, help="Free translation in English")
    gloss_p.add_argument("--format", choices=["text", "latex", "markdown"], default="text", help="Output formatting")

    # Research: Quantitative Metrics
    met_p = subparsers.add_parser("metrics", help="Compute quantitative corpus statistics (TTR, hapax, syllables, V2 check)")
    met_p.add_argument("text", help="Text or corpus excerpt to evaluate")

    # Research: Bibliographic & Historical Sources
    src_p = subparsers.add_parser("sources", help="List and search academic and historical research books powering Koshur")
    src_p.add_argument("--search", type=str, help="Search research sources by author, title or keyword")
    src_p.add_argument("--all", action="store_true", help="Display all bibliographic source details")

    # Digital Library command
    lib_p = subparsers.add_parser("library", help="Access the digital library of downloaded books, catalogues, discourses, and papers")
    lib_p.add_argument("--stats", action="store_true", help="Display summary corpus statistics")
    lib_p.add_argument("--category", choices=["books", "catalogues", "discourses", "papers"], help="Filter items by category")
    lib_p.add_argument("--level", choices=["elementary", "intermediate", "advanced"], help="Filter items by learning progression level (elementary, intermediate, advanced)")
    lib_p.add_argument("--info", type=str, help="Display detailed metadata for a specific volume by ID or filename")
    lib_p.add_argument("--read", type=str, help="Read/preview text from a downloaded volume by ID or filename")
    lib_p.add_argument("--chars", type=int, default=1000, help="Number of characters to read with --read (default: 1000)")
    lib_p.add_argument("--search", type=str, help="Full-text keyword search across all 3.34M+ words in downloaded library")

    # Proverb command
    prov_p = subparsers.add_parser("proverb", help="Display or search Kashmiri proverbs (Kahan / Masal)")
    prov_p.add_argument("--random", action="store_true", help="Display a random proverb")
    prov_p.add_argument("--search", type=str, help="Search proverbs by keyword")
    prov_p.add_argument("--all", action="store_true", help="List all proverbs")

    # Revenue record command
    rev_p = subparsers.add_parser("revenue", help="Look up J&K land revenue records terminology, deeds, and cadastral registers")
    rev_p.add_argument("--term", type=str, help="Revenue term to look up (e.g. jamabandi, khasra, bainama, malik_ala)")
    rev_p.add_argument("--search", type=str, help="Search revenue terms by keyword in English, Urdu, or Hindi")
    rev_p.add_argument("--category", type=str, help="Filter terms by category (e.g. Deed, Register, Tenure, Administration)")
    rev_p.add_argument("--list", action="store_true", help="List all cataloged revenue terms and categories")

    # Shikasta command
    shik_p = subparsers.add_parser("shikasta", help="Khat-i-Shikast palaeography, cursive ligature rules, scribal abbreviations & traditional units")
    shik_p.add_argument("--rules", action="store_true", help="List all Shikasta cursive ligature rules")
    shik_p.add_argument("--rule", type=str, help="Explain a specific Shikasta letter rule (e.g. alif, dal_series, re_series, seen_sheen, kaaf_gaaf, meem, he_variants)")
    shik_p.add_argument("--abbrevs", action="store_true", help="List common court & scribal abbreviations used in Shikasta documents")
    shik_p.add_argument("--abbrev", type=str, help="Look up a specific scribal abbreviation (e.g. al_abd, marqooma, faqat, dastkhat, naql_mutabiq_asl)")
    shik_p.add_argument("--weight", nargs="+", help="Convert traditional weights (e.g. --weight 10 tolas, --weight 2 sers, --weight 1 maund)")
    shik_p.add_argument("--currency", nargs="+", help="Format traditional currency (e.g. --currency 10 8 2 for 10 Rs 8 Annas 2 Paisas)")
    shik_p.add_argument("--fasli", action="store_true", help="Display current Fasli crop/revenue calendar year and conversion")

    # Land Area converter
    area_p = subparsers.add_parser("area", help="Convert J&K traditional land units (Kanal, Marla, Sersai, Ghumaon)")
    area_p.add_argument("--kanals", type=float, default=0.0, help="Number of Kanals")
    area_p.add_argument("--marlas", type=float, default=0.0, help="Number of Marlas")
    area_p.add_argument("--sersai", type=float, default=0.0, help="Number of Sersai")

    # Number command
    num_p = subparsers.add_parser("number", help="Convert integer to Kashmiri words")
    num_p.add_argument("value", type=int, help="Integer to convert")
    num_p.add_argument("--script", choices=["roman", "devanagari", "persoarabic"], default="roman", help="Output script")

    # Dialect command
    dial_p = subparsers.add_parser("dialect", help="Information on regional dialects (Kishtwari, Poguli, Siraji, Rambani)")
    dial_p.add_argument("name", help="Dialect name")

    # Compare dialects command
    comp_p = subparsers.add_parser("compare", help="Compare lexical items across Kashmiri dialects")
    comp_p.add_argument("concept", help="Concept or word to compare across dialects")

    # Grammar command
    gram_p = subparsers.add_parser("grammar", help="Kashmiri grammar engine (syntax, noun declension, verb conjugation)")
    gram_p.add_argument("--noun", type=str, help="Decline a noun")
    gram_p.add_argument("--gender", choices=["masculine", "feminine"], default="masculine", help="Gender for noun")
    gram_p.add_argument("--verb", type=str, help="Conjugate a verb")
    gram_p.add_argument("--syntax", type=str, help="Analyze V2 syntax for a space-separated clause")
    gram_p.add_argument("--stem", type=str, help="Morphologically stem a word")

    # Phonology command
    phon_p = subparsers.add_parser("phonology", help="Kashmiri phonetics, IPA, and vowel inventory")
    phon_p.add_argument("--ipa", type=str, help="Convert text to IPA phonetic transcription")
    phon_p.add_argument("--vowels", action="store_true", help="Display the 16-vowel inventory table")

    # Analyze command
    ana_p = subparsers.add_parser("analyze", help="Analyze linguistic statistics of a Kashmiri text")
    ana_p.add_argument("text", help="Text to analyze")

    # Folklore and Songs command
    folk_p = subparsers.add_parser("folklore", help="Kashmiri folklore genres, musical traditions, and authentic folk songs")
    folk_p.add_argument("--genre", type=str, help="Display specific folklore genre (e.g. wanvun, rouf, chakri, ladishah)")
    folk_p.add_argument("--genres", action="store_true", help="List all Kashmiri folklore and musical genres")
    folk_p.add_argument("--song", type=str, help="Display authentic song details, lyrics across 4 scripts, and translation")
    folk_p.add_argument("--songs", action="store_true", help="List all cataloged traditional songs and lyrics")
    folk_p.add_argument("--search", type=str, help="Search songs by poet, title, or lyric keyword")

    # Local Deities & Sacred Pantheon command
    deity_p = subparsers.add_parser("deity", help="Kashmiri sacred pantheon, Nilamata Nagas, Shakta Peethas, and Ashta Bhairavas")
    deity_p.add_argument("--name", type=str, help="Look up a deity, tirtha, or sacred spring by name (e.g. sharika, ragnya, nilanag)")
    deity_p.add_argument("--bhairavas", action="store_true", help="Display the Ashta Bhairavas (8 directional guardian protectors of Srinagar)")
    deity_p.add_argument("--all", action="store_true", help="List all cataloged deities and sacred tirthas")

    # Translation and Decipherment of Government Records
    for cmd_name in ["translate-record", "record-translate"]:
        trans_rec_p = subparsers.add_parser(cmd_name, help="Translate & decipher J&K government land records, deeds, and archival documents to English/Hindi")
        trans_rec_p.add_argument("--text", type=str, help="Raw document text in Urdu, Shikasta, or Kashmiri")
        trans_rec_p.add_argument("--file", type=str, help="Path to document file (Image: PNG/JPG/TIFF/WEBP, PDF, or Plain Text)")
        trans_rec_p.add_argument("--sample", type=str, help="Run on built-in archival specimen ID (e.g. jamabandi_shalimar, bainama_pampore, intiqal_virasat, rahannama_baramulla, arzi_dawa_anantnag)")
        trans_rec_p.add_argument("--lang", choices=["en", "hi", "both"], default="en", help="Target translation language: 'en' for English, 'hi' for Hindi, 'both' for dual (default: en)")
        trans_rec_p.add_argument("--list-samples", action="store_true", help="List all available archival sample records")
        trans_rec_p.add_argument("--json", action="store_true", help="Output complete structured translation and entity extraction as JSON")
        trans_rec_p.add_argument("--html", action="store_true", help="Output printable HTML translation certificate")
        trans_rec_p.add_argument("--output", type=str, help="Write translation output (Markdown, JSON, or HTML) to specified file")
        trans_rec_p.add_argument("--serve", action="store_true", help="Launch interactive web application server")
        trans_rec_p.add_argument("--port", type=int, default=8080, help="HTTP server port if using --serve (default: 8080)")
        trans_rec_p.add_argument("--host", type=str, default="127.0.0.1", help="HTTP server host if using --serve (default: 127.0.0.1)")
        trans_rec_p.add_argument("--no-browser", action="store_true", help="Do not automatically open browser with --serve")

    # Web application command
    web_rec_p = subparsers.add_parser("translator-web", help="Launch interactive web application for government records translation and decipherment")
    web_rec_p.add_argument("--port", type=int, default=8080, help="HTTP server port (default: 8080)")
    web_rec_p.add_argument("--host", type=str, default="127.0.0.1", help="HTTP server host (default: 127.0.0.1)")
    web_rec_p.add_argument("--no-browser", action="store_true", help="Do not automatically open browser")

    # Version command
    subparsers.add_parser("version", help="Show version information")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "version":
        print(f"Koshur toolkit version: {koshur.__version__}")
        print("Author: Koshur Preservation Initiative")
        print("Preserving the Kashmiri language (कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳)")

    elif args.command == "translate-record":
        from koshur.translator import (
            translate_record,
            translate_record_file,
            get_sample_record,
            list_sample_records
        )
        if args.list_samples:
            samples = list_sample_records()
            print(f"=== Available J&K Archival Government Records ({len(samples)} specimens) ===")
            for s in samples:
                print(f"  • {s['id']:<24} [{s['doc_type']:<12}] {s['title']}")
                print(f"    Jurisdiction: {s.get('village', '')}, {s.get('tehsil', '')}, {s.get('district', '')} | Era: {s.get('date_fasli', '')} / {s.get('date_gregorian', '')}")
            return

        result = None
        if args.sample:
            s_data = get_sample_record(args.sample)
            if not s_data:
                print(f"Error: Unknown sample record '{args.sample}'. Use --list-samples to view available records.")
                return
            result = translate_record(s_data["urdu_text"], doc_id=args.sample)
        elif args.file:
            result = translate_record_file(args.file)
        elif args.text:
            result = translate_record(args.text)
        else:
            print("Please specify an input: --text '...', --file <path>, or --sample <id>. Run --list-samples to see examples.")
            return

        if args.json:
            output_str = json.dumps(result, indent=2, ensure_ascii=False)
        elif args.html:
            output_str = result.get("certified_html", "")
        else:
            output_str = result.get("markdown", "")

        if args.output:
            with open(args.output, "w", encoding="utf-8") as out_f:
                out_f.write(output_str)
            print(f"Translation successfully saved to: {args.output}")
        else:
            print(output_str)

    elif args.command == "translator-web":
        from koshur.translator.web_app import start_server
        start_server(host=args.host, port=args.port, open_browser=not args.no_browser)

    elif args.command == "transliterate":
        out = koshur.transliterate(args.text, target_script=args.to)
        print(f"Input:         {args.text}")
        print(f"Detected:      {koshur.detect_script(args.text)}")
        print(f"Output ({args.to}): {out}")

    elif args.command == "lookup":
        res = koshur.lookup(args.word)
        if res:
            print("=== Word Found ===")
            print(f"Lemma:        {res['lemma']}")
            print(f"Roman:        {res['roman']}")
            print(f"Devanagari:   {res['devanagari']}")
            print(f"Perso-Arabic: {res['persoarabic']}")
            print(f"Sharada:      {res['sharada']}")
            print(f"Part of Speech: {res.get('pos', 'N/A')}")
            print(f"English:      {res['meaning_en']}")
            print(f"Hindi:        {res['meaning_hi']}")
            print(f"Etymology:    {res.get('etymology', 'N/A')}")
            print(f"Tags:         {', '.join(res.get('tags', []))}")
        else:
            print(f"Word '{args.word}' not found directly. Searching partial matches...")
            matches = koshur.search_words(args.word)
            if matches:
                print(f"Found {len(matches)} matches:")
                for m in matches:
                    print(f"- {m['lemma']} ({m['devanagari']} / {m['persoarabic']}): {m['meaning_en']}")
            else:
                print("No matches found.")

    elif args.command == "search":
        matches = koshur.search_words(args.query, tag=args.tag)
        tag_str = f" in tag '{args.tag}'" if args.tag else ""
        print(f"Found {len(matches)} match(es){tag_str}:")
        for m in matches[:25]:
            print(f"- {m['lemma']} | {m['devanagari']} | {m['persoarabic']} | {m['sharada']}")
            print(f"  English: {m['meaning_en']}")
            print(f"  Hindi:   {m['meaning_hi']}")
        if len(matches) > 25:
            print(f"... and {len(matches) - 25} more entries.")

    elif args.command == "i18n":
        if args.export:
            koshur.export_i18n_json(script=args.script, filepath=args.export)
            print(f"Exported {len(koshur.get_all_ui_keys())} UI strings to: {args.export} ({args.script})")
        elif args.key:
            val = koshur.get_ui_string(args.key, script=args.script)
            print(f"[{args.key}] ({args.script}): {val}")
        elif args.all:
            print(f"=== Koshur UI Localization Strings ({args.script}) ===")
            print(f"{'Key':<20} {'Translation':<30} {'English Fallback'}")
            print("-" * 75)
            for k in koshur.get_all_ui_keys():
                val = koshur.get_ui_string(k, script=args.script)
                en = koshur.get_ui_string(k, script="english")
                print(f"{k:<20} {val:<30} {en}")
        else:
            print("Please specify --key <KEY>, --all, or --export <FILE>.")

    elif args.command == "date":
        if args.relative is not None:
            rel = koshur.format_relative_time(args.relative, script=args.script)
            print(f"Relative time ({args.relative}s) in {args.script}: {rel}")
        else:
            formatted = koshur.format_date(script=args.script, traditional=args.traditional)
            cal_name = "Traditional Saptrishi/Navreh" if args.traditional else "Gregorian"
            print(f"Current Date ({cal_name} / {args.script}): {formatted}")

    elif args.command == "keyboard":
        target = args.script or args.to or "devanagari"
        if args.type_text:
            out = koshur.transcribe_keystrokes(args.type_text, target_script=target)
            print(f"Typed (ASCII):  {args.type_text}")
            print(f"Output ({target}): {out}")
        else:
            layout_script = args.layout or args.script or "devanagari"
            layout = koshur.get_keyboard_layout(layout_script)
            print(f"=== {layout['name']} (Direction: {layout['direction']}) ===")
            for row_idx, row in enumerate(layout['rows'], 1):
                print(f"Row {row_idx}: {' '.join(row)}")

    elif args.command == "webfonts":
        full_css = koshur.generate_webfont_css(include_cdn=True)
        if args.script:
            print(f"/* Koshur WebFont CSS for {args.script} */")
            if args.script == "sharada":
                print("@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Sharada&display=swap');")
                print(".koshur-sharada { font-family: 'Noto Sans Sharada', sans-serif; direction: ltr; }")
            elif args.script == "persoarabic":
                print("@import url('https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;700&display=swap');")
                print(".koshur-persoarabic { font-family: 'Noto Naskh Arabic', 'Urdu Typesetting', serif; direction: rtl; }")
            else:
                print("@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&display=swap');")
                print(".koshur-devanagari { font-family: 'Noto Sans Devanagari', sans-serif; direction: ltr; }")
        else:
            print(full_css)

    elif args.command == "gloss":
        src_tokens = args.source.split()
        gls_tokens = args.gloss.split()
        res = koshur.generate_leipzig_gloss(src_tokens, gls_tokens, args.trans, output_format=args.format)
        print(f"=== Interlinear Leipzig Gloss ({args.format}) ===")
        print(res)

    elif args.command == "metrics":
        stats = koshur.compute_lexical_metrics(args.text)
        v2 = koshur.verify_v2_word_order(args.text)
        print("=== Corpus Lexical Metrics ===")
        print(f"Total Tokens:           {stats['tokens']}")
        print(f"Total Unique Types:     {stats['types']}")
        print(f"Type-Token Ratio (TTR): {stats['ttr']}")
        print(f"Root TTR (Guiraud):     {stats['root_ttr']}")
        print(f"Hapax Legomena:         {stats['hapax_count']} ({stats['hapax_ratio']*100:.1f}%)")
        print(f"Avg Word Length:        {stats['avg_word_length']} characters")
        print(f"Avg Syllables/Word:     {stats['avg_syllables_per_word']}")
        print("\n=== Syntactic Analysis ===")
        print(f"V2 Compliant:           {v2['is_v2_compliant']}")
        print(f"Explanation:            {v2['explanation']}")

    elif args.command == "sources":
        if args.search:
            sources = koshur.search_research_sources(args.search)
            print(f"Found {len(sources)} source(s) matching '{args.search}':")
        else:
            sources = koshur.get_research_sources()
            print(f"=== Koshur Primary Academic & Historical Research Sources ({len(sources)} total) ===")
        for s in sources:
            print(f"\n[{s['year']}] {s['title']}")
            print(f"  Authors:   {', '.join(s['authors'])}")
            print(f"  Publisher: {s['publisher']}")
            print(f"  Summary:   {s['description']}")
            if 'archive_id' in s:
                print(f"  Archive:   https://archive.org/details/{s['archive_id']}")
            if 'local_source' in s:
                print(f"  Local Ref: {s['local_source']}")
            if 'local_file' in s:
                print(f"  Downloaded: library/{s['local_file']}")

    elif args.command == "library":
        if args.stats:
            st = koshur.get_library_stats()
            print("=== Koshur Digital Linguistics Library Corpus Stats ===")
            print(f"Total Volumes:       {st['total_volumes']}")
            print(f"Total Corpus Words:  {st['total_words']:,d}")
            print(f"Total Characters:    {st['total_characters']:,d}")
            print("Category Breakdown:")
            for cat, cnt in st.get("category_counts", {}).items():
                print(f"  - {cat.title():<12}: {cnt} volumes")
            if "level_counts" in st and st["level_counts"]:
                print("Learning Progression Levels:")
                for lvl, cnt in st["level_counts"].items():
                    print(f"  - {lvl.title():<12}: {cnt} volumes")
        elif args.level:
            cat = koshur.get_library_catalog()
            items = [i for i in cat.get("items", []) if i.get("level", "").lower() == args.level.lower()]
            desc = cat.get("learning_levels", {}).get(args.level.lower(), "")
            print(f"=== Koshur Learning Progression: {args.level.title()} Level ({len(items)} volumes) ===")
            if desc:
                print(f"Curriculum Focus: {desc}\n")
            for i in items:
                wc = f"({i['word_count']:,d} words)" if "word_count" in i else "(Catalog)"
                print(f"• [{i.get('id')}] {i.get('title')}")
                print(f"    Author: {i.get('author', 'Unknown')} ({i.get('year')}) | {wc}")
                print(f"    Summary: {i.get('description')}\n")
        elif args.info:
            cat = koshur.get_library_catalog()
            found = False
            target = args.info.strip().lower()
            for item in cat.get("items", []):
                if target == item.get("id", "").lower() or target in item.get("title", "").lower() or target in item.get("file", "").lower():
                    print(f"=== Library Volume: {item.get('title')} ===")
                    print(f"ID:          {item.get('id')}")
                    print(f"Category:    {item.get('category', '').title()}")
                    if "level" in item:
                        print(f"Level:       {item.get('level', '').title()}")
                    print(f"Author(s):   {item.get('author')}")
                    print(f"Year:        {item.get('year')}")
                    print(f"Publisher:   {item.get('publisher')}")
                    if "word_count" in item:
                        print(f"Word Count:  {item['word_count']:,d} words")
                    if "file" in item:
                        print(f"Local File:  library/{item['file']}")
                    if "archive_id" in item and item["archive_id"]:
                        print(f"Archive URL: https://archive.org/details/{item['archive_id']}")
                    print(f"Description: {item.get('description')}")
                    found = True
                    break
            if not found:
                print(f"Volume '{args.info}' not found in library.")
        elif args.read:
            text = koshur.read_library_source(args.read, max_chars=args.chars)
            if text:
                print(f"=== Previewing: {args.read} (First {len(text)} characters) ===")
                print(text)
            else:
                print(f"Could not read source '{args.read}'.")
        elif args.search:
            results = koshur.search_library_text(args.search, max_results=10)
            print(f"=== Library Full-Text Search for '{args.search}' ({len(results)} matches) ===")
            if results:
                for r in results:
                    print(f"\n[library/{r['file']} (Line {r['line_number']})]")
                    print(f"  {r['snippet']}")
            else:
                print(f"No occurrences of '{args.search}' found in library corpus.")
        elif args.category:
            cat = koshur.get_library_catalog()
            items = [i for i in cat.get("items", []) if i.get("category", "").lower() == args.category.lower()]
            print(f"=== Library Category: {args.category.title()} ({len(items)} volumes) ===")
            for i in items:
                wc = f"({i['word_count']:,d} words)" if "word_count" in i else "(Catalog)"
                lvl = f"[{i.get('level', '').title()[:5]}]" if "level" in i else ""
                print(f"• {lvl:<7} [{i.get('id')}] {i.get('title')} - {i.get('author', 'Unknown')} {wc}")
        else:
            cat = koshur.get_library_catalog()
            items = cat.get("items", [])
            st = koshur.get_library_stats()
            print(f"=== Koshur Digital Library ({len(items)} volumes, {st.get('total_words', 3348910):,d} words) ===")
            for i in items:
                wc = f"({i['word_count']:,d} words)" if "word_count" in i else "(Catalog)"
                lvl = f"[{i.get('level', '').title()[:5]}]" if "level" in i else ""
                print(f"• {lvl:<7} [{i.get('category', '').title():<10}] {i.get('title')[:50]:<52} {wc}")
            print("\nOptions: --stats, --level <elementary|intermediate|advanced>, --category <name>, --info <id>, --read <id>, --search <query>")

    elif args.command == "proverb":
        if args.search:
            res = koshur.search_proverbs(args.search)
            print(f"Found {len(res)} proverb(s):")
            for p in res:
                print(f"\n[#{p['id']}] {p['kashmiri_roman']}")
                print(f"  Devanagari:   {p['kashmiri_dev']}")
                print(f"  Perso-Arabic: {p['kashmiri_arabic']}")
                print(f"  Sharada:      {p['kashmiri_sharada']}")
                print(f"  English:      {p['translation_en']}")
                print(f"  Context:      {p['cultural_context']}")
        elif args.all:
            all_p = koshur.get_all_proverbs()
            print(f"=== All {len(all_p)} Kashmiri Proverbs ===")
            for p in all_p:
                print(f"#{p['id']:02d}: {p['kashmiri_roman']} -> {p['translation_en']}")
        else:
            p = koshur.random_proverb()
            print(f"--- Kashmiri Proverb #{p['id']} ---")
            print(f"Roman:        {p['kashmiri_roman']}")
            print(f"Devanagari:   {p['kashmiri_dev']}")
            print(f"Perso-Arabic: {p['kashmiri_arabic']}")
            print(f"Sharada:      {p['kashmiri_sharada']}")
            print(f"English:      {p['translation_en']}")
            print(f"Hindi:        {p['translation_hi']}")
            print(f"Context:      {p['cultural_context']}")

    elif args.command == "revenue":
        if args.search:
            results = koshur.search_revenue_terms(args.search)
            print(f"=== J&K Revenue Terms matching '{args.search}' ({len(results)} found) ===")
            for r in results:
                print(f"? {r['key']} ({r.get('term_urdu', '')} / {r.get('term_dev', '')}) [{r.get('category', '')}]")
                print(f"  English: {r.get('meaning_en', '')}")
                print(f"  Hindi:   {r.get('meaning_hi', '')}")
                print()
        elif args.category:
            results = koshur.get_terms_by_category(args.category)
            print(f"=== J&K Revenue Terms in Category '{args.category}' ({len(results)} terms) ===")
            for r in results:
                print(f"? {r['key']:<24} {r.get('term_urdu', ''):<18} {r.get('term_dev', ''):<20} {r.get('meaning_en', '')[:45]}")
        elif args.list:
            categories = koshur.list_categories()
            terms = koshur.list_revenue_terms()
            print(f"=== J&K Land Revenue Registry ({len(terms)} terms across {len(categories)} categories) ===")
            print("Categories:")
            for c in categories:
                count = len(koshur.get_terms_by_category(c))
                print(f"  - {c} ({count} terms)")
            print("\nUse 'koshur revenue --category <category>' or '--search <keyword>' to inspect.")
        elif args.term:
            res = koshur.lookup_revenue_term(args.term)
            if res:
                print("=== J&K Land Revenue Record ===")
                print(f"Term (English): {args.term.title()}")
                print(f"Term (Urdu):    {res.get('term_urdu', '')}")
                print(f"Term (Dev):     {res.get('term_dev', '')}")
                print(f"Category:       {res.get('category', '')}")
                print(f"English:        {res.get('meaning_en', '')}")
                print(f"Hindi:          {res.get('meaning_hi', '')}")
                if 'frequency' in res:
                    print(f"Frequency:      {res['frequency']}")
            else:
                print(f"Revenue term '{args.term}' not found in registry. Run 'koshur revenue --list' or '--search <query>'.")
        else:
            print("Please specify --term <name>, --search <query>, --category <category>, or --list.")

    elif args.command == "shikasta":
        if args.rules:
            print("=== Khat-i-Shikast (?? ?????) Orthographic Ligature Rules ===")
            rules = koshur.list_shikasta_rules()
            for rk in rules:
                r = koshur.explain_shikasta_rule(rk)
                print(f"? {r.get('letter', rk)}: {r.get('shikasta_rule', '')[:90]}...")
            print("\nRun 'koshur shikasta --rule <letter_name>' for detailed letter breakdown.")
        elif args.rule:
            r = koshur.explain_shikasta_rule(args.rule)
            if r:
                print(f"=== Shikasta Rule: {r.get('letter', args.rule)} ===")
                print(f"Standard Nasta'liq: {r.get('standard_rule', '')}")
                print(f"Shikasta Rule:     {r.get('shikasta_rule', '')}")
                if "subsequent_rule" in r:
                    print(f"Subsequent Link:   {r['subsequent_rule']}")
                if "examples" in r:
                    print("Examples:")
                    for ex in r["examples"]:
                        print(f"  - {ex.get('word', '')} ({ex.get('meaning', '')}): {ex.get('note', '')}")
            else:
                print(f"Rule '{args.rule}' not found. Available rules: {', '.join(koshur.list_shikasta_rules())}")
        elif args.abbrevs:
            print("=== Khat-i-Shikast Historical Scribal & Court Abbreviations ===")
            abbrevs = koshur.list_shikasta_abbreviations()
            print(f"{'Key':<26} {'Abbr':<12} {'Full Urdu':<30} {'Meaning'}")
            print("-" * 110)
            for k in abbrevs:
                info = koshur.lookup_shikasta_abbreviation(k)
                print(f"{k:<26} {info.get('arabic', ''):<12} {info.get('transliteration', ''):<30} {info.get('meaning_en', '')[:40]}")
        elif args.abbrev:
            info = koshur.lookup_shikasta_abbreviation(args.abbrev)
            if info:
                print(f"=== Scribal Abbreviation: {args.abbrev} ===")
                print(f"Abbreviation Form: {info.get('arabic', '')}")
                print(f"Full Urdu / Term:  {info.get('transliteration', '')}")
                print(f"Meaning (English): {info.get('meaning_en', '')}")
                print(f"Meaning (Hindi):   {info.get('meaning_hi', '')}")
                print(f"Usage Context:     {info.get('context', '')}")
            else:
                print(f"Abbreviation '{args.abbrev}' not found. Run 'koshur shikasta --abbrevs' to list all.")
        elif args.weight:
            tolas = 0.0
            sers = 0.0
            maunds = 0.0
            val = float(args.weight[0])
            unit = args.weight[1].lower() if len(args.weight) > 1 else "tola"
            if "tola" in unit:
                tolas = val
            elif "ser" in unit:
                sers = val
            elif "maund" in unit or "man" in unit:
                maunds = val
            res = koshur.convert_traditional_weight(maunds=maunds, sers=sers, tolas=tolas)
            print(f"=== Traditional Weight Conversion ({val} {unit}) ===")
            print(f"Grams:            {res['total_grams']} g")
            print(f"Kilograms:        {res['total_kg']} kg")
            print(f"Imperial Pounds:  {res['total_lbs']} lbs")
            print(f"Kashmiri Traks:   {res['kashmiri_traks']} traks (~5.2 kg/trak)")
            print(f"Kashmiri Kharwar: {res['kashmiri_kharwar']} kharwar (~83.2 kg/kharwar)")
        elif args.currency:
            r = int(args.currency[0]) if len(args.currency) > 0 else 0
            a = int(args.currency[1]) if len(args.currency) > 1 else 0
            p = int(args.currency[2]) if len(args.currency) > 2 else 0
            c = koshur.format_traditional_currency(rupees=r, annas=a, paisas=p)
            print("=== Traditional Pre-Decimal Currency ===")
            print(f"Urdu / Raqam:    {c['urdu_text']}")
            print(f"English:         Rs. {c['rupees']}, {c['annas']} Annas, {c['paisas']} Paisas")
            print(f"Decimal Value:   Rs. {c['decimal_rupees']:.4f}")
        elif args.fasli:
            finfo = koshur.calculate_fasli_year()
            print("=== Fasli Agricultural & Revenue Calendar ===")
            print(f"Fasli Year:      {finfo['fasli_year_urdu']} (Year {finfo['fasli_year']})")
            print(f"Fasli Period:    {finfo['fasli_period']}")
            print(f"Samvat / Bikrami:{finfo['samvat_year_urdu']}")
            print(f"Gregorian Date:  {finfo['gregorian_date']}")
            print(f"Historical Note: {finfo['explanation']}")
        else:
            print("Please specify --rules, --rule <letter>, --abbrevs, --abbrev <key>, --weight <val> <unit>, --currency <r> <a> <p>, or --fasli.")

    elif args.command == "area":
        conv = koshur.convert_land_area(kanals=args.kanals, marlas=args.marlas, sersai=args.sersai)
        print("=== J&K Land Area Conversion ===")
        print(f"Input: {args.kanals} Kanals, {args.marlas} Marlas, {args.sersai} Sersai")
        print(f"Total Marlas:    {conv['total_marlas']}")
        print(f"Total Kanals:    {conv['total_kanals']}")
        print(f"Square Feet:     {conv['sq_feet']} sq ft")
        print(f"Square Metres:   {conv['sq_meters']} sq m")
        print(f"Acres (Ghumaon): {conv['acres']} acres")
        print(f"Hectares:        {conv['hectares']} ha")

    elif args.command == "number":
        res = koshur.number_to_koshur(args.value, script=args.script)
        print(f"{args.value} in Koshur ({args.script}): {res}")

    elif args.command == "dialect":
        res = koshur.get_dialect_info(args.name)
        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "compare":
        comp = koshur.compare_dialects(args.concept)
        if comp:
            print(f"=== Dialect Comparison for '{args.concept}' ===")
            for c in comp:
                print(f"Concept:            {c['concept']}")
                print(f"Standard Kashmiri:  {c['standard_kashmiri']}")
                print(f"Kishtwari:          {c['kishtwari']}")
                print(f"Poguli:             {c['poguli']}")
                print(f"Siraji:             {c['siraji']}")
                print(f"Sanskrit Cognate:   {c['sanskrit_cognate']}")
                print("-" * 40)
        else:
            print(f"No comparative entries found for '{args.concept}'.")

    elif args.command == "grammar":
        if args.noun:
            dec = koshur.decline_noun(args.noun, gender=args.gender)
            print(f"=== Declension Paradigm: {args.noun} ({args.gender}) ===")
            print(json.dumps(dec, indent=2, ensure_ascii=False))
        elif args.verb:
            conj = koshur.conjugate_verb(args.verb)
            print(f"=== Conjugation Paradigm: {args.verb} ===")
            print(json.dumps(conj, indent=2, ensure_ascii=False))
        elif args.syntax:
            tokens = args.syntax.split()
            syn = koshur.analyze_v2_syntax(tokens)
            print("=== V2 Syntax Analysis ===")
            print(json.dumps(syn, indent=2, ensure_ascii=False))
        elif args.stem:
            stemmed = stem_word(args.stem)
            print(f"Word:    {args.stem}")
            print(f"Stem:    {stemmed}")
        else:
            print("Please specify --noun, --verb, --syntax, or --stem.")

    elif args.command == "phonology":
        if args.ipa:
            ipa = koshur.to_ipa(args.ipa)
            print(f"Input: {args.ipa}")
            print(f"IPA:   /{ipa}/")
        elif args.vowels:
            print("=== Kashmiri 16-Vowel Inventory ===")
            print(f"{'IPA':<6} {'Devanagari':<12} {'Perso-Arabic':<14} {'Description'}")
            print("-" * 65)
            for v in KASHMIRI_VOWEL_INVENTORY:
                desc = f"{v['height']} {v['backness']} ({v.get('example', '')})"
                print(f"{v['symbol']:<6} {v['devanagari']:<12} {v['persoarabic']:<14} {desc}")
        else:
            print("Please specify --ipa <text> or --vowels.")

    elif args.command == "analyze":
        stats = analyze_text(args.text)
        print("=== Linguistic Corpus Analysis ===")
        print(json.dumps(stats, indent=2, ensure_ascii=False))

    elif args.command == "folklore":
        if args.genres:
            genres = koshur.get_all_folklore_genres()
            print("=== Kashmiri Folklore & Musical Traditions ===")
            for g in genres:
                print(f"[{g['id']}] {g['name']} ({g.get('devanagari', '')} / {g.get('persoarabic', '')} / {g.get('sharada', '')})")
                print(f"  Description: {g.get('description', '')}")
                if "instruments" in g:
                    print(f"  Instruments: {', '.join(g['instruments'])}")
                print()
        elif args.genre:
            g = koshur.get_folklore_genre(args.genre)
            if g:
                print(f"=== Folklore Genre: {g['name']} ===")
                print(f"Devanagari:   {g.get('devanagari', '')}")
                print(f"Perso-Arabic: {g.get('persoarabic', '')}")
                print(f"Sharada:      {g.get('sharada', '')}")
                print(f"Category:     {g.get('category', '')}")
                print(f"Description:  {g.get('description', '')}")
                if "cultural_significance" in g:
                    print(f"Significance: {g['cultural_significance']}")
                if "instruments" in g:
                    print(f"Instruments:  {', '.join(g['instruments'])}")
                if "occasions" in g:
                    print(f"Occasions:    {', '.join(g['occasions'])}")
                if "sample_verse" in g:
                    sv = g["sample_verse"]
                    print("\nSample Verse:")
                    print(f"  Roman:        {sv.get('kashmiri_roman', '')}")
                    print(f"  Devanagari:   {sv.get('kashmiri_dev', '')}")
                    print(f"  Perso-Arabic: {sv.get('kashmiri_arabic', '')}")
                    print(f"  Sharada:      {sv.get('kashmiri_sharada', '')}")
                    print(f"  English:      {sv.get('translation_en', '')}")
            else:
                print(f"Genre '{args.genre}' not found. Run 'koshur folklore --genres' to list all.")
        elif args.songs:
            songs = koshur.get_all_songs()
            print("=== Traditional Kashmiri Folk & Classical Songs ===")
            for s in songs:
                print(f"[{s['id']}] \"{s['title']}\" by {s.get('poet', 'Unknown')} - {s.get('genre', '')}")
        elif args.song:
            s = koshur.get_song(args.song)
            if s:
                print(f"=== Song: {s['title']} ===")
                print(f"Poet / Composer:  {s.get('poet', 'Traditional')}")
                print(f"Genre:            {s.get('genre', '')}")
                print(f"Musical Style:    {s.get('musical_genre', 'N/A')}")
                print(f"Theme:            {s.get('theme', 'N/A')}")
                if "historical_context" in s:
                    print(f"Context:          {s['historical_context']}")
                print("\nLyrics (Roman):")
                print(s.get("kashmiri_roman", "").strip())
                print("\nLyrics (Devanagari):")
                print(s.get("kashmiri_dev", "").strip())
                print("\nLyrics (Perso-Arabic):")
                print(s.get("kashmiri_arabic", "").strip())
                print("\nLyrics (Sharada):")
                print(s.get("kashmiri_sharada", "").strip())
                print("\nEnglish Translation:")
                print(s.get("translation_en", "").strip())
            else:
                print(f"Song '{args.song}' not found. Run 'koshur folklore --songs' to list all.")
        elif args.search:
            results = koshur.search_songs(args.search)
            if results:
                print(f"Found {len(results)} matching song(s) for '{args.search}':")
                for s in results:
                    print(f"- [{s['id']}] \"{s['title']}\" by {s.get('poet', 'Unknown')} ({s.get('genre', '')})")
            else:
                print(f"No songs found matching '{args.search}'.")
        else:
            print("Please specify --genres, --genre <id>, --songs, --song <id>, or --search <query>.")

    elif args.command == "deity":
        if args.bhairavas:
            bhairavas = koshur.get_guardian_bhairavas()
            print("=== Ashta Bhairavas of the Kashmir Valley (8 Directional Guardians) ===")
            print(f"{'Direction':<14} {'Bhairava Name':<28} {'Location / Mohalla':<32} {'Role'}")
            print("-" * 105)
            for b in bhairavas:
                print(f"{b['direction']:<14} {b['name']:<28} {b['location']:<32} {b.get('role', 'N/A')}")
        elif args.all:
            deities = koshur.get_all_deities()
            print("=== Kashmiri Sacred Pantheon & Tirthas ===")
            for d in deities:
                print(f"• {d['name']} ({d.get('devanagari', '')} / {d.get('sharada', '')}) - {d.get('category', '')}")
                print(f"  Shrine: {d.get('shrine_location', 'Kashmir')}")
                sig = d.get('mythological_origin') or d.get('description') or d.get('significance', '')
                if sig:
                    print(f"  Significance: {sig[:120]}...")
                print()
        elif args.name:
            d = koshur.lookup_deity(args.name)
            if d:
                print(f"=== Deity / Tirtha: {d['name']} ===")
                print(f"Devanagari:   {d.get('devanagari', '')}")
                print(f"Perso-Arabic: {d.get('persoarabic', '')}")
                print(f"Sharada:      {d.get('sharada', '')}")
                print(f"Category:     {d.get('category', '')}")
                if "epithets" in d:
                    print(f"Epithets:     {', '.join(d['epithets'])}")
                print(f"Shrine / Tirtha: {d.get('shrine_location', '')}")
                if "annual_festival" in d:
                    print(f"Sacred Festival: {d['annual_festival']}")
                if "iconography" in d:
                    print(f"Iconography:  {d['iconography']}")
                sig = d.get('mythological_origin') or d.get('description') or d.get('significance', '')
                if sig:
                    print(f"Significance: {sig}")
            else:
                print(f"Deity '{args.name}' not found. Run 'koshur deity --all' or '--bhairavas' to inspect all.")
        else:
            print("Please specify --name <deity>, --bhairavas, or --all.")

    elif args.command in ["translate-record", "record-translate"]:
        if getattr(args, "serve", False):
            from koshur.translator.web_app import start_server
            start_server(host=args.host, port=args.port, open_browser=not args.no_browser)
            return

        if args.list_samples:
            samples = koshur.list_sample_records()
            print("=== Archival J&K Revenue & Legal Sample Records ===")
            for s in samples:
                print(f"[{s['id']}] {s['title']} ({s.get('date', '')}) - Mauza {s.get('village', '')}, {s.get('district', '')}")
            return

        target_lang = getattr(args, "lang", "en")
        res = None

        if args.sample:
            s_data = koshur.get_sample_record(args.sample)
            if not s_data:
                print(f"Error: Sample record '{args.sample}' not found. Run 'koshur translate-record --list-samples' to view all.")
                return
            res = koshur.translate_record(s_data["urdu_text"], doc_id=args.sample, target_lang=target_lang)
        elif args.file:
            res = koshur.translate_record_file(args.file, target_lang=target_lang)
        elif args.text:
            res = koshur.translate_record(args.text, target_lang=target_lang)
        else:
            print("Please specify --text <str>, --file <path>, --sample <id>, --list-samples, or --serve.")
            return

        if args.json:
            out_str = json.dumps(res, indent=2, ensure_ascii=False)
        elif args.html:
            out_str = res.get("certified_html", "")
        else:
            out_str = res.get("markdown", "")

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(out_str)
            print(f"Translation successfully saved to '{args.output}'.")
        else:
            print(out_str)

    elif args.command == "translator-web":
        from koshur.translator.web_app import start_server
        start_server(host=args.host, port=args.port, open_browser=not args.no_browser)

    elif args.command == "version":
        print(f"Koshur Computational Linguistics, Web Application & Preservation Toolkit v{koshur.__version__}")
        print("Specialized Features: J&K Land Records Decipherment, Khat-i-Shikast Palaeography & Bilingual Legal Translation (EN/HI)")

if __name__ == "__main__":
    main()

