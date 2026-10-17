"""
Research Sources & Bibliographic Reference Catalog:
Provides programmatic access to the historical, lexicographical,
grammatical, and epigraphic primary sources powering the Koshur library,
including downloaded full-text volumes, manuscripts catalogues, discourses, and papers.
"""

from typing import List, Dict, Any, Optional
import os
import json

HISTORICAL_SOURCES: List[Dict[str, Any]] = [
    {
        "id": "grierson_dict_1932",
        "title": "A Dictionary of the Kashmiri Language",
        "authors": ["Sir George Abraham Grierson", "Pandit Iśvara Kaula", "Mahāmahopādhyāya Mukundarāma Śāstrī"],
        "year": 1932,
        "publisher": "Royal Asiatic Society of Bengal / Bibliotheca Indica, Calcutta",
        "description": "The definitive comprehensive four-part lexicon of classical and modern Kashmiri, compiled partly from Pandit Ishvara Kaula's materials with Devanagari, Perso-Arabic, Roman transliteration, and Sanskrit glosses.",
        "domains": ["lexicography", "morphology", "etymology", "comparative"],
        "category": "books",
        "archive_id": "dictionaryofkash01grieuoft"
    },
    {
        "id": "grierson_manual_1911",
        "title": "A Manual of the Kashmiri Language (Vol. 1: Grammar; Vol. 2: Kashmiri-English Vocabulary)",
        "authors": ["Sir George Abraham Grierson"],
        "year": 1911,
        "publisher": "Clarendon Press, Oxford",
        "description": "Standard pedagogical and reference manual containing systematic noun declensions across classes 1-6, split-ergative past tenses, V2 syntax rules, phrasebook, and extensive vocabulary.",
        "domains": ["grammar", "syntax", "pedagogy", "vocabulary"],
        "category": "books",
        "archive_id": "hdsK_standard-manual-of-the-kashmiri-language-vol-2-by-george-a.-grierson-kashmiri-en"
    },
    {
        "id": "elmslie_vocab_1872",
        "title": "A Vocabulary of the Kashmiri Language",
        "authors": ["Dr. William Jackson Elmslie"],
        "year": 1872,
        "publisher": "Church Missionary Society / Harrison & Sons, London",
        "description": "Pioneering English-Kashmiri and Kashmiri-English medical and conversational vocabulary compiled during missionary medical work in Srinagar, documenting anatomical, flora, and domestic terms.",
        "domains": ["vocabulary", "lexicography", "anatomy", "ethnobotany"],
        "category": "books",
        "archive_id": "avocavularykash00elmsgoog",
        "local_file": "books/elmslie_1872_vocabulary.txt"
    },
    {
        "id": "knowles_proverbs_1885",
        "title": "A Dictionary of Kashmiri Proverbs and Sayings",
        "authors": ["Rev. J. Hinton Knowles"],
        "year": 1885,
        "publisher": "Education Society's Press, Bombay / Trübner & Co., London",
        "description": "Comprehensive folk repository of Kashmiri oral wisdom, idioms (kahan / masal), and cultural metaphors with literal translations and sociological folklore commentary.",
        "domains": ["folklore", "proverbs", "idioms", "sociolinguistics"],
        "category": "books",
        "archive_id": "dictionaryofkash014372mbp",
        "local_file": "books/knowles_1885_proverbs.txt"
    },
    {
        "id": "handoo_common_vocab_1975",
        "title": "Hindi-Kashmiri Common Vocabulary",
        "authors": ["Dr. Jawahar Lal Handoo", "Dr. Lalita Handoo"],
        "year": 1975,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "description": "Comparative linguistic analysis mapping shared Indo-Aryan cognates, semantic shifts, and morphological correspondences across Kashmiri (Devanagari & Perso-Arabic) and Modern Standard Hindi.",
        "domains": ["comparative_linguistics", "cognates", "semantics", "pedagogy"],
        "category": "books",
        "archive_id": "hindi-kashmiri-common-vocabulary-jawahar-lal-and-lalita-handoo",
        "local_file": "books/handoo_1975_common_vocab.txt"
    },
    {
        "id": "kaul_vyeth_vyatha_2000",
        "title": "Vyeth-Vyatha: Vitasta Tat Par Koshur Samajik evam Sahityik Adhyayan (व्यथ-व्यथा)",
        "authors": ["Dr. Hari Krishna Kaul (डॉ. हरिकृष्ण कौल)"],
        "year": 2000,
        "publisher": "Srinagar / Jammu",
        "description": "Authoritative literary and socio-historical treatise analyzing the Vitasta (Jhelum) civilization, ancient toponyms, Sharada manuscript tradition, Shaivite philosophy, and the evolution of the Kashmiri language.",
        "domains": ["sociolinguistics", "history", "sharada_tradition", "philosophy"],
        "category": "discourses",
        "local_source": "Vyeth Vyetha.pdf"
    },
    {
        "id": "asi_epigraphia_indica_1987",
        "title": "Epigraphia Indica: Arabic & Persian Supplement 1951-54 (In continuation of Epigraphia Indo-Moslemica)",
        "authors": ["Archaeological Survey of India (Director General: K.V. Ramesh / Z.A. Desai)"],
        "year": 1987,
        "publisher": "Archaeological Survey of India, Janpath, New Delhi",
        "description": "Scholarly epigraphic corpus of Sultanate and Mughal monumental inscriptions from Kashmir, Delhi, Gujarat, and Bengal, documenting historical shikasta/naskh paleography (Acc. No. 75129, Call No. 417.6105).",
        "domains": ["epigraphy", "paleography", "persoarabic_script", "history"],
        "category": "catalogues",
        "local_source": "75129.pdf"
    },
    {
        "id": "anand_koul_proverbs_1933",
        "title": "Kashmiri Proverbs",
        "authors": ["Pandit Anand Koul"],
        "year": 1933,
        "publisher": "Calcutta",
        "description": "Collection of traditional Kashmiri proverbs, vakhs, and philosophical idioms preserving oral cultural heritage.",
        "domains": ["folklore", "proverbs", "vakhs"],
        "category": "books"
    },
    {
        "id": "isvara_kaula_sabdamrta_1898",
        "title": "Kāśmīraśabdāmṛta (A Grammar of the Kashmiri Language in Sanskrit)",
        "authors": ["Pandit Iśvara Kaula", "Edited by George A. Grierson"],
        "year": 1898,
        "publisher": "Asiatic Society of Bengal, Calcutta",
        "description": "The seminal indigenous Paninian Sanskrit treatise systematically codifying Kashmiri phonology, matsaryar palatalization, noun declensions, and verb conjugations.",
        "domains": ["paninian_grammar", "morphology", "phonology", "sanskrit_tradition"],
        "category": "books"
    },
    {
        "id": "lal_ded_nund_rishi_14th_c",
        "title": "Lalla Vakyani & Shruk Tradition (Foundational Classical Poetic Corpus)",
        "authors": ["Lalleshwari (Lal Ded)", "Sheikh Noor-ud-Din Wali (Nund Rishi)"],
        "year": 1380,
        "publisher": "Oral Tradition & 17th-c. Sharda/Persian recensions (Grierson & Barnett 1920)",
        "description": "14th-century mystical verse corpus establishing the foundation of Kashmiri poetic meter, spiritual lexicon, and Trika Shaivite/Rishi-Sufi synthesis.",
        "domains": ["classical_poetry", "trika_shaivism", "rishi_sufism", "mysticism"],
        "category": "discourses"
    },
    # --- Expanded Library Volumes (Downloaded Full Texts & Catalogues) ---
    {
        "id": "kalhana_rajatarangini_stein_vol1",
        "title": "Kalhana's Rajatarangini: A Chronicle of the Kings of Kashmir (Vol. 1)",
        "authors": ["Kalhana", "Sir M. Aurel Stein (Translator & Editor)"],
        "year": 1900,
        "publisher": "Archibald Constable & Co., London",
        "description": "Monumental 12th-century Sanskrit chronicle and moral discourse on Kashmir history, topography, ancient shrine toponyms, and Vitasta valley geography.",
        "domains": ["history", "chronicles", "toponymy", "sacred_geography"],
        "category": "discourses",
        "archive_id": "dli.pahar.1527",
        "local_file": "discourses/kalhana_rajatarangini_stein_vol1.txt"
    },
    {
        "id": "grierson_1919_lsi_dardic",
        "title": "Linguistic Survey of India (Vol. VIII, Part II: Specimens of the Dardic or Pisacha Languages)",
        "authors": ["Sir George Abraham Grierson"],
        "year": 1919,
        "publisher": "Superintendent Government Printing, Calcutta",
        "description": "Foundational comparative linguistic survey covering Kashmiri grammar, standard dialects (Kishtwari, Poguli, Siraji, Rambani), and Dardic language specimens.",
        "domains": ["dialectology", "comparative_linguistics", "grammar", "phonology"],
        "category": "books",
        "archive_id": "in.ernet.dli.2015.32109",
        "local_file": "books/grierson_1919_lsi_vol8_part2_dardic.txt"
    },
    {
        "id": "knowles_1888_folktales",
        "title": "Folk-Tales of Kashmir",
        "authors": ["Rev. J. Hinton Knowles"],
        "year": 1888,
        "publisher": "Trübner & Co., London",
        "description": "Comprehensive authentic collection of 64 traditional Kashmiri folk stories, legends, fairy tales, and oral wisdom recorded directly from village storytellers.",
        "domains": ["folklore", "oral_literature", "sociolinguistics"],
        "category": "books",
        "archive_id": "folktalesofkashm00knowuoft",
        "local_file": "books/knowles_1888_folktales.txt"
    },
    {
        "id": "hatims_tales_1923",
        "title": "Hatim's Tales: Kashmiri Stories and Songs",
        "authors": ["Hatim Tilawōny", "Sir M. Aurel Stein", "Sir George A. Grierson"],
        "year": 1923,
        "publisher": "John Murray, London",
        "description": "Primary linguistic and folklore corpus recorded in phonetic transcription from Hatim Tilawōny of Arigom with word-for-word interlinear translations and vocabulary.",
        "domains": ["folklore", "oral_corpus", "phonetics", "vocabulary"],
        "category": "discourses",
        "archive_id": "dli.ministry.02518",
        "local_file": "discourses/hatims_tales_1923.txt"
    },
    {
        "id": "stein_1894_raghunatha",
        "title": "Catalogue of the Sanskrit & Kashmiri Manuscripts in the Raghunatha Temple Library",
        "authors": ["Sir M. Aurel Stein"],
        "year": 1894,
        "publisher": "Messrs. Luzac & Co., London / Nirnaya Sagara Press, Bombay",
        "description": "Authoritative descriptive catalogue of over 4,500 manuscripts (including Sharada birch-bark manuscripts of Kashmir Shaivism, Paninian grammar, and literature).",
        "domains": ["catalogues", "manuscripts", "sharada_script", "palaeography"],
        "category": "catalogues",
        "archive_id": "SanskritManuscriptsInRaghunathTempleLibraryM.A.Stein",
        "local_file": "catalogues/stein_1894_raghunatha_manuscripts.txt"
    },
    {
        "id": "nilamata_purana_vol1",
        "title": "The Nilamata Purana (Vol. 1: Cultural and Literary Study of a Kashmiri Purana)",
        "authors": ["Dr. Ved Kumari Ghai"],
        "year": 1968,
        "publisher": "J&K Academy of Art, Culture and Languages, Srinagar",
        "description": "Seminal study of the ancient sacred purana of Kashmir, detailing the origin of the Vitasta valley, Nagas, traditional festivals, and sacred geography.",
        "domains": ["purana", "sacred_geography", "nagas", "culture"],
        "category": "discourses",
        "archive_id": "the-nilamata-purana-vol-1-dr.-ved-kumari-ghai",
        "local_file": "discourses/nilamata_purana_vol1.txt"
    },
    {
        "id": "kashmiri_ramayana_1930",
        "title": "The Kashmiri Ramayana (Sriramavataracarita)",
        "authors": ["Divakara Prakasa Bhatta", "Sir George A. Grierson (Editor)"],
        "year": 1930,
        "publisher": "Asiatic Society of Bengal, Bibliotheca Indica, Calcutta",
        "description": "Late 18th-century classical Kashmiri poetic epic narrative preserving authentic Kashmiri idiom, metric structures, and vocabulary.",
        "domains": ["classical_poetry", "epic", "literature", "idioms"],
        "category": "discourses",
        "archive_id": "in.ernet.dli.2015.48970",
        "local_file": "discourses/kashmiri_ramayana_1930.txt"
    },
    {
        "id": "lalla_vakyani_1920",
        "title": "Lalla-Vakyani or The Wise Sayings of Lal-Ded",
        "authors": ["Lalleshwari (Lal Ded)", "Sir George A. Grierson", "Dr. Lionel D. Barnett"],
        "year": 1920,
        "publisher": "Royal Asiatic Society, London",
        "description": "The foundational 14th-century mystic verses (vakhs) of Yogini Lalleshwari (Lal Ded) with word-by-word Sanskrit glosses, English translation, and complete vocabulary.",
        "domains": ["classical_poetry", "trika_shaivism", "mysticism", "vakhs"],
        "category": "discourses",
        "archive_id": "dli.ernet.544299",
        "local_file": "discourses/lalla_vakyani_1920.txt"
    },
    {
        "id": "raina_history_literature",
        "title": "A History of Kashmiri Literature",
        "authors": ["Triloki Nath Raina"],
        "year": 2002,
        "publisher": "Sahitya Akademi, New Delhi",
        "description": "Comprehensive historical and critical treatise covering seven centuries of Kashmiri literature from Shitikantha to modern poets.",
        "domains": ["literary_history", "poetry", "criticism"],
        "category": "books",
        "archive_id": "a-history-of-kashmiri-literature-triloki-nath-raina",
        "local_file": "books/raina_history_kashmiri_literature.txt"
    },
    {
        "id": "koul_studies_linguistics",
        "title": "Studies in Kashmiri Linguistics",
        "authors": ["Prof. Omkar N. Koul"],
        "year": 2005,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "description": "Scholarly research papers on Kashmiri phonetics, morphology, syntax, sociolinguistics, and language pedagogy.",
        "domains": ["linguistics", "phonetics", "syntax", "pedagogy"],
        "category": "books",
        "archive_id": "studies-in-kashmiri-linguistics-omkar-n-koul",
        "local_file": "books/koul_studies_linguistics.txt"
    },
    {
        "id": "wade_1888_grammar",
        "title": "A Grammar of the Kashmiri Language",
        "authors": ["Rev. T. Russell Wade"],
        "year": 1888,
        "publisher": "Society for Promoting Christian Knowledge, London",
        "description": "Systematic pioneer grammar of spoken Kashmiri covering noun declensions, pronouns, verb conjugations, and syntax.",
        "domains": ["grammar", "morphology", "syntax"],
        "category": "books",
        "archive_id": "in.ernet.dli.2015.458430",
        "local_file": "books/wade_1888_grammar.txt"
    },
    {
        "id": "kaul_1945_lyrics",
        "title": "Kashmiri Lyrics: Selected and Translated",
        "authors": ["Pandit J. L. Kaul"],
        "year": 1945,
        "publisher": "Rinemisray, Srinagar",
        "description": "Anthology of classic Kashmiri lyrical poetry including Habba Khatoon, Rasul Mir, Arnimal, and Mahmud Gami.",
        "domains": ["poetry", "lyrics", "translation"],
        "category": "books",
        "archive_id": "in.ernet.dli.2015.102721",
        "local_file": "books/kaul_1945_kashmiri_lyrics.txt"
    },
    {
        "id": "koul_1933_riddles",
        "title": "Kashmiri Riddles",
        "authors": ["Pandit Anand Koul"],
        "year": 1933,
        "publisher": "Calcutta",
        "description": "Traditional Kashmiri cultural riddles (praatshik) and word games preserving indigenous vernacular expressions.",
        "domains": ["folklore", "riddles", "culture"],
        "category": "books",
        "archive_id": "KashmiriRiddlesKoul",
        "local_file": "books/koul_1933_kashmiri_riddles.txt"
    },
    # --- Peer-Reviewed Academic Papers ---
    {
        "id": "hook_koul_1996_v2",
        "title": "V-2 and the Verb Complex in Kashmiri",
        "authors": ["Peter Edwin Hook", "Omkar N. Koul"],
        "year": 1996,
        "publisher": "Bahri Publications / South Asian Language Review",
        "description": "Foundational syntactic study establishing the Verb-Second (V2) root clause constraint, finite auxiliary positioning, and clitic clustering.",
        "domains": ["syntax", "v2_word_order", "verb_complex", "typology"],
        "category": "papers",
        "local_file": "papers/hook_koul_1996_v2_syntax.txt"
    },
    {
        "id": "hook_koul_1984_ergativity",
        "title": "Pronominal Suffixes and Split Ergativity in Kashmiri",
        "authors": ["Peter Edwin Hook", "Omkar N. Koul"],
        "year": 1984,
        "publisher": "Bahri Publications / Aspects of Kashmiri Linguistics",
        "description": "Syntactic analysis of aspectual split ergativity, 4 noun declension classes, and verb pronominal suffixes.",
        "domains": ["ergativity", "morphology", "noun_declension", "clitics"],
        "category": "papers",
        "local_file": "papers/hook_koul_1984_split_ergativity.txt"
    },
    {
        "id": "wali_koul_1994_clitics",
        "title": "Kashmiri Clitics and Agreement",
        "authors": ["Kashi Wali", "Ashok K. Koul"],
        "year": 1994,
        "publisher": "Linguistic Inquiry / Topics in South Asian Linguistics",
        "description": "Analysis of pronominal clitic docking on V2 finite verbs, clitic doubling, and hierarchical person agreement.",
        "domains": ["syntax", "clitics", "agreement"],
        "category": "papers",
        "local_file": "papers/wali_koul_1994_clitics_agreement.txt"
    },
    {
        "id": "bhatt_1999_verb_movement",
        "title": "Verb Movement and the Syntax of Kashmiri",
        "authors": ["Rakesh M. Bhatt"],
        "year": 1999,
        "publisher": "Kluwer Academic Publishers / Studies in Natural Language and Linguistic Theory",
        "description": "Generative minimalist analysis of I-to-C movement, topic-first positioning, and wh-fronting in Kashmiri.",
        "domains": ["generative_syntax", "verb_movement", "minimalism"],
        "category": "papers",
        "local_file": "papers/bhatt_1999_verb_movement.txt"
    },
    {
        "id": "pandey_2012_sharada",
        "title": "Proposal to Encode the Sharada Script in ISO/IEC 10646",
        "authors": ["Anshuman Pandey"],
        "year": 2012,
        "publisher": "Unicode Technical Committee Document L2/12-124",
        "description": "Comprehensive palaeographic and orthographic analysis of Sharada ligatures, matras, virama, and Kashmiri signs encoded in Unicode U+11180-U+111DF.",
        "domains": ["sharada_script", "unicode", "palaeography", "epigraphy"],
        "category": "papers",
        "local_file": "papers/pandey_2012_sharada_unicode.txt"
    },
    {
        "id": "bailey_1937_pronunciation",
        "title": "The Pronunciation of Kashmiri: Kashmiri Sounds, How to Make Them and How to Transcribe Them",
        "authors": ["T. Grahame Bailey"],
        "year": 1937,
        "publisher": "Royal Asiatic Society, London (James G. Forlong Fund Vol. XVI)",
        "description": "Pioneering phonetic investigation into the 16 vowels, central unrounded vowels (ɨ, ə), and matra-vowel palatalization rules.",
        "domains": ["phonetics", "phonology", "16_vowels", "transcription"],
        "category": "papers",
        "local_file": "papers/bailey_1937_kashmiri_pronunciation.txt"
    },
    {
        "id": "morgenstierne_1941_dardic",
        "title": "Dardic and the Linguistic Position of Kashmiri",
        "authors": ["Georg Morgenstierne"],
        "year": 1941,
        "publisher": "Acta Orientalia",
        "description": "Classification of Dardic within the Indo-Aryan family and preservation of archaic consonant clusters in Kishtwari.",
        "domains": ["dardic", "comparative_linguistics", "kishtwari"],
        "category": "papers",
        "local_file": "papers/morgenstierne_1941_dardic_kashmiri.txt"
    },
    {
        "id": "hook_koul_2022_sarcasm",
        "title": "A Dedicated Sarcasm Construction in Kashmiri as a Feature of the South Asian Linguistic Area",
        "authors": ["Peter Edwin Hook", "Omkar N. Koul"],
        "year": 2022,
        "publisher": "Bhasha: Journal of South Asian Linguistics, Philology and Culture",
        "description": "Analysis of grammaticalized conversational sarcasm and pragmatic polarity in Kashmiri using enclitic -ay.",
        "domains": ["pragmatics", "discourse", "sociolinguistics"],
        "category": "papers",
        "local_file": "papers/hook_koul_2022_dedicated_sarcasm.txt"
    },
    # --- Newly Integrated Elementary, Intermediate, and Advanced Library Volumes ---
    {
        "id": "bhat_2007_course_kashmiri",
        "title": "A Course in Kashmiri Language",
        "authors": ["Dr. Roop Krishen Bhat"],
        "year": 2007,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "description": "Introductory pedagogical coursebook for second language learners covering basic Kashmiri phonology, greetings, case suffixes, verb stems, and conversational dialogues.",
        "domains": ["pedagogy", "conversation", "elementary_grammar", "second_language"],
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.language.0066",
        "local_file": "books/bhat_2007_course_in_kashmiri.txt"
    },
    {
        "id": "koul_1987_spoken_kashmiri",
        "title": "Spoken Kashmiri: A Language Course",
        "authors": ["Prof. Omkar N. Koul"],
        "year": 1987,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "description": "Foundational introductory textbook structured in graded lessons, drills, structural notes, everyday dialogues, and elementary vocabulary.",
        "domains": ["spoken_kashmiri", "dialogues", "elementary_grammar", "pedagogy"],
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.language.0846",
        "local_file": "books/koul_1987_spoken_kashmiri.txt"
    },
    {
        "id": "shauq_kashmiri_reader",
        "title": "Kashmiri English Hindi Reader",
        "authors": ["Prof. Shafi Shauq"],
        "year": 1990,
        "publisher": "University of Kashmir / Cultural Academy, Srinagar",
        "description": "Graded multilingual reader featuring short stories, cultural essays, everyday prose, and parallel sentence-level English and Hindi glosses.",
        "domains": ["graded_reader", "trilingual", "stories", "elementary"],
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.ernet.509601",
        "local_file": "books/shauq_kashmiri_reader.txt"
    },
    {
        "id": "koul_intermediate_course",
        "title": "An Intermediate Course in Kashmiri",
        "authors": ["Prof. Omkar N. Koul"],
        "year": 1995,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "description": "Bridge textbook advancing from basic grammar to complex sentence construction, relative clauses, compound verbs, and cultural discourse.",
        "domains": ["intermediate_grammar", "syntax", "compound_verbs", "pedagogy"],
        "category": "books",
        "level": "intermediate",
        "archive_id": "mjnv-an-intermediate-course-in-kashmiri-omkar-m.-koul",
        "local_file": "books/koul_intermediate_course_kashmiri.txt"
    },
    {
        "id": "koul_2000_dictionary_second_language",
        "title": "Kashmiri-English Dictionary for Second Language Learners",
        "authors": ["Prof. Omkar N. Koul", "Dr. Roop Krishen Bhat", "Prof. S. N. Raina"],
        "year": 2000,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "description": "Comprehensive learner-oriented dictionary with grammatical category labels, phonemic Roman transliteration, illustrative sentences, and English glosses.",
        "domains": ["lexicography", "pedagogy", "learner_dictionary", "vocabulary"],
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.2243",
        "local_file": "books/koul_2000_dictionary_second_language.txt"
    },
    {
        "id": "handoo_1994_folk_analysis",
        "title": "Structural Analysis of Kashmiri Folk Tales",
        "authors": ["Dr. Lalita Handoo"],
        "year": 1994,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "description": "Deep morphological and structural analysis applying Proppian narratology and folkloric motifs to Kashmiri oral tales and fairy lore.",
        "domains": ["folklore", "narratology", "structuralism", "morphology"],
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.1960",
        "local_file": "books/handoo_1994_structural_analysis_folk_tales.txt"
    },
    {
        "id": "koul_2000_linguistics_culture",
        "title": "Kashmiri Language, Linguistics and Culture",
        "authors": ["Prof. Omkar N. Koul"],
        "year": 2000,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "description": "Sociolinguistic and anthropological treatise covering speech levels, honorifics, kinship terms, modes of address, and personal names.",
        "domains": ["sociolinguistics", "honorifics", "kinship", "culture"],
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.1684",
        "local_file": "books/koul_2000_language_linguistics_culture.txt"
    },
    {
        "id": "koul_wali_2006_modern_grammar",
        "title": "Modern Kashmiri Grammar",
        "authors": ["Prof. Omkar N. Koul", "Prof. Kashi Wali"],
        "year": 2006,
        "publisher": "Dunwoody Press / Lincom Europa",
        "description": "Comprehensive linguistic reference grammar covering phonology, nominal morphology, case markers, verbal system, complex sentence structure, and clitic placement.",
        "domains": ["reference_grammar", "syntax", "morphology", "phonology"],
        "category": "books",
        "level": "advanced",
        "archive_id": "218-kashmiri",
        "local_file": "books/koul_wali_2006_modern_kashmiri_grammar.txt"
    },
    {
        "id": "grierson_1898_kasmirasabdamrta",
        "title": "The Kāśmīraśabdāmṛta: A Kashmiri Grammar in Sanskrit",
        "authors": ["Pandit Iśvara Kaula", "Sir George Abraham Grierson (Editor)"],
        "year": 1898,
        "publisher": "Asiatic Society of Bengal / Baptist Mission Press, Calcutta",
        "description": "Foundational indigenous Paninian Sanskrit treatise systematically formulating Kashmiri phonological laws, matra-vowel shifts, noun declensions, and verb conjugations in sutras.",
        "domains": ["paninian_grammar", "sanskrit_sutras", "morphology", "phonology"],
        "category": "books",
        "level": "advanced",
        "archive_id": "kamiraabdamr00isvauoft",
        "local_file": "books/grierson_1898_kasmirasabdamrta.txt"
    },
    {
        "id": "grierson_1932_dictionary",
        "title": "A Dictionary of the Kashmiri Language (Complete 4-Part Edition)",
        "authors": ["Sir George Abraham Grierson", "Pandit Iśvara Kaula"],
        "year": 1932,
        "publisher": "Royal Asiatic Society of Bengal, Calcutta",
        "description": "Monumental exhaustive lexicon of the Kashmiri language containing over one million words of text with Sanskrit, Perso-Arabic, Devanagari, and Roman glosses, cross-references, and historical etymologies.",
        "domains": ["lexicography", "etymology", "sanskrit_glosses", "exhaustive_lexicon"],
        "category": "books",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.24175",
        "local_file": "books/grierson_1932_dictionary_of_kashmiri_language.txt"
    },
    {
        "id": "kalhana_rajatarangini_vol2",
        "title": "Kalhana's Rajatarangini: A Chronicle of the Kings of Kasmir (Vol. 2: Notes, Geographical Memoir, and Index)",
        "authors": ["Kalhana", "Sir M. Aurel Stein (Translator & Editor)"],
        "year": 1900,
        "publisher": "Archibald Constable and Co., Westminster",
        "description": "The second volume containing the exhaustive history of the Lohara dynasty, Stein's masterwork Memoir on the Ancient Geography of Kashmir, and full topographical index.",
        "domains": ["history", "ancient_geography", "toponymy", "lohara_dynasty"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "kalhanasrajatara02mast",
        "local_file": "discourses/stein_1900_rajatarangini_vol2.txt"
    },
    {
        "id": "razdan_1913_sivaparinayah",
        "title": "Śivapariṇayaḥ: A Poem in the Kashmiri Language",
        "authors": ["Krishna Rajanaka (Krishna Razdan)", "Mahāmahopādhyāya Mukundarāma Śāstrī", "Sir George A. Grierson"],
        "year": 1913,
        "publisher": "Asiatic Society of Bengal / Bibliotheca Indica, Calcutta",
        "description": "Masterpiece of classical Kashmiri epic poetry narrating the divine marriage of Shiva and Parvati, with Sanskrit chaya and linguistic notes.",
        "domains": ["classical_poetry", "shaivism", "epic", "sanskrit_chaya"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "sivaparinayahpoe00krsnuoft",
        "local_file": "discourses/razdan_1913_sivaparinayah.txt"
    },
    {
        "id": "dinanath_1928_shri_krishnavatara_lila",
        "title": "Śrī Kṛṣṇāvatāra Līlā of Dinanath in Kashmiri",
        "authors": ["Dinanath", "Sir George Abraham Grierson (Editor)"],
        "year": 1928,
        "publisher": "Bibliotheca Indica / Asiatic Society of Bengal, Calcutta",
        "description": "Famous 19th-century Kashmiri devotional epic depicting the life of Lord Krishna in melodious indigenous verse with scholarly linguistic commentary.",
        "domains": ["classical_poetry", "devotional", "epic", "verse"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "cCPK_shri-krishnavatara-lila-of-dinanath-in-kashmiri-george-grierson",
        "local_file": "discourses/dinanath_1928_shri_krishnavatara_lila.txt"
    },
    {
        "id": "grierson_1916_sarada_alphabet",
        "title": "On the Sarada Alphabet",
        "authors": ["Sir George Abraham Grierson"],
        "year": 1916,
        "publisher": "Journal of the Royal Asiatic Society of Great Britain and Ireland",
        "description": "Seminal paleographical study tracing the historical evolution of the Sharada alphabet from Western Brahmi and Siddhamatrika, detailing letterforms, numeral signs, and Kashmir scribal traditions.",
        "domains": ["sharada_script", "palaeography", "epigraphy", "scribal_tradition"],
        "category": "papers",
        "level": "advanced",
        "archive_id": "OnTheSaradaAlphabetGrierson",
        "local_file": "papers/grierson_1916_on_the_sarada_alphabet.txt"
    },
    {
        "id": "lawrence_1895_valley_of_kashmir",
        "title": "The Valley of Kashmir",
        "authors": ["Sir Walter Roper Lawrence"],
        "year": 1895,
        "publisher": "Henry Frowde / Oxford University Press Warehouse, London",
        "description": "Monumental encyclopedic survey of Kashmir by the State Settlement Commissioner detailing geography, geology, flora and fauna, archaeology, history, social life, tribes, agriculture, land settlement, traditional proverbs, and an extensive Kashmiri glossary.",
        "domains": ["geography", "history", "settlement", "lexicography", "flora_fauna", "sociology"],
        "category": "books",
        "level": "advanced",
        "archive_id": "valleyofkashmir00lawruoft",
        "local_file": "books/lawrence_1895_valley_of_kashmir.txt"
    },
    {
        "id": "grierson_1899_essays_grammar",
        "title": "Essays on Kashmiri Grammar",
        "authors": ["Sir George Abraham Grierson"],
        "year": 1899,
        "publisher": "Asiatic Society of Bengal / Baptist Mission Press, Calcutta",
        "description": "Authoritative comparative treatise on Kashmiri morphology, phonology, split-ergativity, pronominal clitic clusters, and systematic noun-verb paradigms based on indigenous Sanskrit grammars.",
        "domains": ["grammar", "syntax", "morphology", "phonology"],
        "category": "books",
        "level": "advanced",
        "archive_id": "kashmiriessaysonkashmirigrammargeorgegriersona._202003_670_U",
        "local_file": "books/grierson_1899_essays_on_kashmiri_grammar.txt"
    },
    {
        "id": "buhler_1877_kashmir_mss_tour",
        "title": "Detailed Report of a Tour in Search of Sanskrit MSS. in Kasmir, Rajputana, and Central India",
        "authors": ["Dr. Georg Bühler"],
        "year": 1877,
        "publisher": "Royal Asiatic Society (Bombay Branch) / Society's Press, Bombay",
        "description": "Historic landmark report documenting the philological discovery of ancient Sharada birch-bark manuscripts in Srinagar, collating the editio princeps of Kalhana's Rajatarangini, Nilamata Purana, and Kashmiri Shaivite texts.",
        "domains": ["catalogues", "sharada_manuscripts", "epigraphy", "palaeography"],
        "category": "catalogues",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.124536",
        "local_file": "catalogues/buhler_1877_kashmir_manuscripts_tour.txt"
    },
    {
        "id": "temple_1924_word_of_lalla",
        "title": "The Word of Lalla the Prophetess: Being the Sayings of Lal Ded or Lal Diddi of Kashmir",
        "authors": ["Sir Richard Carnac Temple"],
        "year": 1924,
        "publisher": "Cambridge University Press, Cambridge",
        "description": "Exhaustive verse translation and metric, linguistic, and philosophical study of the Vakhs of 14th-century mystic poetess Lal Ded, with an analytical dictionary and comparative Shaiva-Sufi theological exposition.",
        "domains": ["folklore", "poetry", "vakhs", "mysticism", "philosophy"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "TheWordOfLallaTheProphetessSirRichardCarnacTemple",
        "local_file": "discourses/temple_1924_word_of_lalla.txt"
    },
    {
        "id": "koul_1924_the_kashmiri_pandit",
        "title": "The Kashmiri Pandit: Early History, Social Customs, Language, and Folklore",
        "authors": ["Pandit Anand Koul"],
        "year": 1924,
        "publisher": "Utpal Publications, Delhi / Calcutta",
        "description": "Pioneering socio-cultural and linguistic history of the Kashmiri Saraswat community, documenting ancient clans, gotras, historical migrations, folklore idioms, wedding songs, and traditional festivals.",
        "domains": ["history", "sociology", "customs", "folklore", "idioms"],
        "category": "discourses",
        "level": "intermediate",
        "archive_id": "thekashmiripanditanandkoul",
        "local_file": "discourses/koul_1924_the_kashmiri_pandit.txt"
    },
    {
        "id": "vigne_1842_travels_kashmir",
        "title": "Travels in Kashmir, Ladak, Iskardo, the Countries Adjoining the Mountain-Course of the Indus",
        "authors": ["Godfrey Thomas Vigne"],
        "year": 1842,
        "publisher": "Henry Colburn, Great Marlborough Street, London",
        "description": "Early detailed Victorian exploration of the Kashmir Valley, documenting ancient temples (Martand, Avantipora, Shankaracharya), river networks, indigenous trades, folklore, and Dardic border dialects.",
        "domains": ["travelogue", "geography", "history", "archaeology", "dialects"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "travelsinkashmir01vign",
        "local_file": "discourses/vigne_1842_travels_in_kashmir.txt"
    },
    {
        "id": "dutt_1879_kings_kashmira_vol1",
        "title": "Kings of Kashmira (Vol. 1: Sanskrit Chronicles of Kalhana's Rajatarangini)",
        "authors": ["Jogesh Chunder Dutt"],
        "year": 1879,
        "publisher": "I. C. Bose & Co., Stanhope Press, Calcutta",
        "description": "Pioneering English prose translation of the first six cantos of Kalhana's Sanskrit epic chronicle Rajatarangini, narrating the early dynasties of Kashmir, sacred springs, and foundation of Srinagar.",
        "domains": ["chronicles", "history", "sanskrit_translation", "dynasties"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "RajataranginiOfKalhana-English-JogeshChunderDuttVolumes12",
        "local_file": "discourses/dutt_1879_kings_of_kashmira_vol1.txt"
    },
    {
        "id": "dutt_1887_kings_kashmira_vol2_jonaraja",
        "title": "Kings of Kashmira (Vol. 2: The Rajatarangini of Jonaraja)",
        "authors": ["Jogesh Chunder Dutt"],
        "year": 1887,
        "publisher": "Elm Press, Calcutta",
        "description": "Translation of Jonaraja's Sanskrit chronicle continuing the royal history of Kashmir from 1150 to 1459 CE, detailing the rise of the Shah Mir dynasty and the reign of Sultan Zain-ul-Abidin (Budshah).",
        "domains": ["chronicles", "history", "shah_mir_dynasty", "jonaraja"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "RajataranginiOfKalhana-English-JogeshChunderDuttVolumes12",
        "local_file": "discourses/dutt_1887_kings_of_kashmira_vol2_jonaraja.txt"
    },
    {
        "id": "dutt_1898_kings_kashmira_vol3_srivara",
        "title": "Kings of Kashmira (Vol. 3: The Rajatarangini of Srivara and Prajyabhatta)",
        "authors": ["Jogesh Chunder Dutt"],
        "year": 1898,
        "publisher": "Metcalfe Press, Calcutta",
        "description": "Translation of Srivara's Jaina-Rajatarangini and Prajyabhatta's Rajavalipataka covering Kashmir's late medieval history (1459–1586 CE) up to Emperor Akbar's incorporation of the Valley into the Mughal Empire.",
        "domains": ["chronicles", "history", "srivara", "medieval_kashmir"],
        "category": "discourses",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.530049",
        "local_file": "discourses/dutt_1898_kings_of_kashmira_vol3_srivara.txt"
    },
    {
        "id": "bernier_1665_travels_kashmir",
        "title": "Travels in the Mogul Empire: Journey to the Kingdom of Kachemire",
        "authors": ["François Bernier"],
        "year": 1665,
        "publisher": "Archibald Constable & Co., Westminster, London",
        "description": "Celebrated personal letters and eyewitness narrative by the French physician accompanying Emperor Aurangzeb's royal caravan across the Pir Panjal passes into the Kashmir Valley in 1665.",
        "domains": ["travelogue", "mughal_period", "eyewitness_history"],
        "category": "discourses",
        "level": "intermediate",
        "archive_id": "travelsinmogulem00bernuoft",
        "local_file": "discourses/bernier_1665_travels_in_kashmir.txt"
    }
]

def _find_library_dir() -> Optional[str]:
    """Locates the library directory relative to package or current working dir."""
    candidates = [
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "library")),
        os.path.abspath(os.path.join(os.getcwd(), "library")),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "library"))
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None

def get_research_sources() -> List[Dict[str, Any]]:
    """Return all historical research and reference sources."""
    return HISTORICAL_SOURCES

def search_research_sources(query: str) -> List[Dict[str, Any]]:
    """Search research sources by title, author, domain, category, or keyword."""
    q = query.strip().lower()
    results = []
    for s in HISTORICAL_SOURCES:
        if (
            q in s["title"].lower()
            or q in s.get("description", "").lower()
            or any(q in a.lower() for a in s.get("authors", []))
            or any(q in d.lower() for d in s.get("domains", []))
            or q in str(s.get("year", ""))
            or q in s.get("category", "").lower()
            or q in s.get("id", "").lower()
        ):
            results.append(s)
    return results

def get_sources_by_category(category: str) -> List[Dict[str, Any]]:
    """Return all sources classified under a specific category (books, catalogues, discourses, papers)."""
    c = category.strip().lower()
    cat = get_library_catalog()
    items = cat.get("items", [])
    matched = [it for it in items if it.get("category", "").lower() == c]
    if matched:
        return matched
    return [s for s in HISTORICAL_SOURCES if s.get("category", "").lower() == c]

def get_sources_by_level(level: str) -> List[Dict[str, Any]]:
    """
    Return all sources classified under a specific learning progression level
    ('elementary', 'intermediate', 'advanced').
    """
    lvl = level.strip().lower()
    cat = get_library_catalog()
    items = cat.get("items", [])
    matched = [it for it in items if it.get("level", "").lower() == lvl]
    if matched:
        return matched
    return [s for s in HISTORICAL_SOURCES if s.get("level", "").lower() == lvl]

def get_library_catalog() -> Dict[str, Any]:
    """
    Returns the comprehensive manifest of all downloaded and indexed texts
    in the Koshur library, including word counts and file sizes.
    """
    lib_dir = _find_library_dir()
    if lib_dir:
        cat_file = os.path.join(lib_dir, "library_catalog.json")
        if os.path.isfile(cat_file):
            try:
                with open(cat_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return {
        "catalog_version": "3.0.0",
        "repository": "Koshur Digital Linguistics Library",
        "items": HISTORICAL_SOURCES,
        "summary": {
            "total_volumes": len(HISTORICAL_SOURCES),
            "categories": {
                "books": len([s for s in HISTORICAL_SOURCES if s.get("category") == "books"]),
                "catalogues": len([s for s in HISTORICAL_SOURCES if s.get("category") == "catalogues"]),
                "discourses": len([s for s in HISTORICAL_SOURCES if s.get("category") == "discourses"]),
                "papers": len([s for s in HISTORICAL_SOURCES if s.get("category") == "papers"])
            }
        }
    }

def get_library_stats() -> Dict[str, Any]:
    """Returns high-level statistics about the Koshur library corpus."""
    cat = get_library_catalog()
    summary = cat.get("summary", {})
    return {
        "total_volumes": summary.get("total_volumes", len(HISTORICAL_SOURCES)),
        "total_words": summary.get("total_words", 3348910),
        "total_characters": summary.get("total_characters", 20820571),
        "category_counts": summary.get("categories", {}),
        "level_counts": summary.get("levels", {})
    }

def read_library_source(source_id: str, max_chars: Optional[int] = None) -> Optional[str]:
    """
    Reads the content of a downloaded library source by its ID.
    Optionally limits output to the first max_chars.
    """
    lib_dir = _find_library_dir()
    if not lib_dir:
        return None

    # Search in historical sources
    matched = None
    for s in HISTORICAL_SOURCES:
        if s["id"] == source_id or s.get("local_file", "").endswith(f"{source_id}.txt"):
            matched = s
            break

    if not matched or "local_file" not in matched:
        # Try finding by filename directly
        for root, _, files in os.walk(lib_dir):
            for f in files:
                if source_id in f and f.endswith(".txt"):
                    target = os.path.join(root, f)
                    with open(target, "r", encoding="utf-8", errors="ignore") as fp:
                        return fp.read(max_chars) if max_chars else fp.read()
        return None

    target = os.path.join(lib_dir, matched["local_file"])
    if os.path.isfile(target):
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(max_chars) if max_chars else f.read()

    return None

def search_library_text(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Performs full-text keyword search across all 4.32+ million words in the
    downloaded library corpus, returning source title, category, and matching text snippets.
    """
    lib_dir = _find_library_dir()
    if not lib_dir or not query or not query.strip():
        return []

    q = query.strip().lower()
    results = []

    for root, _, files in os.walk(lib_dir):
        for f in sorted(files):
            if not f.endswith(".txt"):
                continue
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                    lines = fp.readlines()
                    for idx, line in enumerate(lines):
                        if q in line.lower():
                            snippet = line.strip()
                            results.append({
                                "file": f,
                                "line_number": idx + 1,
                                "snippet": snippet[:200]
                            })
                            if len(results) >= max_results:
                                return results
            except Exception:
                continue

    return results
