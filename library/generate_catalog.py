import os
import json

BASE_DIR = r"c:\Users\Ankush Pandita\Desktop\koshur\library"

catalog = {
    "catalog_version": "3.0.0",
    "repository": "Koshur Digital Linguistics Library & Research Archive",
    "learning_levels": {
        "elementary": "Foundational primers, introductory spoken courses, basic grammar, and graded parallel readers for new learners",
        "intermediate": "Bridge grammar, learner dictionaries, proverbs, oral folk tales, lyrics, and cultural linguistic treatises",
        "advanced": "Comprehensive theoretical grammars, monumental historical dictionaries, classical Sanskrit-Kashmiri sutras, epic poems, historical chronicles, and peer-reviewed syntactic research"
    },
    "categories": {
        "books": "Grammars, dictionaries, vocabularies, and course textbooks",
        "catalogues": "Manuscript catalogues and epigraphic registers",
        "discourses": "Classical epics, puranas, historical chronicles, and folk literature",
        "papers": "Peer-reviewed academic research on Kashmiri syntax, phonology, and typography"
    },
    "items": []
}

meta_map = {
    # BOOKS
    "bhat_2007_course_in_kashmiri.txt": {
        "id": "bhat_2007_course_kashmiri",
        "title": "A Course in Kashmiri Language",
        "author": "Dr. Roop Krishen Bhat",
        "year": 2007,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.language.0066",
        "description": "Introductory pedagogical coursebook for second language learners covering basic Kashmiri phonology, greetings, case suffixes, verb stems, and conversational dialogues."
    },
    "koul_1987_spoken_kashmiri.txt": {
        "id": "koul_1987_spoken_kashmiri",
        "title": "Spoken Kashmiri: A Language Course",
        "author": "Prof. Omkar N. Koul",
        "year": 1987,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.language.0846",
        "description": "Foundational introductory textbook structured in graded lessons, drills, structural notes, everyday dialogues, and elementary vocabulary."
    },
    "wade_1888_grammar.txt": {
        "id": "wade_1888_grammar",
        "title": "A Grammar of the Kashmiri Language",
        "author": "Rev. T. R. Wade",
        "year": 1888,
        "publisher": "Society for Promoting Christian Knowledge, London",
        "category": "books",
        "level": "elementary",
        "archive_id": "grammarofkashmir0000wade",
        "description": "Early systematic English grammar of Kashmiri outlining alphabetic orthography, noun classes, pronouns, declensions, and basic verb conjugations."
    },
    "shauq_kashmiri_reader.txt": {
        "id": "shauq_kashmiri_reader",
        "title": "Kashmiri English Hindi Reader",
        "author": "Prof. Shafi Shauq",
        "year": 1990,
        "publisher": "University of Kashmir / Cultural Academy, Srinagar",
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.ernet.509601",
        "description": "Graded multilingual reader featuring short stories, cultural essays, everyday prose, and parallel sentence-level English and Hindi glosses."
    },
    "handoo_1975_common_vocab.txt": {
        "id": "handoo_1975_common_vocab",
        "title": "Hindi-Kashmiri Common Vocabulary",
        "author": "Dr. Jawahar Lal Handoo and Dr. Lalita Handoo",
        "year": 1975,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "category": "books",
        "level": "elementary",
        "archive_id": "hindi-kashmiri-common-vocabulary-jawahar-lal-and-lalita-handoo",
        "description": "Comparative linguistic analysis mapping shared Indo-Aryan cognates, phonetic shifts, and shared morphological stems across Kashmiri and Hindi."
    },
    "koul_1933_kashmiri_riddles.txt": {
        "id": "koul_1933_riddles",
        "title": "Kashmiri Riddles",
        "author": "Pandit Anand Koul",
        "year": 1933,
        "publisher": "Calcutta",
        "category": "books",
        "level": "elementary",
        "archive_id": "KashmiriRiddlesKoul",
        "description": "Traditional Kashmiri cultural riddles (praatshik) and word puzzles preserving indigenous idioms and humorous vernacular phrasing."
    },
    "koul_intermediate_course_kashmiri.txt": {
        "id": "koul_intermediate_course",
        "title": "An Intermediate Course in Kashmiri",
        "author": "Prof. Omkar N. Koul",
        "year": 1995,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "category": "books",
        "level": "intermediate",
        "archive_id": "mjnv-an-intermediate-course-in-kashmiri-omkar-m.-koul",
        "description": "Bridge textbook advancing from basic grammar to complex sentence construction, relative clauses, compound verbs, and cultural discourse."
    },
    "koul_2000_dictionary_second_language.txt": {
        "id": "koul_2000_dictionary_second_language",
        "title": "Kashmiri-English Dictionary for Second Language Learners",
        "author": "Prof. Omkar N. Koul, Dr. Roop Krishen Bhat, and Prof. S. N. Raina",
        "year": 2000,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.2243",
        "description": "Comprehensive learner-oriented dictionary with grammatical category labels, phonemic Roman transliteration, illustrative sentences, and English glosses."
    },
    "knowles_1885_proverbs.txt": {
        "id": "knowles_1885_proverbs",
        "title": "A Dictionary of Kashmiri Proverbs and Sayings",
        "author": "Rev. J. Hinton Knowles",
        "year": 1885,
        "publisher": "Education Society's Press, Bombay / Trübner & Co., London",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dictionaryofkash014372mbp",
        "description": "Monumental folk repository of Kashmiri proverbs, idioms, folklore, and cultural metaphors with literal translations and sociological folklore commentary."
    },
    "knowles_1888_folktales.txt": {
        "id": "knowles_1888_folktales",
        "title": "Folk-Tales of Kashmir",
        "author": "Rev. J. Hinton Knowles",
        "year": 1888,
        "publisher": "Trübner & Co., London",
        "category": "books",
        "level": "intermediate",
        "archive_id": "folktalesofkashm00knowuoft",
        "description": "Extensive collection of 64 traditional Kashmiri legends, fairy tales, and oral folklore recorded directly from village storytellers."
    },
    "handoo_1994_structural_analysis_folk_tales.txt": {
        "id": "handoo_1994_folk_analysis",
        "title": "Structural Analysis of Kashmiri Folk Tales",
        "author": "Dr. Lalita Handoo",
        "year": 1994,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.1960",
        "description": "Deep morphological and structural analysis applying Proppian narratology and folkloric motifs to Kashmiri oral tales and fairy lore."
    },
    "kaul_1945_kashmiri_lyrics.txt": {
        "id": "kaul_1945_lyrics",
        "title": "Kashmiri Lyrics: Selected and Translated",
        "author": "Pandit J. L. Kaul",
        "year": 1945,
        "publisher": "Rinemisray, Srinagar",
        "category": "books",
        "level": "intermediate",
        "archive_id": "in.ernet.dli.2015.102721",
        "description": "Anthology of classic Kashmiri lyrical poetry including Habba Khatoon, Rasul Mir, Arnimal, and Mahmud Gami with English translations."
    },
    "koul_2000_language_linguistics_culture.txt": {
        "id": "koul_2000_linguistics_culture",
        "title": "Kashmiri Language, Linguistics and Culture",
        "author": "Prof. Omkar N. Koul",
        "year": 2000,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.1684",
        "description": "Sociolinguistic and anthropological treatise covering speech levels, honorifics, kinship terms, modes of address, and personal names."
    },
    "raina_history_kashmiri_literature.txt": {
        "id": "raina_history_literature",
        "title": "A History of Kashmiri Literature",
        "author": "Prof. Triloki Nath Raina",
        "year": 2002,
        "publisher": "Sahitya Akademi, New Delhi",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.2319",
        "description": "Comprehensive historical chronicle of Kashmiri poetry, prose, mystical vakhs, masnavis, and modern literary revivals from the 14th century to present."
    },
    "koul_studies_linguistics.txt": {
        "id": "koul_studies_linguistics",
        "title": "Studies in Kashmiri Linguistics",
        "author": "Prof. Omkar N. Koul",
        "year": 2005,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "category": "books",
        "level": "advanced",
        "archive_id": "studies-in-kashmiri-linguistics-omkar-n-koul",
        "description": "Scholarly papers on Kashmiri phonetics, morphology, syntax, sociolinguistics, and language pedagogy."
    },
    "koul_wali_2006_modern_kashmiri_grammar.txt": {
        "id": "koul_wali_2006_modern_grammar",
        "title": "Modern Kashmiri Grammar",
        "author": "Prof. Omkar N. Koul and Prof. Kashi Wali",
        "year": 2006,
        "publisher": "Dunwoody Press / Lincom Europa",
        "category": "books",
        "level": "advanced",
        "archive_id": "218-kashmiri",
        "description": "Comprehensive linguistic reference grammar covering phonology, nominal morphology, case markers, verbal system, complex sentence structure, and clitic placement."
    },
    "grierson_1898_kasmirasabdamrta.txt": {
        "id": "grierson_1898_kasmirasabdamrta",
        "title": "The Kāśmīraśabdāmṛta: A Kashmiri Grammar in Sanskrit",
        "author": "Pandit Iśvara Kaula (Edited by George A. Grierson)",
        "year": 1898,
        "publisher": "Asiatic Society of Bengal / Baptist Mission Press, Calcutta",
        "category": "books",
        "level": "advanced",
        "archive_id": "kamiraabdamr00isvauoft",
        "description": "Foundational indigenous Paninian Sanskrit treatise systematically formulating Kashmiri phonological laws, matra-vowel shifts, noun declensions, and verb conjugations in sutras."
    },
    "grierson_1919_lsi_vol8_part2_dardic.txt": {
        "id": "grierson_1919_lsi_dardic",
        "title": "Linguistic Survey of India (Vol. VIII, Part II: Specimens of the Dardic or Pisacha Languages)",
        "author": "Sir George Abraham Grierson",
        "year": 1919,
        "publisher": "Superintendent Government Printing, Calcutta",
        "category": "books",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.32109",
        "description": "Foundational linguistic survey covering Kashmiri grammar, standard dialects (Kishtwari, Poguli, Siraji, Rambani), and comparative Dardic specimens."
    },
    "elmslie_1872_vocabulary.txt": {
        "id": "elmslie_1872_vocab",
        "title": "A Vocabulary of the Kashmiri Language (English-Kashmiri and Kashmiri-English)",
        "author": "Dr. William Jackson Elmslie",
        "year": 1872,
        "publisher": "Church Missionary Society / Harrison & Sons, London",
        "category": "books",
        "level": "advanced",
        "archive_id": "avocavularykash00elmsgoog",
        "description": "Pioneering medical and conversational vocabulary compiled in Srinagar documenting anatomical, botanical, domestic, and clinical terms."
    },
    "grierson_1932_dictionary_of_kashmiri_language.txt": {
        "id": "grierson_1932_dictionary",
        "title": "A Dictionary of the Kashmiri Language",
        "author": "Sir George Abraham Grierson and Pandit Iśvara Kaula",
        "year": 1932,
        "publisher": "Royal Asiatic Society of Bengal, Calcutta",
        "category": "books",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.24175",
        "description": "Monumental exhaustive lexicon of the Kashmiri language in four parts, containing over one million words of text with Sanskrit, Perso-Arabic, Devanagari, and Roman glosses, cross-references, and historical etymologies."
    },
    "ciil_1988_trilingual_dictionary.txt": {
        "id": "ciil_1988_trilingual_dictionary",
        "title": "Hindi-Kashmiri-English Trilingual Dictionary (Jild 3)",
        "author": "Central Institute of Indian Languages (CIIL)",
        "year": 1988,
        "publisher": "Central Institute of Indian Languages (CIIL), Mysore",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.language.1564",
        "description": "Comprehensive trilingual lexicographical reference linking Hindi headwords with Kashmiri (Devanagari & Perso-Arabic) equivalents and English definitions."
    },
    "kaul_gile_tori_short_stories.txt": {
        "id": "kaul_gile_tori_short_stories",
        "title": "Gile Tori: Kashmiri Short Stories",
        "author": "Prof. Omkar Kaul",
        "year": 1992,
        "publisher": "Kashmiri Cultural Forum, Srinagar",
        "category": "books",
        "level": "intermediate",
        "archive_id": "qYiv_gile-tori-kashmiri-short-stories-omkar-kaul",
        "description": "Collection of contemporary Kashmiri short stories showcasing natural vernacular prose, dialogue, and Kashmiri idioms."
    },
    "koul_schmidt_sociolinguistic_survey.txt": {
        "id": "koul_schmidt_sociolinguistic_survey",
        "title": "Kashmiri: A Sociolinguistic Survey",
        "author": "Prof. Omkar N. Koul and Ruth Laila Schmidt",
        "year": 1983,
        "publisher": "Indian Institute of Language Studies, Patiala",
        "category": "books",
        "level": "advanced",
        "archive_id": "KFnj_kashmiri-a-sociolinguistic-survey-omkar-n-koul-and-ruth-laila-schmidt",
        "description": "Empirical sociolinguistic survey investigating language usage, bilingualism, dialect variation, and language maintenance in Kashmir."
    },
    "koul_kashmiri_english_dictionary.txt": {
        "id": "koul_kashmiri_english_dictionary",
        "title": "Kashmiri-English Dictionary",
        "author": "Prof. Omkar N. Koul",
        "year": 2005,
        "publisher": "Indian Institute of Language Studies, Delhi",
        "category": "books",
        "level": "intermediate",
        "archive_id": "sqkr-kashmiri-english-dictionary-omkar-n-koul",
        "description": "Modern Kashmiri-English dictionary indexing thousands of contemporary, literary, and spoken Kashmiri words with phonetic and grammatical tags."
    },
    "munwar_shauq_1973_kashur_grammar.txt": {
        "id": "munwar_shauq_1973_kashur_grammar",
        "title": "Kashur Grammar",
        "author": "Naji Munwar and Prof. Shafi Shauq",
        "year": 1973,
        "publisher": "Bazm-e-Adab / Cultural Academy, Srinagar",
        "category": "books",
        "level": "elementary",
        "archive_id": "dli.ernet.504533",
        "description": "Foundational introductory grammar of Kashmiri formulating nominal declensions, pronouns, adverbs, and basic verbal conjugations in clear pedagogical format."
    },
    "shauq_kaishrik_grammar.txt": {
        "id": "shauq_kaishrik_grammar",
        "title": "Kạ̄shrik Grammar",
        "author": "Prof. Shafi Shauq",
        "year": 1985,
        "publisher": "Ali Mohammad & Sons, Srinagar",
        "category": "books",
        "level": "intermediate",
        "archive_id": "dli.ernet.510105",
        "description": "Structural and phonological Kashmiri grammar examining vocalic harmony, consonant palatalization, ergative alignment, and syntactic subordination."
    },
    "toshakhani_1967_kashir_dictionary_vol1.txt": {
        "id": "toshakhani_1967_kashir_dictionary_vol1",
        "title": "Kashir Dictionary (Vol. 1: Alif to Tsa)",
        "author": "S.K. Toshakhani, J.L. Koul, Mohi-ud-Din Hajni, P.N. Pushp, and Mohi-ud-Din Akhtar",
        "year": 1967,
        "publisher": "Jammu and Kashmir Academy of Art, Culture and Languages, Srinagar",
        "category": "books",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.510168",
        "description": "The monumental lexicographical authority for Kashmiri language, providing comprehensive definitions, script glosses, idioms, and literary attestations for letters Alif to Tsa."
    },
    "toshakhani_1969_kashir_dictionary_vol2.txt": {
        "id": "toshakhani_1969_kashir_dictionary_vol2",
        "title": "Kashir Dictionary (Vol. 2: Tsa to Dal)",
        "author": "S.K. Toshakhani, J.L. Koul, Mohi-ud-Din Hajni, P.N. Pushp, and Mohi-ud-Din Akhtar",
        "year": 1969,
        "publisher": "Jammu and Kashmir Academy of Art, Culture and Languages, Srinagar",
        "category": "books",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.510170",
        "description": "Volume 2 of the definitive Academy dictionary, containing thousands of words covering letters Tsa, Jim, Che, He, Khe, and Dal with etymological citations."
    },
    "toshakhani_1972_kashir_dictionary_vol3.txt": {
        "id": "toshakhani_1972_kashir_dictionary_vol3",
        "title": "Kashir Dictionary (Vol. 3: Dal to Re)",
        "author": "S.K. Toshakhani, J.L. Koul, Mohi-ud-Din Hajni, P.N. Pushp, and Mohi-ud-Din Akhtar",
        "year": 1972,
        "publisher": "Jammu and Kashmir Academy of Art, Culture and Languages, Srinagar",
        "category": "books",
        "level": "advanced",
        "archive_id": "KashmiriDictionaryPartIIIJKCulturalAcademy",
        "description": "Volume 3 of the encyclopedic Academy dictionary, defining words from Dal, Ddal, Zal, and Re with detailed folk phraseology and literary examples."
    },
    "toshakhani_1979_kashir_dictionary_vol7.txt": {
        "id": "toshakhani_1979_kashir_dictionary_vol7",
        "title": "Kashir Dictionary (Vol. 7: Vaw to Ye)",
        "author": "S.K. Toshakhani, J.L. Koul, Mohi-ud-Din Hajni, P.N. Pushp, and Mohi-ud-Din Akhtar",
        "year": 1979,
        "publisher": "Jammu and Kashmir Academy of Art, Culture and Languages, Srinagar",
        "category": "books",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.510171",
        "description": "Volume 7 concluding the monumental Academy dictionary series, covering terminal letters Vaw, He, and Ye with rich botanical, dialectal, and folkloric terms."
    },

    # CATALOGUES
    "stein_1894_raghunatha_manuscripts.txt": {
        "id": "stein_1894_raghunatha_catalogue",
        "title": "Catalogue of the Sanskrit Manuscripts in the Raghunatha Temple Library of the Maharaja of Jammu and Kashmir",
        "author": "Sir Marc Aurel Stein",
        "year": 1894,
        "publisher": "Nirnaya-Sagara Press, Bombay / Luzac & Co., London",
        "category": "catalogues",
        "level": "advanced",
        "archive_id": "catalogueofsansk00steigoog",
        "description": "Master epigraphic and palaeographical register cataloging over 4,500 birch-bark and paper manuscripts in Sharada, Devanagari, and Kashmiri."
    },

    # DISCOURSES
    "hatims_tales_1923.txt": {
        "id": "hatims_tales_1923",
        "title": "Hatim's Tales: Kashmiri Stories and Songs",
        "author": "Hatim Tilawöñ, Sir Aurel Stein, and Sir George A. Grierson",
        "year": 1923,
        "publisher": "John Murray, London",
        "category": "discourses",
        "level": "intermediate",
        "archive_id": "taleskashmiristo00hatiuoft",
        "description": "Phonetically recorded oral narratives and songs dictated by legendary storyteller Hatim Tilawöñ of Panderethan, with interlinear text, vocabulary, and English translation."
    },
    "lalla_vakyani_1920.txt": {
        "id": "lalla_vakyani_1920",
        "title": "Lalla-Vakyani or The Wise Sayings of Lal Ded",
        "author": "Sir George Abraham Grierson and Dr. Lionel D. Barnett",
        "year": 1920,
        "publisher": "Royal Asiatic Society, London",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.48971",
        "description": "The ancient mystical vakhs of 14th-century mystic poetess Lalleshwari (Lal Ded) with word-by-word Sanskrit chaya, English translation, and philosophical commentary."
    },
    "kashmiri_ramayana_1930.txt": {
        "id": "kashmiri_ramayana_1930",
        "title": "The Kashmiri Ramayana (Ramavataracarita)",
        "author": "Divakara Prakasa Bhatta (Edited by Sir George A. Grierson)",
        "year": 1930,
        "publisher": "Asiatic Society of Bengal / Bibliotheca Indica, Calcutta",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.48970",
        "description": "The classical Kashmiri Ramayana comprising the Ramavataracarita and Lavakusacarita in original Kashmiri verse with introduction, grammatical notes, and vocabulary."
    },
    "nilamata_purana_vol1.txt": {
        "id": "nilamata_purana_vol1",
        "title": "The Nilamata Purana (Vol. 1: Cultural and Literary Study)",
        "author": "Dr. Ved Kumari Ghai",
        "year": 1968,
        "publisher": "J&K Academy of Art, Culture and Languages, Srinagar",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "dli.language.2393",
        "description": "Foundational puranic chronicle of the Kashmir Valley detailing origin myths (Satisaras, Kashyapa, Naga rites), sacred geography, and ancient toponyms."
    },
    "kalhana_rajatarangini_stein_vol1.txt": {
        "id": "kalhana_rajatarangini_vol1",
        "title": "Kalhana's Rajatarangini: A Chronicle of the Kings of Kasmir (Vol. 1: Introduction and Books I-VII)",
        "author": "Kalhana (Translated with commentary by Sir M. A. Stein)",
        "year": 1900,
        "publisher": "Archibald Constable and Co., Westminster",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "kalhanasrajatara01sira",
        "description": "The monumental 12th-century Sanskrit-Kashmiri verse chronicle of the rulers of Kashmir, critical introduction, and extensive historical apparatus."
    },
    "stein_1900_rajatarangini_vol2.txt": {
        "id": "kalhana_rajatarangini_vol2",
        "title": "Kalhana's Rajatarangini: A Chronicle of the Kings of Kasmir (Vol. 2: Book VIII, Notes, Geographical Memoir, and Index)",
        "author": "Kalhana (Translated with commentary by Sir M. A. Stein)",
        "year": 1900,
        "publisher": "Archibald Constable and Co., Westminster",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "kalhanasrajatara02mast",
        "description": "The second volume containing the exhaustive history of the Lohara dynasty, Stein's masterwork Memoir on the Ancient Geography of Kashmir, and full topographical index."
    },
    "razdan_1913_sivaparinayah.txt": {
        "id": "razdan_1913_sivaparinayah",
        "title": "Śivapariṇayaḥ: A Poem in the Kashmiri Language",
        "author": "Krishna Rajanaka (Krishna Razdan), with gloss by Mukundarama Shastri, ed. George A. Grierson",
        "year": 1913,
        "publisher": "Asiatic Society of Bengal / Bibliotheca Indica, Calcutta",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "sivaparinayahpoe00krsnuoft",
        "description": "Masterpiece of classical Kashmiri epic poetry narrating the marriage of Shiva and Parvati, with Sanskrit chaya and linguistic notes."
    },
    "dinanath_1928_shri_krishnavatara_lila.txt": {
        "id": "dinanath_1928_shri_krishnavatara_lila",
        "title": "Śrī Kṛṣṇāvatāra Līlā of Dinanath in Kashmiri",
        "author": "Dinanath (Edited with translation and notes by Sir George A. Grierson)",
        "year": 1928,
        "publisher": "Bibliotheca Indica / Asiatic Society of Bengal, Calcutta",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "cCPK_shri-krishnavatara-lila-of-dinanath-in-kashmiri-george-grierson",
        "description": "Famous 19th-century Kashmiri devotional epic depicting the life of Lord Krishna in melodious indigenous verse with scholarly linguistic commentary."
    },
    "sufi_1948_kashir_history_vol1.txt": {
        "id": "sufi_1948_kashir_history_vol1",
        "title": "Kāshīr: Being a History of Kashmir (Vol. 1)",
        "author": "Dr. G. M. D. Sufi",
        "year": 1948,
        "publisher": "University of the Panjab / Civil and Military Gazette Press, Lahore",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.280747",
        "description": "Exhaustive cultural and political history of Kashmir spanning ancient dynasties, geography, people, religious traditions, and socio-economic life."
    },
    "sufi_1949_kashir_history_vol2.txt": {
        "id": "sufi_1949_kashir_history_vol2",
        "title": "Kāshīr: Being a History of Kashmir (Vol. 2: Literature, Arts, and Culture)",
        "author": "Dr. G. M. D. Sufi",
        "year": 1949,
        "publisher": "University of the Panjab / Civil and Military Gazette Press, Lahore",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.280746",
        "description": "Encyclopedic treatise documenting Kashmiri literature, mystic poets (Lal Ded, Nund Rishi, Habba Khatun, Arnimal), arts, crafts, and language history."
    },

    # PAPERS
    "bailey_1937_kashmiri_pronunciation.txt": {
        "id": "bailey_1937_pronunciation",
        "title": "The Pronunciation of Kashmiri: Kashmiri Sounds through the Management of the Tongue",
        "author": "T. Grahame Bailey",
        "year": 1937,
        "publisher": "Royal Asiatic Society, London",
        "category": "papers",
        "level": "elementary",
        "archive_id": "in.ernet.dli.2015.57293",
        "description": "Pioneering phonetic investigation of Kashmiri central vowels (ɨ, ɨː, ə, əː), tone, and vocalic mechanics."
    },
    "hook_koul_1996_v2_syntax.txt": {
        "id": "hook_koul_1996_v2",
        "title": "Kashmiri as a V-2 Language: Verb Second Order in Indo-Aryan",
        "author": "Peter Edwin Hook and Omkar N. Koul",
        "year": 1996,
        "publisher": "Cognitive and Typological Studies in Indo-Aryan",
        "category": "papers",
        "level": "advanced",
        "archive_id": "hook-koul-1996-v2-syntax",
        "description": "Linguistic demonstration that Kashmiri deviates from standard Indo-Aryan SOV order by exhibiting strict Verb-Second (V2) word order in root clauses."
    },
    "hook_koul_1984_split_ergativity.txt": {
        "id": "hook_koul_1984_ergativity",
        "title": "Pronominal Suffixes and Split Ergativity in Kashmiri",
        "author": "Peter Edwin Hook and Omkar N. Koul",
        "year": 1984,
        "publisher": "Kurukshetra University Linguistic Colloquium",
        "category": "papers",
        "level": "advanced",
        "archive_id": "hook-koul-1984-ergativity",
        "description": "Analysis of tripartite tense-aspect based split ergativity, case alignment, and verbal agreement in Kashmiri."
    },
    "wali_koul_1994_clitics_agreement.txt": {
        "id": "wali_koul_1994_clitics",
        "title": "Kashmiri Clitics: The Role of Agreement and Case",
        "author": "Kashi Wali and Omkar N. Koul",
        "year": 1994,
        "publisher": "Linguistics / Cambridge University Press",
        "category": "papers",
        "level": "advanced",
        "archive_id": "wali-koul-1994-clitics",
        "description": "Investigation of postverbal pronominal clitic clusters in Kashmiri, case absorption, and person hierarchy constraints."
    },
    "bhatt_1999_verb_movement.txt": {
        "id": "bhatt_1999_verb_movement",
        "title": "Verb Movement and the Syntax of Kashmiri",
        "author": "Rakesh Mohan Bhatt",
        "year": 1999,
        "publisher": "Kluwer Academic Publishers, Dordrecht",
        "category": "papers",
        "level": "advanced",
        "archive_id": "bhatt-1999-verb-movement",
        "description": "Generative syntactic account of I-to-C verb raising, specifier licensing, and word order variations in matrix vs. embedded clauses."
    },
    "pandey_2012_sharada_unicode.txt": {
        "id": "pandey_2012_sharada_unicode",
        "title": "Proposal to Encode the Sharada Script in ISO/IEC 10646 (Unicode Standard)",
        "author": "Anshuman Pandey",
        "year": 2012,
        "publisher": "Unicode Technical Committee (Document L2/12-124)",
        "category": "papers",
        "level": "advanced",
        "archive_id": "pandey-2012-sharada-unicode",
        "description": "Authoritative character architecture, conjunct ligatures, and script encoding specification allocating U+11180..U+111DF for Sharada."
    },
    "morgenstierne_1941_dardic_kashmiri.txt": {
        "id": "morgenstierne_1941_dardic",
        "title": "Notes on Kashmiri Linguistics and its Dardic Affinities",
        "author": "Georg Morgenstierne",
        "year": 1941,
        "publisher": "Norsk Tidsskrift for Sprogvidenskap, Oslo",
        "category": "papers",
        "level": "advanced",
        "archive_id": "morgenstierne-1941-dardic",
        "description": "Comparative linguistic analysis of Kashmiri within the Dardic branch of Indo-Iranian, tracing retroflexes and archaisms."
    },
    "hook_koul_2022_dedicated_sarcasm.txt": {
        "id": "hook_koul_2022_sarcasm",
        "title": "Grammaticalized Sarcasm in Kashmiri: The Morpheme -a:n and Enclitic Echoes",
        "author": "Peter Edwin Hook and Omkar N. Koul",
        "year": 2022,
        "publisher": "Journal of South Asian Linguistics",
        "category": "papers",
        "level": "advanced",
        "archive_id": "hook-koul-2022-sarcasm",
        "description": "Sociolinguistic discovery of grammaticalized morphemes and tone intonation used specifically to encode ironic and sarcastic intent."
    },
    "grierson_1916_on_the_sarada_alphabet.txt": {
        "id": "grierson_1916_sarada_alphabet",
        "title": "On the Sarada Alphabet",
        "author": "Sir George Abraham Grierson",
        "year": 1916,
        "publisher": "Journal of the Royal Asiatic Society of Great Britain and Ireland",
        "category": "papers",
        "level": "advanced",
        "archive_id": "OnTheSaradaAlphabetGrierson",
        "description": "Seminal paleographical study tracing the historical evolution of the Sharada alphabet from Western Brahmi and Siddhamatrika, detailing letterforms, numeral signs, and Kashmir scribal traditions."
    },

    # NEW HISTORICAL VOLUMES & ARCHIVES
    "lawrence_1895_valley_of_kashmir.txt": {
        "id": "lawrence_1895_valley_of_kashmir",
        "title": "The Valley of Kashmir",
        "author": "Sir Walter Roper Lawrence",
        "year": 1895,
        "publisher": "Henry Frowde / Oxford University Press Warehouse, London",
        "category": "books",
        "level": "advanced",
        "archive_id": "valleyofkashmir00lawruoft",
        "description": "Monumental encyclopedic survey of Kashmir by the State Settlement Commissioner detailing geography, geology, flora and fauna, archaeology, history, social life, tribes, agriculture, land settlement, traditional proverbs, and an extensive Kashmiri glossary."
    },
    "grierson_1899_essays_on_kashmiri_grammar.txt": {
        "id": "grierson_1899_essays_grammar",
        "title": "Essays on Kashmiri Grammar",
        "author": "Sir George Abraham Grierson",
        "year": 1899,
        "publisher": "Asiatic Society of Bengal / Baptist Mission Press, Calcutta",
        "category": "books",
        "level": "advanced",
        "archive_id": "kashmiriessaysonkashmirigrammargeorgegriersona._202003_670_U",
        "description": "Authoritative comparative treatise on Kashmiri morphology, phonology, split-ergativity, pronominal clitic clusters, and systematic noun-verb paradigms based on indigenous Sanskrit grammars."
    },
    "buhler_1877_kashmir_manuscripts_tour.txt": {
        "id": "buhler_1877_kashmir_mss_tour",
        "title": "Detailed Report of a Tour in Search of Sanskrit MSS. in Kasmir, Rajputana, and Central India",
        "author": "Dr. Georg Bühler",
        "year": 1877,
        "publisher": "Royal Asiatic Society (Bombay Branch) / Society's Press, Bombay",
        "category": "catalogues",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.124536",
        "description": "Historic landmark report documenting the philological discovery of ancient Sharada birch-bark manuscripts in Srinagar, collating the editio princeps of Kalhana's Rajatarangini, Nilamata Purana, and Kashmiri Shaivite texts."
    },
    "temple_1924_word_of_lalla.txt": {
        "id": "temple_1924_word_of_lalla",
        "title": "The Word of Lalla the Prophetess: Being the Sayings of Lal Ded or Lal Diddi of Kashmir",
        "author": "Sir Richard Carnac Temple",
        "year": 1924,
        "publisher": "Cambridge University Press, Cambridge",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "TheWordOfLallaTheProphetessSirRichardCarnacTemple",
        "description": "Exhaustive verse translation and metric, linguistic, and philosophical study of the Vakhs of 14th-century mystic poetess Lal Ded, with an analytical dictionary and comparative Shaiva-Sufi theological exposition."
    },
    "koul_1924_the_kashmiri_pandit.txt": {
        "id": "koul_1924_the_kashmiri_pandit",
        "title": "The Kashmiri Pandit: Early History, Social Customs, Language, and Folklore",
        "author": "Pandit Anand Koul",
        "year": 1924,
        "publisher": "Utpal Publications, Delhi / Calcutta",
        "category": "discourses",
        "level": "intermediate",
        "archive_id": "thekashmiripanditanandkoul",
        "description": "Pioneering socio-cultural and linguistic history of the Kashmiri Saraswat community, documenting ancient clans, gotras, historical migrations, folklore idioms, wedding songs, and traditional festivals."
    },
    "vigne_1842_travels_in_kashmir.txt": {
        "id": "vigne_1842_travels_kashmir",
        "title": "Travels in Kashmir, Ladak, Iskardo, the Countries Adjoining the Mountain-Course of the Indus",
        "author": "Godfrey Thomas Vigne",
        "year": 1842,
        "publisher": "Henry Colburn, Great Marlborough Street, London",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "travelsinkashmir01vign",
        "description": "Early detailed Victorian exploration of the Kashmir Valley, documenting ancient temples (Martand, Avantipora, Shankaracharya), river networks, indigenous trades, folklore, and Dardic border dialects."
    },
    "dutt_1879_kings_of_kashmira_vol1.txt": {
        "id": "dutt_1879_kings_kashmira_vol1",
        "title": "Kings of Kashmira (Vol. 1: Sanskrit Chronicles of Kalhana's Rajatarangini)",
        "author": "Jogesh Chunder Dutt",
        "year": 1879,
        "publisher": "I. C. Bose & Co., Stanhope Press, Calcutta",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "RajataranginiOfKalhana-English-JogeshChunderDuttVolumes12",
        "description": "Pioneering English prose translation of the first six cantos of Kalhana's Sanskrit epic chronicle Rajatarangini, narrating the early dynasties of Kashmir, sacred springs, and foundation of Srinagar."
    },
    "dutt_1887_kings_of_kashmira_vol2_jonaraja.txt": {
        "id": "dutt_1887_kings_kashmira_vol2_jonaraja",
        "title": "Kings of Kashmira (Vol. 2: The Rajatarangini of Jonaraja)",
        "author": "Jogesh Chunder Dutt",
        "year": 1887,
        "publisher": "Elm Press, Calcutta",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "RajataranginiOfKalhana-English-JogeshChunderDuttVolumes12",
        "description": "Translation of Jonaraja's Sanskrit chronicle continuing the royal history of Kashmir from 1150 to 1459 CE, detailing the rise of the Shah Mir dynasty and the reign of Sultan Zain-ul-Abidin (Budshah)."
    },
    "dutt_1898_kings_of_kashmira_vol3_srivara.txt": {
        "id": "dutt_1898_kings_kashmira_vol3_srivara",
        "title": "Kings of Kashmira (Vol. 3: The Rajatarangini of Srivara and Prajyabhatta)",
        "author": "Jogesh Chunder Dutt",
        "year": 1898,
        "publisher": "Metcalfe Press, Calcutta",
        "category": "discourses",
        "level": "advanced",
        "archive_id": "in.ernet.dli.2015.530049",
        "description": "Translation of Srivara's Jaina-Rajatarangini and Prajyabhatta's Rajavalipataka covering Kashmir's late medieval history (1459–1586 CE) up to Emperor Akbar's incorporation of the Valley into the Mughal Empire."
    },
    "bernier_1665_travels_in_kashmir.txt": {
        "id": "bernier_1665_travels_kashmir",
        "title": "Travels in the Mogul Empire: Journey to the Kingdom of Kachemire",
        "author": "François Bernier",
        "year": 1665,
        "publisher": "Archibald Constable & Co., Westminster, London",
        "category": "discourses",
        "level": "intermediate",
        "archive_id": "travelsinmogulem00bernuoft",
        "description": "Celebrated personal letters and eyewitness narrative by the French physician accompanying Emperor Aurangzeb's royal caravan across the Pir Panjal passes into the Kashmir Valley in 1665."
    }
}

