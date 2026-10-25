# Koshur (कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳)

[![PyPI version](https://img.shields.io/badge/pypi-v1.1.0-blue.svg)](https://pypi.org/project/koshur/)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://pypi.org/project/koshur/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests Passing](https://img.shields.io/badge/tests-99%20passed-brightgreen.svg)]()
[![Lexicon](https://img.shields.io/badge/lexicon-1%2C616%20entries-purple.svg)]()
[![Digital Library](https://img.shields.io/badge/library-5.51M%2B%20words%20%7C%2061%20volumes-blueviolet.svg)]()
[![Scripts](https://img.shields.io/badge/scripts-Sharada%20%7C%20Devanagari%20%7C%20Perso--Arabic%20%7C%20Latin-orange)]()

**Koshur** is an authoritative, production-grade computational linguistics toolkit, web development localization framework, and digital preservation library for the **Kashmiri language** (*Kōshur* / कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳) and its endangered regional sister dialects (**Kishtwari**, **Poguli**, **Siraji**, and **Rambani**).

---

## Table of Contents
1. [Linguistic Background & Preservation Mission](#linguistic-background--preservation-mission)
2. [Architecture & Key Features](#architecture--key-features)
3. [Installation](#installation)
4. [Quickstart Guide](#quickstart-guide)
   - [1. Multi-Script Transliteration](#1-multi-script-transliteration-sharada--devanagari--perso-arabic--latin)
   - [2. Lexicon & Fuzzy Dictionary Lookup (1,616 Entries)](#2-lexicon--fuzzy-dictionary-lookup-1616-entries)
   - [3. Web & Mobile App Localization (i18n & WebFonts)](#3-web--mobile-app-localization-i18n--webfonts)
   - [4. Date, Time & Calendar Formatting](#4-date-time--calendar-formatting)
   - [5. Multi-Script Search Indexing & Autocomplete](#5-multi-script-search-indexing--autocomplete)
   - [6. Computational Linguistics & Fieldwork Research](#6-computational-linguistics--fieldwork-research)
   - [7. Kashmiri Morphosyntax & V2 Syntax Analyzer](#7-kashmiri-morphosyntax--v2-syntax-analyzer)
   - [8. Traditional Proverbs & Idioms (Kahan & Masal)](#8-traditional-proverbs--idioms-kahan--masal)
   - [9. Phonology & IPA Transcription (16-Vowel System)](#9-phonology--ipa-transcription-16-vowel-system)
   - [10. Comparative Dialectology Engine](#10-comparative-dialectology-engine)
   - [11. J&K Land Revenue Records & Area Converter](#11-historical-jk-land-revenue-records--area-converter)
   - [12. NLP Tokenizer & Text Analytics](#12-nlp-tokenizer--text-analytics)
   - [13. Folklore, Classical Songs & Sacred Kashmiri Pantheon](#13-folklore-classical-songs--sacred-kashmiri-pantheon)
   - [14. Government Records Translation & Decipherment (Image & Text to English)](#14-government-records-translation--decipherment-image--text-to-english)
   - [15. Digital Linguistics Library (5.51M+ Words & 60 Volumes)](#15-digital-linguistics-library-551m-words--60-volumes)
5. [Command Line Interface (CLI)](#command-line-interface-cli)
6. [Academic & Research References](#academic--research-references)
7. [License](#license)

---

## Linguistic Background & Preservation Mission

Kashmiri (*Koshur*) belongs to the Dardic subgroup of the Indo-Aryan language family, spoken by over 7 million people predominantly in the Kashmir Valley of Jammu & Kashmir and across the global diaspora. 

Typologically, Kashmiri is unique among modern Indo-Aryan languages:
- **Strict Verb-Second (V2) Word Order**: Unlike almost all other modern South Asian languages which are strictly Verb-Final (SOV), Kashmiri exhibits Verb-Second (V2) syntax in root clauses, mirroring Germanic languages (such as German, Dutch, and Icelandic).
- **Extraordinary Vowel System**: Features a rich inventory of **16 phonemic vowels**, including rare high and mid-central vowels (*/ɨ/*, */ɨː/*, */ə/*, */əː/*) requiring special diacritical orthography.
- **Pervasive Palatalization (*Matsaryar*)**: Extensive consonant palatalization and morphophonemic vowel shifts that distinguish noun plurals, past tense verb stems, and case markers.
- **Multi-Script Heritage**:
  - **Sharada (𑆯𑆳𑆫𑆢𑆳)**: The historical Brahmic script native to Kashmir (dating back to the 8th century CE), in which ancient Sanskrit and Old Kashmiri manuscripts (*Vyeth* / Vitasta literary tradition) were documented.
  - **Kashmiri Devanagari (कश्मीरी देवनागरी)**: Standardized Devanagari script enriched with Unicode diacritics (ॳ, ॴ, ॶ, ॷ, ॅ, ॉ) for central and short vowels.
  - **Kashmiri Perso-Arabic (کٲشُر نستعلیق)**: The officially recognized Nastaliq-based script utilizing specialized diacritics (including *inverted damma* ٚ, *noon ghunna* ٛ, *waw with ring* ۄ, and *Kashmiri yeh* ؠ).
  - **Roman / Latin Phonetic**: Academic romanization with macrons and IPA transcription.

`koshur` was built as a comprehensive computational toolkit to preserve, analyze, transliterate, and revitalize this ancient and vulnerable linguistic treasure.

---

## Architecture & Key Features

| Subpackage | Description |
| :--- | :--- |
| **`koshur.scripts`** | Bidirectional transliteration between Sharada, Devanagari, Perso-Arabic, and Latin scripts. Script auto-detector. |
| **`koshur.web`** | Web & mobile UI localization (react-i18next/vue-i18n ready), HTML text-direction/font wrappers, and virtual keyboards. |
| **`koshur.datetime`** | Kashmiri calendar engine (Saptrishi/Navreh & Gregorian), relative time formatter (*vuhein*, *rāth*, *pāgah*), and time-of-day terms. |
| **`koshur.search`** | Inverted multi-script search indexer with diacritic-insensitive normalization and real-time prefix autocomplete. |
| **`koshur.research`** | Computational fieldwork suite: Leipzig interlinear glossing, CoNLL-U, TEI-XML, JSON-LD Linked Data, and quantitative lexical metrics. |
| **`koshur.phonology`** | Complete 16-vowel inventory, vowel shift rules, consonant palatalization (*matsaryar*), and automatic IPA transcription engine. |
| **`koshur.grammar`** | V2 (Verb-Second) syntax clause analyzer, split-ergative 4-class noun declensions, verb conjugator with clitics, and stemmer. |
| **`koshur.lexicon`** | Curated 570+ entry cultural lexicon with 5-stage fuzzy lookup (handles accents/spelling variations), 30 traditional proverbs, and numeral converters. |
| **`koshur.folklore`** | Kashmiri folklore genres (Wanvun, Rouf, Chakri, Ladishah, Bhand Pather), authentic songs (Habba Khatoon, Rasul Mir, Arnimal, Lal Ded), sacred pantheon (Sharika, Kheer Bhawani, Jwalamukhi, Nilamata Nagas), and Ashta Bhairavas. |
| **`koshur.dialects`** | Comparative dialectology engine covering **Kishtwari** (archaic consonant cluster retention), **Poguli** (transitional Dardic-Pahari), **Siraji**, and **Rambani**. |
| **`koshur.revenue`** | Digital register of official Jammu & Kashmir Land Revenue Records (*Jamabandi*, *Khasra*, *Girdawari*, *Intiqal*) and traditional area converter (*Kanal*, *Marla*, *Sersai*, *Ghumaon*). |
| **`koshur.translator`** | Domain-aware government land records & deeds decipherment engine: converts scans/images (PNG, JPG, TIFF, WEBP, PDF) or raw text (Urdu, Khat-i-Shikast, Kashmiri) into certified English translations with cadastral conversions and printable certificates. |
| **`koshur.nlp`** | Script-aware sentence and word tokenizer, Perso-Arabic/Indic normalizer, and corpus text diversity statistics analyzer. |
| **`koshur.cli`** | Comprehensive command-line utility with rich UTF-8 output support across all operating systems. |

---

## Installation

Install in editable/development mode directly from source:

```bash
git clone https://github.com/analytics-hub-new26/koshur-language-library.git
cd koshur
pip install -e .
```

Verify the installation:

```bash
python -m koshur.cli version
```

---

## Quickstart Guide

### 1. Multi-Script Transliteration (Sharada / Devanagari / Perso-Arabic / Latin)

```python
import koshur

# Transliterate from Roman / Latin to Sharada
print(koshur.to_sharada("Vyeth"))
# Output: 𑆮𑇀𑆪𑆼𑆡𑇀

# Transliterate from Devanagari to Sharada
print(koshur.to_sharada("कश्मीरी"))
# Output: 𑆑𑆯𑇀𑆩𑆵𑆫𑆵

# Transliterate to Kashmiri Perso-Arabic
print(koshur.to_persoarabic("Vyeth"))
# Output: ویےتھ

# Transliterate to Kashmiri Devanagari
print(koshur.to_devanagari("koshur"))
# Output: कोशुर्

# Universal transliteration dispatcher
result = koshur.transliterate("शीन", target_script="sharada")
print(result) # Output: 𑆯𑆵𑆤
```

### 2. Lexicon & Fuzzy Dictionary Lookup (1,616 Entries)

The dictionary features an intelligent **5-stage lookup engine** that indexes **1,616 curated vocabulary entries** with 100% 4-script representation (Sharada, Devanagari, Perso-Arabic, Latin), resolving exact matches, handling diacritic insensitivity (e.g. typing `pheran` matches `Phēran`), alternative transliterations (`phoran`, `phiran`), aliases, and English/Hindi semantic queries:

```python
import koshur

# Lookup with typo or alternative spelling
word = koshur.lookup("phoran")
print(word["lemma"])        # Phēran
print(word["devanagari"])   # फेरन
print(word["persoarabic"])  # پھیرَن
print(word["sharada"])      # 𑆦𑆼𑆫𑆤
print(word["meaning_en"])   # Traditional long woollen Kashmiri cloak worn in winter

# Lookup landmark / river by historical Sanskrit name
river = koshur.lookup("vitasta")
print(river["lemma"])       # Vyeth (The Jhelum River)

# Search words by category tag
cuisine_items = koshur.get_words_by_tag("cuisine")
print(f"Total cuisine items: {len(cuisine_items)}")
for item in cuisine_items[:5]:
    print(f"- {item['lemma']}: {item['meaning_en']}")

# Translate convenience function
print(koshur.translate("Sheen", target_lang="en")) # Snow
print(koshur.translate("Sheen", target_lang="hi")) # बर्फ़ / हिम
```

### 3. Web & Mobile App Localization (i18n & WebFonts)

Build production websites, web apps, and mobile applications in Kashmiri:

```python
import koshur

# 1. UI String Localization across scripts
print(koshur.get_ui_string("home", script="devanagari"))    # सादर
print(koshur.get_ui_string("home", script="persoarabic"))   # سادُر
print(koshur.get_ui_string("search", script="sharada"))     # 𑆒𑆾𑆘
print(koshur.get_ui_string("save", script="persoarabic"))     # رَچھُن

# 2. Export localization dictionaries for React (react-i18next), Vue (vue-i18n), Next.js
locales = koshur.export_i18n_json(script="devanagari", filepath="locales/ks-Deva.json")

# 3. HTML text wrappers & CSS font configuration
html_tag = koshur.wrap_html_text("کٲشُر", script="persoarabic")
# Output: <span dir="rtl" lang="ks-Arab" class="koshur-persoarabic">کٲشُر</span>

# 4. Virtual Keyboard & Real-time Phonetic input for search inputs
kashmiri_text = koshur.transcribe_keystrokes("koshur chhu asul", target_script="devanagari")
# Output: कोशुर् छु असुल्
```

### 4. Date, Time & Calendar Formatting

```python
import koshur
import datetime

# 1. Format dates in Kashmiri (Gregorian or Traditional Navreh calendar)
dt = datetime.date(2026, 10, 8)
print(koshur.format_date(dt, script="devanagari"))
# Output: ब्रेसवार, ८ अक्टूबर २०२६

print(koshur.format_date(dt, script="persoarabic"))
# Output: برٛیسوار، ٨ اَکتوٗبَر ٢٠٢٦

# 2. Human-friendly Relative Time ("Just now", "Yesterday", "3 hours ago")
print(koshur.format_relative_time(20, script="devanagari"))     # वुहैन (अभी)
print(koshur.format_relative_time(86400, script="devanagari"))  # राथ (कल)
print(koshur.format_relative_time(-86400, script="persoarabic")) # پاگَہ (कल)

# 3. Kashmiri Times of Day
print(koshur.get_time_of_day(8, script="devanagari"))   # सुबहन् (Morning)
print(koshur.get_time_of_day(14, script="devanagari"))  # दुपहर (Afternoon)
print(koshur.get_time_of_day(22, script="devanagari"))  # राथस् (Night)
```

### 5. Multi-Script Search Indexing & Autocomplete

In-memory search indexer that strips Kashmiri diacritics and enables unified search across scripts:

```python
import koshur

# Get pre-built index of the entire 300+ word Kashmiri lexicon
search_index = koshur.KoshurSearchIndex.get_default_lexicon_index()

# 1. Diacritic-insensitive search (matches even with loose spelling)
results = search_index.search("samovar")
for r in results[:3]:
    print(f"[{r['score']}] {r['document']['title']}")

# 2. Real-time autocomplete suggestions for search inputs
suggestions = search_index.autocomplete("phe", limit=5)
for s in suggestions:
    print(f"- {s['title']} ({s['meaning']})")
```

### 6. Computational Linguistics & Fieldwork Research

Tools designed for field linguists, NLP researchers, and digital humanists:

```python
import koshur

# 1. Leipzig Glossing Rules standard interlinear generator
src = ["aslam-an", "por", "akhavbar"]
gls = ["Aslam-ERG", "read.PST.M.SG", "newspaper.NOM.M.SG"]
trans = "Aslam read the newspaper."

print(koshur.generate_leipzig_gloss(src, gls, trans, output_format="text"))
# aslam-an   por            akhavbar
# Aslam-ERG  read.PST.M.SG  newspaper.NOM.M.SG
# 'Aslam read the newspaper.'

# 2. Corpus Lexical Metrics (TTR, Hapax Legomena, Syllables, V2 verification)
metrics = koshur.compute_lexical_metrics("सु छु किताब परान। सो छ़े चाय चवान।")
print(f"TTR: {metrics['ttr']}, Hapax count: {metrics['hapax_count']}")

# 3. Universal Dependencies & Digital Humanities Exports
koshur.export_tei_xml(koshur.search_words("", tag="culture"), filepath="koshur_tei.xml")
```

### 7. Kashmiri Morphosyntax & V2 Syntax Analyzer

Analyze root clauses for strict Verb-Second positioning, decline nouns across 4 classes, and generate verb conjugations:

```python
import koshur

# 1. Analyze sentence with finite verb in position 2
clause = ["राजू", "छु", "च्योन", "ख्यवान"] # Raju is eating apple
analysis = koshur.analyze_v2_syntax(clause)
print(f"Is V2 compliant: {analysis['is_v2']}")        # True
print(f"Finite verb:    {analysis['finite_verb']}")   # छु
print(f"Position:       {analysis['position']}")      # 2

# 2. Morphological noun declension (split-ergative cases)
dec = koshur.decline_noun("larka")
print(dec["singular"]["ergative"]) # larkan (लड़कन / لڑکَن)
print(dec["singular"]["dative"])   # larkas (लड़कस / लड़कَس)

# 3. Verb conjugation paradigm & transitivity
conj = koshur.conjugate_verb("parun")
print(conj["present_tense"]["1st_sing_masc"]) # bɨ chhus parān
```

### 8. Traditional Proverbs & Idioms (Kahan & Masal)

Authentic Kashmiri proverbs featuring Lal Ded's vakhs, Sheikh Noor-ud-Din's shruks, and folk idioms:

```python
import koshur

# Random proverb
prov = koshur.random_proverb()
print(f"Roman:   {prov['kashmiri_roman']}")
print(f"English: {prov['translation_en']}")
print(f"Sharada: {prov['kashmiri_sharada']}")

# Search proverbs by keyword or author
results = koshur.search_proverbs("Nund Rishi")
for p in results:
    print(f"#{p['id']}: {p['kashmiri_roman']}")
    print(f"Meaning: {p['translation_en']}")
    # Ann pōshi teli yeli van pōshi (Food will thrive only as long as the forests thrive)
```

### 9. Phonology & IPA Transcription (16-Vowel System)

```python
import koshur
from koshur.phonology.palatalization import palatalize_consonant, apply_kashmiri_plural_mutation

# Convert Kashmiri text to IPA transcription
ipa = koshur.to_ipa("व्यथ्")
print(f"IPA: /{ipa}/")

# Consonant palatalization (matsaryar)
print(palatalize_consonant("t"))  # ts
print(palatalize_consonant("d"))  # j
print(palatalize_consonant("th")) # tsh

# Vowel shift in noun plural formation
print(apply_kashmiri_plural_mutation("gōr")) # gə̄rʲ
```

### 10. Comparative Dialectology Engine

Compare words and phonological evolutions across Standard Valley Kashmiri, Kishtwari, Poguli, and Siraji:

```python
import koshur

comparison = koshur.compare_dialects("brother")
for item in comparison:
    print(f"Standard Kashmiri: {item['standard_kashmiri']}") # bōi
    print(f"Kishtwari:         {item['kishtwari']}")         # bhrāu (preserves archaic Sanskrit cluster)
    print(f"Poguli:            {item['poguli']}")            # bhrāu
    print(f"Siraji:            {item['siraji']}")            # bhrā
    print(f"Sanskrit Cognate:  {item['sanskrit_cognate']}")  # bhrātṛ
```

### 11. Historical J&K Land Revenue Records & Cadastral Converter

Comprehensive computational encyclopedia of 79 authentic Jammu & Kashmir revenue terms across 25 administrative categories (Jamabandi, Khasra, Intiqal, Shajra, Dastavezat legal deeds, tenancy rights, and cadastral survey markers) plus traditional land area conversions:

```python
import koshur

# 1. Lookup revenue term in English, Urdu, or Hindi
jamabandi = koshur.lookup_revenue_term("jamabandi")
print(jamabandi["meaning_en"])  # Record of Rights (ROR) containing complete details of owners...
print(jamabandi["term_urdu"])   # ??? ????
print(jamabandi["term_dev"])    # ???????
print(jamabandi["category"])    # Register

# 2. Look up historical legal deeds (Dastavezat / ????? ? ?????????)
bainama = koshur.lookup_revenue_term("bainama")
print(bainama["term_urdu"])     # ??? ???? (Absolute registered deed of sale)

rahan = koshur.lookup_revenue_term("rahannama")
print(rahan["meaning_en"])      # Mortgage deed pledging agricultural land as collateral

# 3. Filter terms by category
deeds = koshur.get_terms_by_category("Deed")
print(f"Total deeds cataloged: {len(deeds)}")  # 11 deeds (Bainama, Rahannama, Hibanama, etc.)

# 4. Search across definitions and translations
results = koshur.search_revenue_terms("mortgage")
for r in results:
    print(r["key"], "->", r["term_urdu"])

# 5. Traditional J&K land measurement conversion
# 1 Karam = 5.5 ft | 1 Sersai = 30.25 sq ft | 1 Marla = 9 Sersai = 272.25 sq ft
# 1 Kanal = 20 Marlas = 5,445 sq ft | 1 Ghumaon (Acre) = 8 Kanals = 43,560 sq ft
conv = koshur.convert_land_area(kanals=4.0, marlas=10.0, sersai=4.5)
print(f"Total Kanals:  {conv['total_kanals']}")     # 4.525 Kanals
print(f"Square Feet:   {conv['sq_feet']} sq ft")    # 24,638.06 sq ft
print(f"Square Meters: {conv['sq_meters']} sq m")   # 2,288.95 sq m
print(f"Acres:         {conv['acres']} acres")      # 0.5656 acres
```

---

### 12. Khat-i-Shikast Palaeography & Archival Decipherment

Specialized palaeographical engine for reading, deciphering, and converting historical cursive **Khat-i-Shikast (?? ?????)** manuscripts, court orders (*Rubakari*), revenue petitiions, traditional weights, and pre-decimal accounting:

```python
import koshur
from datetime import date

# 1. Inspect cursive ligature and scribal rules
alif_rule = koshur.explain_shikasta_rule("alif")
print(alif_rule["shikasta_rule"])
# In Shikasta, Alif frequently connects continuously to following letters even at word beginnings...
for ex in alif_rule["examples"]:
    print(f"{ex['word']} ({ex['meaning']}) -> {ex['note']}")

# 2. Look up historical court and scribal abbreviations (Huroof-i-Muqatta'at)
abd = koshur.lookup_shikasta_abbreviation("al_abd")
print(abd["abbreviation"])   # Scribal glyph
print(abd["meaning_en"])     # The Servant / Signatory / Executant
print(abd["context"])        # Affixed before the name of the executant on deeds

copy_abbr = koshur.lookup_shikasta_abbreviation("naql_mutabiq_asl")
print(copy_abbr["meaning_en"])  # Certified True Copy (attestation formula)

# 3. Traditional weight conversions (Tola, Masha, Ser, Maund, Kashmiri Trak & Kharwar)
weights = koshur.convert_traditional_weight(sers=2.5, tolas=10.0)
print(f"Metric Grams:     {weights['total_grams']} g")
print(f"Metric Kilograms: {weights['total_kg']} kg")
print(f"Kashmiri Traks:   {weights['kashmiri_traks']} traks (~5.2 kg/trak)")

# 4. Historical Pre-Decimal Currency & Raqam Notation
curr = koshur.format_traditional_currency(rupees=25, annas=12, paisas=2)
print(curr["urdu_text"])       # 25 ????? 12 ??? 2 ????
print(curr["decimal_rupees"])  # 25.78125 Rupees

# 5. Fasli Agricultural & Revenue Calendar Converter
fasli = koshur.calculate_fasli_year(date(2026, 10, 10))
print(fasli["fasli_year_urdu"])  # ??? 1434 ????
print(fasli["samvat_year_urdu"]) # ??? 2083 ???? (?????)
print(fasli["explanation"])      # Historical crop accounting year introduced by Akbar...
```

---

### 13. Folklore, Classical Songs & Sacred Kashmiri Pantheon

```python
import koshur

# 1. Folklore Genres (Wanvun, Rouf, Chakri, Ladishah, Bhand Pather)
wanvun = koshur.get_folklore_genre("wanvun")
print(f"Genre: {wanvun['name']} ({wanvun['devanagari']} / {wanvun['sharada']})")
print(f"Sample: {wanvun['sample_verse']['translation_en']}")

# 2. Authentic Classical Songs & Ballads (4-script orthography & translations)
song = koshur.get_song("habba_khatoon_roshe")
print(f"Poet: {song['poet']}")
print(f"Lyrics (Sharada): {song['kashmiri_sharada']}")
print(f"Translation: {song['translation_en']}")

# Search songs by lyric keyword, poet, or theme
results = koshur.search_songs("kasturi")
print(f"Found: {results[0]['title']} by {results[0]['poet']}")

# 3. Sacred Pantheon & Nilamata Nagas
sharika = koshur.lookup_deity("sharika")
print(f"Deity: {sharika['name']} at {sharika['shrine_location']}")

kheer = koshur.lookup_deity("kheer bhawani")
print(f"Shrine: {kheer['shrine_location']} - Festival: {kheer['annual_festival']}")

# 4. Ashta Bhairavas (The 8 directional guardian deities of Srinagar)
bhairavas = koshur.get_guardian_bhairavas()
for b in bhairavas:
    print(f"[{b['direction']}] {b['name']} ({b['location']})")
```


### 14. Government Revenue Records Translation & Decipherment (English & Hindi with Zero-Error Guarantee)

Palaeographical decipherment and domain-aware translation engine designed specifically for Jammu & Kashmir historical revenue registers, court deeds, and cadastral records (*Jamabandi*, *Khasra Girdawari*, *Bainama*, *Intiqal*, *Rahannama*). Translates official Nastaliq/Shikasta records into **certified English** or **certified Hindi (हिन्दी)** based on user preference, with a **cryptographic zero-error information guarantee**.

#### Key Translation & Decipherment Capabilities:
1. **User Language Preference (English & Hindi)**: Supports full legal translation to English (`target_lang="en"`), Hindi (`target_lang="hi"`), or dual bilingual reports (`target_lang="both"`).
2. **Zero-Error Information Guarantee**: Generates a deterministic SHA-256 cryptographic audit seal of all extracted cadastral entities (survey parcels, measurements, parties, consideration, dates). Every survey identifier (*Khasra*, *Khewat*, *Khatauni*) is strictly preserved verbatim with zero numeric transcription errors.
3. **Statutory Cadastral Area Conversion**: Automatically calculates traditional J&K revenue land units (*1 Karam = 5.5 ft; 1 Sarsahi = 30.25 sq ft; 1 Marla = 9 Sarsahis = 272.25 sq ft; 1 Kanal = 20 Marlas = 5,445 sq ft; 1 Ghumaon/Acre = 8 Kanals = 43,560 sq ft*) and provides exact conversions to Square Feet, Square Meters, Standard Acres, and Hectares.
4. **Khat-i-Shikast Scribal Formula Decipherment**: Automatically detects and decodes historical scribal formulas (*al-abd* [العبد / अल-अब्द], *marqooma* [مرقومہ / अल-मरक़ूमा], *faqat* [فقط / फ़क़त], *manka* [منکہ / मनका], *dastkhat* [دستخط / हस्ताक्षर], *gawah shud* [گواہ شد / गवाह शुद], *naql mutabiq asl* [نقل مطابق اصل / नक़ल मुताबिक़ असल]) with legal significance in English and Hindi.
5. **Historical Calendar Support**: Converts and cross-references **Fasli** crop/revenue years and **Bikrami Samvat** dates to Gregorian equivalents.
6. **Printable Certified HTML Translation Certificates**: Generates self-contained, A4 print-ready legal certificates in both English and Hindi, complete with state archives styling, official seal, attestation block, and SHA-256 verification hash.
7. **Interactive Web Application**: Rich modern web interface (`koshur record-translate --serve`) with dark mode, glassmorphism, instant English/Hindi toggles, archival specimen loaders, and drag-and-drop document scan uploads.

```python
import koshur

# 1. Translate in Hindi (हिन्दी) based on user preference
sample = koshur.get_sample_record("jamabandi_shalimar")
res_hi = koshur.translate_record(sample["urdu_text"], doc_id="jamabandi_01", target_lang="hi")

print("Title (Hindi):", res_hi["title_hi"])
# Output: जमाबंदी (अधिकार अभिलेख)
print("Cadastral Integrity Seal:", res_hi["integrity_hash"])
# Output: d2f094d6d70c9fa6706fe9f8b6dcd25ce7e43787fee032d43a142846e26b6577 (Zero Error)

# Print Hindi cadastral conversion table
print(res_hi["cadastral_table_hi"])

# 2. Translate in English
res_en = koshur.translate_record(sample["urdu_text"], doc_id="jamabandi_01", target_lang="en")
print("Title (English):", res_en["title_en"])
# Output: Jamabandi (Record of Rights)

# 3. Dual Bilingual Translation (English & Hindi)
res_dual = koshur.translate_record(sample["urdu_text"], target_lang="both")

# 4. Save Official Printable Certificates
with open("jamabandi_certificate_hi.html", "w", encoding="utf-8") as f:
    f.write(res_hi["certified_html_hi"])

with open("jamabandi_certificate_en.html", "w", encoding="utf-8") as f:
    f.write(res_en["certified_html_en"])

# 5. Translate from uploaded file or archival scan
img_res = koshur.translate_record_file("page_66.png", target_lang="hi")
print("Deciphered Title:", img_res["title_hi"])
print("Khasra Numbers:", img_res["entities"]["survey"]["khasra_numbers"])
```

### 15. Digital Linguistics Library (4.32M+ Words & 50 Volumes)

The toolkit incorporates a comprehensive, digitized repository of Kashmiri literature, grammars, vocabularies, manuscript catalogues, and peer-reviewed linguistic research spanning **over 4.32 million words across 50 volumes** (25.6M+ characters), organized into a structured **graded learning progression**:

- **Elementary Level (8 volumes, ~154k words)**: 
  - Roop Krishen Bhat's *A Course in Kashmiri Language* (CIIL 2007)
  - Omkar N. Koul's *Spoken Kashmiri: A Language Course* (1987)
  - Shafi Shauq's *Kashmiri English Hindi Reader* (trilingual graded reader)
  - Naji Munwar & Prof. Shafi Shauq's *Kashur Grammar* (1973)
  - Rev. T. R. Wade's *A Grammar of the Kashmiri Language* (1888)
  - Jawahar Lal & Lalita Handoo's *Hindi-Kashmiri Common Vocabulary* (1975)
  - Anand Koul's *Kashmiri Riddles* (1933)
  - T. Grahame Bailey's *The Pronunciation of Kashmiri* (1937)
- **Intermediate Level (13 volumes, ~819k words)**:
  - Omkar N. Koul's *An Intermediate Course in Kashmiri* (1995)
  - Prof. Shafi Shauq's *Kạ̄shrik Grammar* (1985)
  - CIIL's *Hindi-Kashmiri-English Trilingual Dictionary* (1988)
  - Omkar N. Koul's *Kashmiri-English Dictionary* (2005)
  - Omkar Kaul's *Gile Tori: Kashmiri Short Stories* (1992)
  - Koul, Bhat & Raina's *Kashmiri-English Dictionary for Second Language Learners* (2000)
  - J. Hinton Knowles' *A Dictionary of Kashmiri Proverbs and Sayings* (1885)
  - J. Hinton Knowles' *Folk-Tales of Kashmir* (1888)
  - Lalita Handoo's *Structural Analysis of Kashmiri Folk Tales* (1994)
  - J. L. Kaul's *Kashmiri Lyrics* (1945)
  - Omkar N. Koul's *Kashmiri Language, Linguistics and Culture* (2000)
  - Triloki Nath Raina's *A History of Kashmiri Literature* (2002)
  - Hatim Tilawöñ, Aurel Stein & Grierson's *Hatim's Tales: Kashmiri Stories and Songs* (1923)
- **Advanced Level (29 volumes, ~3.35M words)**:
  - J&K Cultural Academy's monumental *Kashir Dictionary* (Volumes 1, 2, 3, 7 by S.K. Toshakhani, J.L. Koul, Mohi-ud-Din Hajni, P.N. Pushp, Mohi-ud-Din Akhtar)
  - Dr. G. M. D. Sufi's monumental *Kāshīr: Being a History of Kashmir* (Vol. 1 & Vol. 2 on Literature, Arts, and Culture, 1948–1949)
  - Sir George Grierson's monumental *A Dictionary of the Kashmiri Language* (1932, over 1 million words)
  - Pandit Ishvara Kaula & Grierson's *The Kāśmīraśabdāmṛta: A Kashmiri Grammar in Sanskrit* (1898)
  - Omkar N. Koul & Kashi Wali's *Modern Kashmiri Grammar* (2006)
  - Grierson's *Linguistic Survey of India: Dardic & Kashmiri* (Vol. VIII, Part II, 1919)
  - Dr. William Jackson Elmslie's *A Vocabulary of the Kashmiri Language* (1872)
  - Sir Aurel Stein's *Kalhana's Rajatarangini: A Chronicle of the Kings of Kasmir* (Vol. 1 & Vol. 2 with Ancient Topography, 1900)
  - Dr. Ved Kumari Ghai's *The Nilamata Purana* (Vol. 1, 1968)
  - Grierson & Barnett's *Lalla-Vakyani or The Wise Sayings of Lal Ded* (1920)
  - Divakara Prakasa Bhatta's *The Kashmiri Ramayana* (1930)
  - Krishna Razdan & Grierson's *Śivapariṇayaḥ: A Poem in the Kashmiri Language* (1913)
  - Dinanath & Grierson's *Śrī Kṛṣṇāvatāra Līlā of Dinanath in Kashmiri* (1928)
  - Sir Aurel Stein's *Catalogue of the Sanskrit & Kashmiri Manuscripts in the Raghunatha Temple Library* (1894)
  - Sir Walter Roper Lawrence's *The Valley of Kashmir* (1895)
  - Sir Richard Carnac Temple's *The Word of Lalla the Prophetess* (1924, Cambridge University Press)
  - Pandit Anand Koul's *The Kashmiri Pandit: Early History, Social Customs, Language, and Folklore* (1924)
  - Dr. Georg Bühler's *Detailed Report of a Tour in Search of Sanskrit MSS. in Kasmir* (1877)
  - Godfrey Thomas Vigne's *Travels in Kashmir, Ladak, Iskardo* (1842)
  - Jogesh Chunder Dutt's *Kings of Kashmira* (Vols. 1, 2, 3 - Chronicles of Kalhana, Jonaraja, Srivara, Prajyabhatta)
  - Sir George Abraham Grierson's *Essays on Kashmiri Grammar* (1899)
  - François Bernier's *Travels in the Mogul Empire: Journey to the Kingdom of Kachemire* (1665)
  - Academic Research Papers: Hook & Koul (V2 syntax, split ergativity, sarcasm), Wali & Koul (clitics & agreement), Bhatt (verb movement), Pandey (Sharada Unicode standard), Morgenstierne (Dardic affinities), Grierson (on the Sarada alphabet).

```python
import koshur

# 1. Corpus Statistics
stats = koshur.get_library_stats()
print(f"Total Volumes: {stats['total_volumes']}")       # 60
print(f"Total Words:   {stats['total_words']:,d}")      # 5,513,958
print(f"Levels:        {stats['level_counts']}")        # elementary: 8, intermediate: 15, advanced: 37

# 2. Filter by Learning Progression Level
elementary = koshur.get_sources_by_level("elementary")
intermediate = koshur.get_sources_by_level("intermediate")
advanced = koshur.get_sources_by_level("advanced")

# 3. Filter Sources by Category
books = koshur.get_sources_by_category("books")
discourses = koshur.get_sources_by_category("discourses")
papers = koshur.get_sources_by_category("papers")

# 4. Full-Text Search across 5.51M+ Words
results = koshur.search_library_text("vitasta", max_results=5)
for r in results:
    print(f"[{r['file']} L{r['line_number']}]: {r['snippet']}")

# 5. Read Primary Texts & Papers Directly
excerpt = koshur.read_library_source("hook_koul_1996_v2", max_chars=400)
print(excerpt)
```

---

## Command Line Interface (CLI)

The `koshur` CLI provides rich terminal tools with automatic UTF-8 terminal encoding support:

```bash
# 1. Multi-script transliteration
python -m koshur.cli transliterate "Vyeth" --to sharada
python -m koshur.cli transliterate "व्यथ्" --to persoarabic

# 2. Dictionary lookup & search (570+ entries)
python -m koshur.cli lookup "tumbaknari"
python -m koshur.cli lookup "sharika"
python -m koshur.cli search "chai"
python -m koshur.cli search --tag music

# 3. Folklore Genres & Traditional Songs
python -m koshur.cli folklore --genres
python -m koshur.cli folklore --genre wanvun
python -m koshur.cli folklore --songs
python -m koshur.cli folklore --song habba_khatoon_roshe
python -m koshur.cli folklore --search "habba"

# 4. Sacred Deities, Tirthas & Ashta Bhairavas
python -m koshur.cli deity --name "sharika"
python -m koshur.cli deity --name "kheer bhawani"
python -m koshur.cli deity --bhairavas
python -m koshur.cli deity --all

# 5. Web & App Localization (i18n & WebFonts)
python -m koshur.cli i18n --key home --script devanagari
python -m koshur.cli i18n --key save --script persoarabic
python -m koshur.cli keyboard --script devanagari
python -m koshur.cli webfonts --script sharada

# 6. Kashmiri Date, Time & Calendar
python -m koshur.cli date --script devanagari
python -m koshur.cli date --script persoarabic
python -m koshur.cli date --calendar navreh

# 7. Fieldwork & Research: Leipzig Interlinear Gloss, Corpus Metrics & Source Catalog
python -m koshur.cli gloss --source "aslam-an por akhavbar" --gloss "Aslam-ERG read.PST newspaper" --translation "Aslam read the newspaper."
python -m koshur.cli metrics --text "सु छु किताब परान। सो छ़े चाय चवान।"
python -m koshur.cli sources --search "Grierson"
python -m koshur.cli sources --all

# 8. Traditional proverbs & vakhs (30 authentic maxims)
python -m koshur.cli proverb --random
python -m koshur.cli proverb --search "secret"
python -m koshur.cli proverb --all

# 9. J&K Land revenue records & cadastral converter (79 terms)
python -m koshur.cli revenue --list
python -m koshur.cli revenue --category Deed
python -m koshur.cli revenue --search mortgage
python -m koshur.cli revenue --term jamabandi
python -m koshur.cli area --kanals 4 --marlas 12

# 10. Khat-i-Shikast Palaeography & Archival Decipherment
python -m koshur.cli shikasta --rules
python -m koshur.cli shikasta --rule alif
python -m koshur.cli shikasta --abbrevs
python -m koshur.cli shikasta --abbrev al_abd
python -m koshur.cli shikasta --weight 10 tolas
python -m koshur.cli shikasta --currency 25 12 2
python -m koshur.cli shikasta --fasli

# 11. Government Revenue Records Translation & Web App (English & Hindi)
python -m koshur.cli record-translate --list-samples
python -m koshur.cli record-translate --sample jamabandi_shalimar --lang hi
python -m koshur.cli record-translate --sample bainama_pampore --lang en
python -m koshur.cli record-translate --sample intiqal_virasat --lang both
python -m koshur.cli record-translate --sample jamabandi_shalimar --lang hi --html --output cert_hi.html
python -m koshur.cli record-translate --serve --port 8080
python -m koshur.cli translator-web

# 12. Kashmiri numeral conversion
python -m koshur.cli number 42 --script roman
python -m koshur.cli number 42 --script devanagari

# 11. Comparative dialectology
python -m koshur.cli compare "brother"
python -m koshur.cli compare "snow"
python -m koshur.cli dialect kishtwari

# 12. Grammar declension & V2 syntax
python -m koshur.cli grammar --noun "larka"
python -m koshur.cli grammar --verb "parun"
python -m koshur.cli grammar --syntax "राजू छु च्योन ख्यवान"

# 13. Phonetics & 16-Vowel Inventory table
python -m koshur.cli phonology --vowels
python -m koshur.cli phonology --ipa "कॉशुर"

# 14. Text linguistic analysis
python -m koshur.cli analyze "अमी पनॳ सोदरस नावि छस लमान।"

# 15. Digital Linguistics Library (3.34M+ words across 38 volumes)
python -m koshur.cli library --stats
python -m koshur.cli library
python -m koshur.cli library --level elementary
python -m koshur.cli library --level intermediate
python -m koshur.cli library --level advanced
python -m koshur.cli library --category books
python -m koshur.cli library --category discourses
python -m koshur.cli library --category papers
python -m koshur.cli library --search "vitasta"
python -m koshur.cli library --search "pheran"
python -m koshur.cli library --info kalhana_rajatarangini_vol1
python -m koshur.cli library --read hook_koul_1996_v2 --chars 500
```

---

## Academic & Research References

The library is built upon verified primary literature, lexicographical fieldwork, and epigraphic archives:

1. **Stein, Sir M. Aurel & Grierson, Sir George A.** (1923). *Hatim's Tales: Kashmiri Stories and Songs*. Recorded in Phonetic Transcription with Translations and Vocabulary from Hatim Tilawōny of Arigom. John Murray, London. [Archive](https://archive.org/details/taleskashmiristo00hatiuoft).
2. **Ghai, Dr. Ved Kumari** (1968). *The Nīlamata Purāṇa: A Cultural and Literary Study of a Kashmiri Purāṇa*. (Vol. 1: Cultural Study; Vol. 2: Sanskrit Text & English Translation). J&K Academy of Art, Culture and Languages, Srinagar.
3. **Grierson, Sir George Abraham** (1916–1932). *A Dictionary of the Kashmiri Language*. Compiled partly from materials left by the late Pandit Iśvara Kaula, assisted by Mahāmahopādhyāya Mukundarāma Śāstrī. Asiatic Society of Bengal / Royal Asiatic Society, Calcutta. [Archive](https://archive.org/details/dictionaryofkash01grieuoft).
4. **Grierson, Sir George Abraham** (1911). *A Manual of the Kashmiri Language: Comprising Grammar, Phrase-Book and Vocabularies* (Vol. 1: Grammar; Vol. 2: Kashmiri-English Vocabulary). Clarendon Press, Oxford. [Archive](https://archive.org/details/hdsK_standard-manual-of-the-kashmiri-language-vol-2-by-george-a.-grierson-kashmiri-en).
5. **Elmslie, Dr. William Jackson** (1872). *A Vocabulary of the Kashmiri Language* (In Two Parts: English-Kashmiri and Kashmiri-English). Church Missionary Society / Harrison & Sons, London. [Archive](https://archive.org/details/avocavularykash00elmsgoog).
6. **Knowles, Rev. J. Hinton** (1885). *A Dictionary of Kashmiri Proverbs and Sayings*. Education Society's Press, Bombay / Trübner & Co., London. [Archive](https://archive.org/details/dictionaryofkash014372mbp).
7. **Handoo, Dr. Jawahar Lal & Handoo, Dr. Lalita** (1975). *Hindi-Kashmiri Common Vocabulary*. Central Institute of Indian Languages (CIIL), Mysore. [Archive](https://archive.org/details/hindi-kashmiri-common-vocabulary-jawahar-lal-and-lalita-handoo).
8. **Kaul, Dr. Hari Krishna** (2000). *Vyeth-Vyatha: A Kashmiri Socio-Literary & Historical Study* (व्यथ-व्यथा). Srinagar / Jammu. Primary study on Kashmiri linguistic heritage and Vitasta literary tradition.
9. **Archaeological Survey of India** (1987). *Epigraphia Indica: Arabic & Persian Supplement 1951-54* (In continuation of Epigraphia Indo-Moslemica). Ed. K.V. Ramesh & Z.A. Desai. ASI, New Delhi (Acc. No. 75129, Call No. 417.6105).
10. **Kaula, Pandit Iśvara** (1898). *Kāśmīraśabdāmṛta: A Grammar of the Kashmiri Language in Sanskrit*. Ed. George A. Grierson. Asiatic Society of Bengal, Calcutta.
11. **Koul, Pandit Anand** (1933). *Kashmiri Proverbs*. Calcutta.
12. **Lal Ded (Lalleshwari) & Sheikh Noor-ud-Din Wali (Nund Rishi)** (14th century). *Lalla Vakyani and Shruk Traditions: Foundations of Classical Kashmiri Poetic Metre and Philosophical Lexicon*.
13. **Wali, Kashi & Koul, Ashok K.** (1997). *Kashmiri: A Cognitive-Descriptive Grammar*. Routledge, London & New York.
14. **Bhatt, Rakesh M.** (1999). *Verb Movement and Code-Switching: The Structure of Kashmiri*. Cambridge University Press.
15. **Pandey, Anshuman** (2012). *Proposal to Encode the Sharada Script in ISO/IEC 10646*. Unicode Technical Committee Document L2/12-124.
16. **Govt. of Jammu and Kashmir** (Financial Commissioner Revenue). *The Jammu and Kashmir Land Revenue Act, Samvat 1996 (1939 A.D.) and Land Records Manual*.
17. **Siddiqi, Maulvi Mohammad Ashfaq** (1940). *Majmu'a Khat-i-Shikast: Kaghazat-i-Karrawai* (?????? ??? ?????: ??????? ????????). Board of High School & Intermediate Education UP & J&K Revenue Archives.
18. **Faruqi, Mohammad Tahir & Rizvi, Sayed Tawakkul Husain** (1928). *A Text-Book of Khat-i-Shikast or Maktoobat-i-Akhgar* (???? ??? ????? ?? ???????? ????). Educational Press.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

*Dedicated to the enduring literary and cultural heritage of Kashmir (कॉशुर / کٲشُر / 𑆯𑆳𑆫𑆢𑆳).*