total_words = 0
total_chars = 0

for cat_dir in ["books", "catalogues", "discourses", "papers"]:
    dpath = os.path.join(BASE_DIR, cat_dir)
    if not os.path.exists(dpath):
        continue
    for f in sorted(os.listdir(dpath)):
        if f.endswith(".txt"):
            p = os.path.join(dpath, f)
            rel_path = f"{cat_dir}/{f}"
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
                w_count = len(txt.split())
                c_count = len(txt)
                total_words += w_count
                total_chars += c_count

            entry = dict(meta_map.get(f, {
                "id": f.replace(".txt", ""),
                "title": f.replace("_", " ").replace(".txt", "").title(),
                "author": "Unknown",
                "year": None,
                "publisher": "Public Domain Archive",
                "category": cat_dir,
                "level": "intermediate",
                "archive_id": None,
                "description": "Historical textual corpus in the Koshur library."
            }))
            entry["file"] = rel_path
            entry["word_count"] = w_count
            entry["char_count"] = c_count
            entry["file_size_bytes"] = os.path.getsize(p)
            catalog["items"].append(entry)

catalog["summary"] = {
    "total_volumes": len(catalog["items"]),
    "total_words": total_words,
    "total_characters": total_chars,
    "categories": {
        "books": len([i for i in catalog["items"] if i["category"] == "books"]),
        "catalogues": len([i for i in catalog["items"] if i["category"] == "catalogues"]),
        "discourses": len([i for i in catalog["items"] if i["category"] == "discourses"]),
        "papers": len([i for i in catalog["items"] if i["category"] == "papers"])
    },
    "levels": {
        "elementary": len([i for i in catalog["items"] if i.get("level") == "elementary"]),
        "intermediate": len([i for i in catalog["items"] if i.get("level") == "intermediate"]),
        "advanced": len([i for i in catalog["items"] if i.get("level") == "advanced"])
    }
}

catalog_path = os.path.join(BASE_DIR, "library_catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Catalog generated successfully at {catalog_path}")
print(f"Total volumes: {len(catalog['items'])}")
print(f"Total library words: {total_words:,d}")
print(f"Total library characters: {total_chars:,d}")
print(f"Category breakdown: {catalog['summary']['categories']}")
print(f"Level breakdown: {catalog['summary']['levels']}")
