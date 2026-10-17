"""
Lexical Extraction & Enrichment Pipeline:
Extracts, structures, and incorporates authentic Kashmiri cultural, historical,
philosophical, agricultural, and geographical terms from the 10 newly downloaded
library volumes into the core Koshur lexicon.
"""

import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import koshur
from koshur.lexicon.words_data import WORDS_DATA

NEW_LEXICAL_CANDIDATES = [
    # -------------------------------------------------------------
    # 1. From Sir Walter Lawrence: The Valley of Kashmir (1895)
    #    (Agriculture, Dal Lake, Implements, Crafts, Rural Life)
    # -------------------------------------------------------------
    {
        "lemma": "Radh",
        "roman": "Rādh",
        "devanagari": "राध",
        "persoarabic": "رادھ",
        "sharada": "𑆫𑆳𑆣",
        "pos": "noun",
        "meaning_en": "Floating vegetable garden of Dal Lake fashioned from woven reeds and aquatic silt",
        "meaning_hi": "राद (डल झील का तैरता हुआ बगीचा)",
        "etymology": "Indigenous Kashmiri lake cultivation term documented by Lawrence",
        "tags": ["agriculture", "dal_lake", "nature"],
        "aliases": ["radh", "floating garden", "dal lake garden"]
    },
    {
        "lemma": "Damb",
        "roman": "Damb",
        "devanagari": "डम्ब",
        "persoarabic": "ڈَمب",
        "sharada": "𑆝𑆩𑇀𑆧",
        "pos": "noun",
        "meaning_en": "Reclaimed marshland plot or lakebank garden used for intensive vegetable cultivation",
        "meaning_hi": "डम्ब (दलदल से निकाली गई उपजाऊ भूमि / सब्जी की क्यारी)",
        "etymology": "Indigenous agricultural term (Lawrence, Valley of Kashmir)",
        "tags": ["agriculture", "land", "geography"],
        "aliases": ["damb", "marshland plot", "vegetable garden"]
    },
    {
        "lemma": "Dembi",
        "roman": "Dembī",
        "devanagari": "डेम्बी",
        "persoarabic": "ڈیمبی",
        "sharada": "𑆝𑆼𑆩𑇀𑆧𑆵",
        "pos": "noun",
        "meaning_en": "Traditional Kashmiri vegetable cultivator farming the floating gardens of Dal and Anchar lakes",
        "meaning_hi": "डेम्बी (झील के तैरते बगीचों का काश्तकार / किसान)",
        "etymology": "Derivative of Damb",
        "tags": ["occupation", "agriculture", "dal_lake"],
        "aliases": ["dembi", "vegetable farmer", "lake farmer"]
    },
    {
        "lemma": "Wudar",
        "roman": "Wudar",
        "devanagari": "वुदर",
        "persoarabic": "وُدَر",
        "sharada": "𑆮𑆶𑆢𑆫",
        "pos": "noun",
        "meaning_en": "Karewa; flat-topped alluvial lacustrine plateau unique to the Kashmir Valley where saffron and almonds grow",
        "meaning_hi": "वुदर (करेवा / पठारीय भूभाग जहाँ केसर व बादाम उगते हैं)",
        "etymology": "Kashmiri native term for Karewa formation",
        "tags": ["geography", "land", "agriculture"],
        "aliases": ["wudar", "karewa", "plateau"]
    },
    {
        "lemma": "Nambal",
        "roman": "Nambal",
        "devanagari": "नम्बल",
        "persoarabic": "نَمبَل",
        "sharada": "𑆤𑆩𑇀𑆧𑆬",
        "pos": "noun",
        "meaning_en": "Swamp, marsh, or low-lying waterlogged pasture rich in water birds",
        "meaning_hi": "नम्बल (दलदली चरागाह / आर्द्रभूमि)",
        "etymology": "Indigenous toponymic and landscape term",
        "tags": ["geography", "water", "wetland"],
        "aliases": ["nambal", "swamp", "marsh", "wetland"]
    },
    {
        "lemma": "Dan_Hearth",
        "roman": "Dān",
        "devanagari": "दान",
        "persoarabic": "دان",
        "sharada": "𑆢𑆳𑆤",
        "pos": "noun",
        "meaning_en": "Traditional multi-aperture earthen clay stove / kitchen hearth polished with yellow clay",
        "meaning_hi": "दान (कश्मीरी मिट्टी का पारंपरिक चूल्हा)",
        "etymology": "Sanskrit: Dāha / Agnyādhāna",
        "tags": ["household", "cuisine", "culture"],
        "aliases": ["dan", "hearth", "clay stove", "chulha"]
    },
    {
        "lemma": "Samāwār",
        "roman": "Samāwār",
        "devanagari": "समावार",
        "persoarabic": "سَماوار",
        "sharada": "𑆱𑆩𑆳𑆮𑆳𑆫",
        "pos": "noun",
        "meaning_en": "Traditional copper or brass kettle with central charcoal chamber for brewing Kehwa and Noon Chai",
        "meaning_hi": "समावार (चारकोल की भट्ठी वाली पारंपरिक कश्मीरी चायदानी)",
        "etymology": "Persian / Russian loan via Central Asian Silk Route",
        "tags": ["household", "tea", "cuisine", "crafts"],
        "aliases": ["samawar", "samovar", "tea kettle"]
    },
    {
        "lemma": "Kānī_Needle",
        "roman": "Kānī",
        "devanagari": "कानी",
        "persoarabic": "کانی",
        "sharada": "𑆑𑆳𑆤𑆵",
        "pos": "noun",
        "meaning_en": "Eyeless hardwood spool or bobbin used for weaving intricate Kani Pashmina shawls",
        "meaning_hi": "कानी (पश्मीना शॉल बुनने की पारंपरिक काष्ठ शलाका)",
        "etymology": "Sanskrit: Kānī (small reed / spool)",
        "tags": ["crafts", "textile", "pashmina"],
        "aliases": ["kani", "spool", "kani shawl", "weaving"]
    },
    {
        "lemma": "Shikāra",
        "roman": "Shikāra",
        "devanagari": "शिकारा",
        "persoarabic": "شِکارہ",
        "sharada": "𑆯𑆴𑆑𑆳𑆫𑆳",
        "pos": "noun",
        "meaning_en": "Traditional wooden light gondola boat steered with heart-shaped paddles across Dal and Nigeen lakes",
        "meaning_hi": "शिकारा (कश्मीर की प्रसिद्ध सुंदर काष्ठ नौका)",
        "etymology": "Persian / Kashmiri marine transport term",
        "tags": ["transport", "dal_lake", "culture"],
        "aliases": ["shikara", "gondola", "boat", "shikar"]
    },
    {
        "lemma": "Dūnga",
        "roman": "Dūnga",
        "devanagari": "डूंगा",
        "persoarabic": "ڈُونگَہ",
        "sharada": "𑆝𑆷𑆕𑇀𑆓𑆳",
        "pos": "noun",
        "meaning_en": "Traditional flat-bottomed wooden houseboat with woven reed matting walls used as family dwelling",
        "meaning_hi": "डूंगा (पारंपरिक कश्मीरी आवासीय नौका)",
        "etymology": "Indigenous boat construction term",
        "tags": ["transport", "architecture", "waterways"],
        "aliases": ["dunga", "doonga", "houseboat"]
    },
    {
        "lemma": "Tumbakhnārī",
        "roman": "Tumbakhnārī",
        "devanagari": "तुम्बखनारी",
        "persoarabic": "تُنبَک\u200cناری",
        "sharada": "𑆠𑆶𑆩𑇀𑆧𑆒𑆤𑆳𑆫𑆵",
        "pos": "noun",
        "meaning_en": "Traditional chalice-shaped clay goblet drum played by women during weddings and celebrations",
        "meaning_hi": "तुम्बकनारी (कश्मीरी मिट्टी का घड़ा-नुमा ढोलक / लोक वाद्य)",
        "etymology": "Persian: Tanbak + Nār (pipe)",
        "tags": ["music", "instruments", "folklore"],
        "aliases": ["tumbakhnari", "tumbaknari", "drum"]
    },
    {
        "lemma": "Kruh",
        "roman": "Krūh",
        "devanagari": "क्रूह",
        "persoarabic": "کروہ",
        "sharada": "𑆑𑇀𑆫𑆷𑆲",
        "pos": "noun",
        "meaning_en": "Traditional Kashmiri distance measure (league), approximately 2 statute miles / kos",
        "meaning_hi": "क्रूह (पारंपरिक दूरी की माप, लगभग दो मील / कोस)",
        "etymology": "Sanskrit: Krośa (क्रोश)",
        "tags": ["measurement", "distance", "revenue"],
        "aliases": ["kruh", "kuroh", "kos", "league"]
    },
    {
        "lemma": "Trākh",
        "roman": "Trākh",
        "devanagari": "त्राख",
        "persoarabic": "تراکھ",
        "sharada": "𑆠𑇀𑆫𑆳𑆒",
        "pos": "noun",
        "meaning_en": "Traditional Kashmiri dry capacity measure for grain, equivalent to approximately five seers",
        "meaning_hi": "त्राख (पारंपरिक अनाज माप, लगभग 5 सेर)",
        "etymology": "Sanskrit: Troṭaka / indigenous metric",
        "tags": ["measurement", "agriculture", "revenue"],
        "aliases": ["trakh", "grain measure", "traakh"]
    },
    {
        "lemma": "Krāl",
        "roman": "Krāl",
        "devanagari": "क्राल",
        "persoarabic": "کرال",
        "sharada": "𑆑𑇀𑆫𑆳𑆬",
        "pos": "noun",
        "meaning_en": "Traditional Kashmiri village potter who crafts earthenware pots, chilams, and kangri bowls",
        "meaning_hi": "क्राल (कुम्हार / मिट्टी के बर्तन बनाने वाला)",
        "etymology": "Sanskrit: Kulāla (कुलाल)",
        "tags": ["occupation", "crafts", "village"],
        "aliases": ["kral", "potter", "kumhar"]
    },
    {
        "lemma": "Khār_Smith",
        "roman": "Khār",
        "devanagari": "खार",
        "persoarabic": "کھار",
        "sharada": "𑆒𑆳𑆫",
        "pos": "noun",
        "meaning_en": "Blacksmith forging agricultural sickles, ploughshares, and cooking vessels",
        "meaning_hi": "खार (लोहार / धातु-शिल्पी)",
        "etymology": "Sanskrit: Karmakāra (कर्मकार)",
        "tags": ["occupation", "crafts"],
        "aliases": ["khar", "blacksmith", "lohar"]
    },
    {
        "lemma": "Pāts_Husk",
        "roman": "Pāts",
        "devanagari": "पाच़",
        "persoarabic": "پاژ",
        "sharada": "𑆥𑆳𑆖",
        "pos": "noun",
        "meaning_en": "Paddy chaff and rice husks winnowed after grain pounding",
        "meaning_hi": "पाच (धान की भूसी / छिलका)",
        "etymology": "Indo-Aryan cereal processing term",
        "tags": ["agriculture", "food"],
        "aliases": ["pats", "chaff", "husk", "bhoosa"]
    },
    {
        "lemma": "Wāyin",
        "roman": "Wāyin",
        "devanagari": "वायिन",
        "persoarabic": "وایِن",
        "sharada": "𑆮𑆳𑆪𑆴𑆤",
        "pos": "noun",
        "meaning_en": "Traditional Kashmiri grocer, apothecary, and dry merchant",
        "meaning_hi": "वायिन (पंसारी / किराना व जड़ी-बूटी विक्रेता)",
        "etymology": "Sanskrit: Vaṇij (वणिज्)",
        "tags": ["occupation", "commerce"],
        "aliases": ["wayin", "wain", "grocer", "bansari"]
    },
    {
        "lemma": "Gārī_Chestnut",
        "roman": "Gārī",
        "devanagari": "गारी",
        "persoarabic": "گاری",
        "sharada": "𑆓𑆳𑆫𑆵",
        "pos": "noun",
        "meaning_en": "Water-chestnut (Trapa bispinosa) harvested en masse from Wular Lake for flour",
        "meaning_hi": "गारी (सिंघाड़ा / वूलर झील की जलीय उपज)",
        "etymology": "Sanskrit: Śṛṅgāṭaka (शृङ्गाटक)",
        "tags": ["nature", "flora", "food", "wular"],
        "aliases": ["gari", "singhara", "water chestnut"]
    },
    {
        "lemma": "Kanz",
        "roman": "Kanz",
        "devanagari": "कन्ज़",
        "persoarabic": "کَنز",
        "sharada": "𑆑𑆤𑇀𑆘",
        "pos": "noun",
        "meaning_en": "Massive stone or heavy wood mortar for traditional manual rice husking",
        "meaning_hi": "कन्ज़ (धान कूटने की भारी ओखली)",
        "etymology": "Sanskrit: Kaṇḍanī (कण्डनी)",
        "tags": ["household", "agriculture", "tools"],
        "aliases": ["kanz", "mortar", "okhli"]
    },
    {
        "lemma": "Mōhul",
        "roman": "Mōhul",
        "devanagari": "मोहोल",
        "persoarabic": "موہُل",
        "sharada": "𑆩𑆾𑆲𑆶𑆬",
        "pos": "noun",
        "meaning_en": "Heavy rounded wooden pestle used with Kanz for pounding grain and husking paddy",
        "meaning_hi": "मोहोल (धान कूटने का भारी मूसल)",
        "etymology": "Sanskrit: Musala (मुसल)",
        "tags": ["household", "agriculture", "tools"],
        "aliases": ["mohul", "pestle", "mooshal"]
    },
    {
        "lemma": "Kūth_Costus",
        "roman": "Kūth",
        "devanagari": "कूथ",
        "persoarabic": "کوٗتھ",
        "sharada": "𑆑𑆷𑆡",
        "pos": "noun",
        "meaning_en": "Himalayan Costus root (Saussurea costus); celebrated aromatic and medicinal root of Kashmir highlands",
        "meaning_hi": "कूथ (कुष्ठ / सुगंधित हिमालयी औषधीय जड़)",
        "etymology": "Sanskrit: Kuṣṭha (कुष्ठ)",
        "tags": ["nature", "flora", "medicine", "trade"],
        "aliases": ["kuth", "costus", "medicinal root"]
    },

    # -------------------------------------------------------------
    # 2. From Sir Richard Carnac Temple: The Word of Lalla (1924)
    #    (Kashmir Shaivism, Vakhs, Spiritual Realization)
    # -------------------------------------------------------------
    {
        "lemma": "Anāhata",
        "roman": "Anāhata",
        "devanagari": "अनाहत",
        "persoarabic": "اَناہَت",
        "sharada": "𑆃𑆤𑆳𑆲𑆠",
        "pos": "noun",
        "meaning_en": "Unstruck mystical sound / heart chakra vibration realized in deep yogic absorption",
        "meaning_hi": "अनाहत (हृदय चक्र की दिव्य अनाहत ध्वनि)",
        "etymology": "Sanskrit: Anāhata-dhvani",
        "tags": ["philosophy", "shaivism", "spirituality"],
        "aliases": ["anahata", "anahat", "unstruck sound"]
    },
    {
        "lemma": "Chitta_Consciousness",
        "roman": "Chitta",
        "devanagari": "चित्त",
        "persoarabic": "چِتّ",
        "sharada": "𑆖𑆴𑆠𑇀𑆠",
        "pos": "noun",
        "meaning_en": "Individual consciousness, receptive mind, and heart reflection in Kashmiri Shaiva philosophy",
        "meaning_hi": "चित्त (अंतःकरण / चेतना)",
        "etymology": "Sanskrit: Citta (चित्त)",
        "tags": ["philosophy", "mind", "shaivism"],
        "aliases": ["chitta", "chitt", "mind", "consciousness"]
    },
    {
        "lemma": "Kundalinī",
        "roman": "Kundalinī",
        "devanagari": "कुण्डलिनी",
        "persoarabic": "کُنڈَلِنی",
        "sharada": "𑆑𑆶𑆟𑇀𑆝𑆬𑆴𑆤𑆵",
        "pos": "noun",
        "meaning_en": "Primordial dormant cosmic energy ascending through the chakras to unite with Shiva",
        "meaning_hi": "कुण्डलिनी (मूलाधार से सहस्रार तक जागृत होने वाली शक्ति)",
        "etymology": "Sanskrit: Kuṇḍalinī (कुण्डलिनी)",
        "tags": ["philosophy", "yoga", "shaivism"],
        "aliases": ["kundalini", "serpent energy", "spiritual power"]
    },
    {
        "lemma": "Sahasrāra",
        "roman": "Sahasrāra",
        "devanagari": "सहस्रार",
        "persoarabic": "سَہَسْرار",
        "sharada": "𑆱𑆲𑆱𑇀𑆫𑆳𑆫",
        "pos": "noun",
        "meaning_en": "Thousand-petaled lotus chakra at the crown of the head where Shiva and Shakti dissolve in unity",
        "meaning_hi": "सहस्रार चक्र (शिरोबिंदु पर स्थित सहस्रदल कमल, शिव-शक्ति का मिलन स्थल)",
        "etymology": "Sanskrit: Sahasrāra-kamala",
        "tags": ["philosophy", "yoga", "shaivism"],
        "aliases": ["sahasrara", "crown chakra", "thousand petaled lotus"]
    },
    {
        "lemma": "Spanda",
        "roman": "Spanda",
        "devanagari": "स्पन्द",
        "persoarabic": "سپَند",
        "sharada": "𑆱𑇀𑆥𑆤𑇀𑆢",
        "pos": "noun",
        "meaning_en": "Divine dynamic pulsation / creative vibration of supreme consciousness manifesting the universe",
        "meaning_hi": "स्पंद (कश्मीर शैवदर्शन का मूलभूत तत्त्व: चेतना का दिव्य कंपन)",
        "etymology": "Sanskrit: Spanda-kārikā (Vasugupta / Kallata)",
        "tags": ["philosophy", "shaivism", "trika"],
        "aliases": ["spanda", "divine pulsation", "vibration"]
    },
    {
        "lemma": "Pratyabhijñā",
        "roman": "Pratyabhijñā",
        "devanagari": "प्रत्यभिज्ञा",
        "persoarabic": "پْرَتْیَبھِجْنا",
        "sharada": "𑆥𑇀𑆫𑆠𑇀𑆪𑆨𑆴𑆘𑇀𑆚𑆳",
        "pos": "noun",
        "meaning_en": "Spontaneous recognition of the self as identical with the supreme Lord Shiva (Utpaladeva & Abhinavagupta)",
        "meaning_hi": "प्रत्यभिज्ञा (स्वयं को परमात्मा शिव रूप में पहचानना)",
        "etymology": "Sanskrit: Pratyabhijñā-hṛdayam",
        "tags": ["philosophy", "shaivism", "trika"],
        "aliases": ["pratyabhijna", "recognition", "kashmir shaivism"]
    },
    {
        "lemma": "Shūnya_Void",
        "roman": "Shūnya",
        "devanagari": "शून्य",
        "persoarabic": "شوٗنیَہ",
        "sharada": "𑆯𑆷𑆤𑇀𑆪",
        "pos": "noun",
        "meaning_en": "The supreme transcendent void (Shunya-Niranjana) where all objective attributes dissolve in pure awareness",
        "meaning_hi": "शून्य (परम शून्यावस्था / निर्विकल्प पद)",
        "etymology": "Sanskrit: Śūnya (शून्य)",
        "tags": ["philosophy", "mysticism", "vakhs"],
        "aliases": ["shunya", "void", "transcendence"]
    },
    {
        "lemma": "Vākh_Poem",
        "roman": "Vākh",
        "devanagari": "वाख",
        "persoarabic": "واکھ",
        "sharada": "𑆮𑆳𑆒",
        "pos": "noun",
        "meaning_en": "Classical four-line mystical aphoristic verse composed by Lal Ded (Lalleshwari)",
        "meaning_hi": "वाख (लाल देद द्वारा रचित चार पंक्तियों का गूढ़ दार्शनिक पद)",
        "etymology": "Sanskrit: Vāk (वाक् - sacred word)",
        "tags": ["literature", "poetry", "lal_ded", "folklore"],
        "aliases": ["vakh", "vaakh", "lal ded verse"]
    },
    {
        "lemma": "Amrīta_Nectar",
        "roman": "Amrīta",
        "devanagari": "अमृत",
        "persoarabic": "اَمْرِت",
        "sharada": "𑆃𑆩𑆸𑆠",
        "pos": "noun",
        "meaning_en": "Nectar of divine consciousness and immortality experienced by yogic adepts",
        "meaning_hi": "अमृत (दिव्य आनंद का रस / सुधा)",
        "etymology": "Sanskrit: Amṛta (अमृत)",
        "tags": ["philosophy", "spirituality"],
        "aliases": ["amrita", "amrit", "nectar"]
    },
    {
        "lemma": "Tattva_Principle",
        "roman": "Tattva",
        "devanagari": "तत्त्व",
        "persoarabic": "تَتْو",
        "sharada": "𑆠𑆠𑇀𑆠𑇀𑆮",
        "pos": "noun",
        "meaning_en": "Ontological reality principle (the 36 cosmic levels of reality in Trika Kashmir Shaivism)",
        "meaning_hi": "तत्त्व (कश्मीर शैवदर्शन के 36 विश्व-रचनात्मक स्तर)",
        "etymology": "Sanskrit: Tattva (तत्त्व)",
        "tags": ["philosophy", "shaivism", "cosmology"],
        "aliases": ["tattva", "tattwa", "principle"]
    },

    # -------------------------------------------------------------
    # 3. From Pandit Anand Koul: The Kashmiri Pandit (1924)
    #    (Socio-cultural Customs, Festivals, Ritual Artefacts)
    # -------------------------------------------------------------
    {
        "lemma": "Hērath",
        "roman": "Hērath",
        "devanagari": "हेरथ",
        "persoarabic": "ہیرَتھ",
        "sharada": "𑆲𑆼𑆫𑆡",
        "pos": "noun",
        "meaning_en": "Maha Shivaratri; the paramount religious and cultural festival of Kashmiri Pandits",
        "meaning_hi": "हेरथ (महाशिवरात्रि: कश्मीरी समाज का सर्वोच्च महापर्व)",
        "etymology": "Sanskrit: Hararātri (हररात्रि - Night of Shiva)",
        "tags": ["festivals", "sacred", "culture", "shiva"],
        "aliases": ["herath", "shivratri", "hararatri"]
    },
    {
        "lemma": "Vātak_Pitcher",
        "roman": "Vātak",
        "devanagari": "वातक",
        "persoarabic": "واتَک",
        "sharada": "𑆮𑆳𑆠𑆑",
        "pos": "noun",
        "meaning_en": "Sacred earthenware vessel worshipped as the embodiment of Lord Shiva during Herath, filled with walnuts and water",
        "meaning_hi": "वातक (हेरथ पूजा में शिव-स्वरूप मिट्टी का पवित्र कलश)",
        "etymology": "Sanskrit: Vaṭaka (वटुक)",
        "tags": ["festivals", "herath", "ritual", "sacred"],
        "aliases": ["vatak", "watak", "vatak puja", "herath pitcher"]
    },
    {
        "lemma": "Sōnth",
        "roman": "Sōnth",
        "devanagari": "सोन्थ",
        "persoarabic": "سونٛتھ",
        "sharada": "𑆱𑆾𑆤𑇀𑆡",
        "pos": "noun",
        "meaning_en": "Festival of the arrival of Spring celebrated on the first day of Chaitra with morning sight of sacred thali",
        "meaning_hi": "सोन्थ (वसंत आगमन का पारंपरिक कश्मीरी पर्व)",
        "etymology": "Sanskrit: Vasanta (वसन्त)",
        "tags": ["festivals", "seasons", "spring"],
        "aliases": ["sonth", "spring festival", "vasant"]
    },
    {
        "lemma": "Navrēh_NewYear",
        "roman": "Navrēh",
        "devanagari": "नवरेह",
        "persoarabic": "نَورؠہ",
        "sharada": "𑆤𑆮𑇀𑆫𑆼𑆲",
        "pos": "noun",
        "meaning_en": "Kashmiri Lunar New Year marking the inauguration of the ancient Saptrishi Samvat era",
        "meaning_hi": "नवरेह (कश्मीरी नववर्ष / सप्तर्षि संवत का प्रथम दिवस)",
        "etymology": "Sanskrit: Nava-varṣa (नववर्ष)",
        "tags": ["festivals", "calendar", "culture"],
        "aliases": ["navreh", "new year", "kashmiri new year"]
    },
    {
        "lemma": "Thāl_Barun",
        "roman": "Thāl Barun",
        "devanagari": "थाल बरुन",
        "persoarabic": "تھال بَرُن",
        "sharada": "𑆡𑆳𑆬 𑆧𑆫𑆶𑆤",
        "pos": "noun",
        "meaning_en": "Auspicious custom of filling a bronze platter with rice, walnuts, mirror, coins, and flowers for New Year darshan",
        "meaning_hi": "थाल भरुन (नवरेह की पूर्व संध्या पर चावल, दर्पण, अखरोट से थाली सजाने की रस्म)",
        "etymology": "Kashmiri compound: Thāl (plate) + Barun (to fill)",
        "tags": ["festivals", "navreh", "customs"],
        "aliases": ["thal barun", "thali darshan", "navreh thali"]
    },
    {
        "lemma": "Zar_Kāsai",
        "roman": "Zar Kāsai",
        "devanagari": "ज़र कासाइ",
        "persoarabic": "زَر کاسَی",
        "sharada": "𑆘𑆫𑇀 𑆑𑆳𑆱𑆽",
        "pos": "noun",
        "meaning_en": "Sacred first hair-cutting / tonsure ceremony performed for a child at ancestral shrines",
        "meaning_hi": "ज़र कासाइ (मुंडन संस्कार / चूड़ाकर्म)",
        "etymology": "Sanskrit: Keśa-saṃskāra / Persian: Zar",
        "tags": ["rituals", "kinship", "family"],
        "aliases": ["zar kasai", "mundan", "tonsure ceremony"]
    },
    {
        "lemma": "Mēkhla",
        "roman": "Mēkhla",
        "devanagari": "मेखला",
        "persoarabic": "میکھلا",
        "sharada": "𑆩𑆼𑆒𑆬𑆳",
        "pos": "noun",
        "meaning_en": "Sacred Yajnopavita investiture ceremony (Munji) wherein the youth receives the sacred thread",
        "meaning_hi": "मेखला (यज्ञोपवीत संस्कार / जनेऊ धारण रस्म)",
        "etymology": "Sanskrit: Mekhalā (मेखला)",
        "tags": ["rituals", "sacred", "culture"],
        "aliases": ["mekhla", "yajnopavita", "yagnya", "janeu"]
    },
    {
        "lemma": "Kāv_Punya",
        "roman": "Kāv Punya",
        "devanagari": "काव पुन्य",
        "persoarabic": "کاو پُنیَہ",
        "sharada": "𑆑𑆳𑆮 𑆥𑆶𑆤𑇀𑆪",
        "pos": "noun",
        "meaning_en": "Winter folk ritual of feeding yellow khichdi to crows on the full moon day of Posh",
        "meaning_hi": "काव पुन्य (पौष पूर्णिमा पर कौओं को खिचड़ी खिलाने का पारंपरिक अनुष्ठान)",
        "etymology": "Sanskrit: Kāka-puṇya (काक-पुण्य)",
        "tags": ["folklore", "rituals", "winter"],
        "aliases": ["kav punya", "crow feeding", "khichdi ritual"]
    },
    {
        "lemma": "Gādda_Batta",
        "roman": "Gādda Batta",
        "devanagari": "गाड बत्त",
        "persoarabic": "گاڈ بَتہ",
        "sharada": "𑆓𑆳𑆝 𑆧𑆠𑇀𑆠",
        "pos": "noun",
        "meaning_en": "Traditional winter ritual feast offering fresh river fish and cooked rice to the protective deity Yaksha",
        "meaning_hi": "गाड बत्त (यक्ष की प्रसन्नता हेतु मछली-भात का पारंपरिक भोग)",
        "etymology": "Kashmiri: Gādda (fish) + Batta (cooked rice)",
        "tags": ["cuisine", "rituals", "yaksha", "folklore"],
        "aliases": ["gadda batta", "gaad bata", "fish and rice"]
    },
    {
        "lemma": "Vātak_Rāza",
        "roman": "Vātak Rāza",
        "devanagari": "वातक राज़",
        "persoarabic": "واتَک رازہ",
        "sharada": "𑆮𑆳𑆠𑆑 𑆫𑆳𑆘",
        "pos": "noun",
        "meaning_en": "King of the Herath vessels personifying Lord Shiva crowned with flowers and walnut offerings",
        "meaning_hi": "वातक राजा (शिवरात्रि का मुख्य कलश जो देवाधिदेव शिव का प्रतीक है)",
        "etymology": "Sanskrit: Vaṭuka-rāja (वटुकराज)",
        "tags": ["festivals", "herath", "sacred"],
        "aliases": ["vatak raza", "watak raja", "vatak raja"]
    },
    {
        "lemma": "Dulīj",
        "roman": "Dulīj",
        "devanagari": "डुलिज",
        "persoarabic": "ڈُلِج",
        "sharada": "𑆝𑆶𑆬𑆴𑆘",
        "pos": "noun",
        "meaning_en": "Smaller earthen vessel placed beside Vataka Raja personifying Mother Goddess Parvati",
        "meaning_hi": "डुलिज (हेरथ पूजा में पार्वती स्वरूपा लघु कलशी)",
        "etymology": "Indigenous sacred pottery term",
        "tags": ["festivals", "herath", "sacred"],
        "aliases": ["dulij", "dulji", "parvati pitcher"]
    },
    {
        "lemma": "Wanvun_Chorus",
        "roman": "Wanvun",
        "devanagari": "वनवुन",
        "persoarabic": "وَن‌وُن",
        "sharada": "𑆮𑆤𑇀𑆮𑆶𑆤",
        "pos": "noun",
        "meaning_en": "Traditional choral wedding chant sung in harmonic Vedic meter by groups of women",
        "meaning_hi": "वनवुन (विवाह एवं मांगलिक अवसरों पर गाया जाने वाला पारंपरिक सामूहिक गान)",
        "etymology": "Sanskrit: Vana-gāna / indigenous meter",
        "tags": ["music", "folklore", "wedding"],
        "aliases": ["wanvun", "vanvun", "wedding song"]
    },

    # -------------------------------------------------------------
    # 4. From Dr. Georg Bühler: Detailed Report of a Tour (1877)
    #    (Sharada Palaeography, Ancient Manuscripts, Epigraphy)
    # -------------------------------------------------------------
    {
        "lemma": "Bhūrjapatra",
        "roman": "Bhūrjapatra",
        "devanagari": "भूर्जपत्र",
        "persoarabic": "بھوٗرجَہ پَتْر",
        "sharada": "𑆨𑆷𑆫𑇀𑆘𑆥𑆠𑇀𑆫",
        "pos": "noun",
        "meaning_en": "Prepared Himalayan birch bark (Betula utilis) historically utilized for ancient Sharada manuscripts",
        "meaning_hi": "भूर्जपत्र (शारदा पाण्डुलिपियों हेतु प्रयुक्त हिमालयी भोजपत्र)",
        "etymology": "Sanskrit: Bhūrja-pattra (भूर्जपत्र)",
        "tags": ["manuscripts", "sharada", "history", "epigraphy"],
        "aliases": ["bhurjapatra", "birch bark", "bhurja leaf"]
    },
    {
        "lemma": "Siyāhī_Almond",
        "roman": "Siyāhī",
        "devanagari": "सियाही",
        "persoarabic": "سیاہی",
        "sharada": "𑆱𑆴𑆪𑆳𑆲𑆵",
        "pos": "noun",
        "meaning_en": "Waterproof indelible manuscript ink prepared by Kashmiri scribes from burnt almond shell soot and gum",
        "meaning_hi": "सियाही (बादाम की छाल से बनी जल-रोधी कश्मीरी पाण्डुलिपि स्याही)",
        "etymology": "Persian: Siyāhī (blackness)",
        "tags": ["manuscripts", "crafts", "calligraphy"],
        "aliases": ["siyahi", "ink", "almond ink", "kashmiri ink"]
    },
    {
        "lemma": "Pōthī_Codex",
        "roman": "Pōthī",
        "devanagari": "पोथी",
        "persoarabic": "پوتھی",
        "sharada": "𑆥𑆾𑆡𑆵",
        "pos": "noun",
        "meaning_en": "Traditional unbound or cord-bound birch-bark manuscript codex containing sacred scriptures",
        "meaning_hi": "पोथी (पारंपरिक हस्तलिखित ग्रंथ / पाण्डुलिपि)",
        "etymology": "Sanskrit: Pustikā (पुस्तिका)",
        "tags": ["manuscripts", "literature", "scholarship"],
        "aliases": ["pothi", "codex", "manuscript"]
    },
    {
        "lemma": "Prashastī_Inscription",
        "roman": "Prashastī",
        "devanagari": "प्रशस्ति",
        "persoarabic": "پْرَشَسْتی",
        "sharada": "𑆥𑇀𑆫𑆯𑆱𑇀𑆠𑆴",
        "pos": "noun",
        "meaning_en": "Eulogistic stone or metallic inscription in Sharada script commemorating monarchs, temples, or bridges",
        "meaning_hi": "प्रशस्ति (शिलालेख / राजाज्ञा व कीर्ति-गाथा)",
        "etymology": "Sanskrit: Praśasti (प्रशस्ति)",
        "tags": ["epigraphy", "archaeology", "history"],
        "aliases": ["prashasti", "inscription", "stone inscription"]
    },
    {
        "lemma": "Shāradā_Pītha",
        "roman": "Shāradā Pītha",
        "devanagari": "शारदा पीठ",
        "persoarabic": "شاردا پیٹھ",
        "sharada": "𑆯𑆳𑆫𑆢𑆳 𑆥𑆵𑆜",
        "pos": "noun",
        "meaning_en": "Ancient temple university and intellectual seat of learning on the Kishenganga river where the Sharada script originated",
        "meaning_hi": "शारदा पीठ (किशनगंगा नदी तट पर स्थित प्राचीन विद्यापीठ व शक्तिपीठ)",
        "etymology": "Sanskrit: Śāradā-pīṭha (Seat of Goddess Saraswati)",
        "tags": ["history", "sacred", "sharada", "pilgrimage"],
        "aliases": ["sharada peeth", "sharda peeth", "sharada pitha"]
    },

    # -------------------------------------------------------------
    # 5. From Dutt: Kings of Kashmira (Rajatarangini Chronicles)
    #    (Historical Capitals, Dynasties, Legendary Rulers)
    # -------------------------------------------------------------
    {
        "lemma": "Pravarapura",
        "roman": "Pravarapura",
        "devanagari": "प्रवरपुर",
        "persoarabic": "پْرَوَرَپوٗر",
        "sharada": "𑆥𑇀𑆫𑆮𑆫𑆥𑆶𑆫",
        "pos": "noun",
        "meaning_en": "Ancient historical name of Srinagar founded in the 6th century CE by King Pravarasena II",
        "meaning_hi": "प्रवरपुर (राजा प्रवरसेन द्वारा स्थापित श्रीनगर का प्राचीन नाम)",
        "etymology": "Sanskrit: Pravarasena-pura",
        "tags": ["history", "geography", "toponym", "srinagar"],
        "aliases": ["pravarapura", "ancient srinagar"]
    },
    {
        "lemma": "Parihāsapura",
        "roman": "Parihāsapura",
        "devanagari": "परिहासपुर",
        "persoarabic": "پَرِہاسَپوٗر",
        "sharada": "𑆥𑆫𑆴𑆲𑆳𑆱𑆥𑆶𑆫",
        "pos": "noun",
        "meaning_en": "City of Smiles; monumental imperial capital founded by Emperor Lalitaditya Muktapida in the 8th century CE",
        "meaning_hi": "परिहासपुर (सम्राट ललितादित्य द्वारा निर्मित भव्य साम्राज्यीय राजधानी)",
        "etymology": "Sanskrit: Parihāsa (mirth/smiles) + Pura (city)",
        "tags": ["history", "archaeology", "toponym"],
        "aliases": ["parihaspura", "parihasapura", "city of smiles"]
    },
    {
        "lemma": "Suyyapura",
        "roman": "Suyyapura",
        "devanagari": "सुय्यपुर",
        "persoarabic": "سُویَّہ پوٗر",
        "sharada": "𑆱𑆶𑆪𑇀𑆪𑆥𑆶𑆫",
        "pos": "noun",
        "meaning_en": "Ancient name of modern Sopore, founded in honor of the genius hydrologist and irrigation engineer Suyya",
        "meaning_hi": "सुय्यपुर (सोपोर का प्राचीन नाम, महान जल-अभियंता सुय्य के नाम पर)",
        "etymology": "Sanskrit: Suyyā-pura",
        "tags": ["history", "geography", "toponym", "sopore"],
        "aliases": ["suyyapura", "sopore", "suyya"]
    },
    {
        "lemma": "Padmapūra",
        "roman": "Padmapūra",
        "devanagari": "पद्मपुर",
        "persoarabic": "پَدْمَہ پوٗر",
        "sharada": "𑆥𑆢𑇀𑆩𑆥𑆶𑆫",
        "pos": "noun",
        "meaning_en": "Ancient historical name of modern Pampore, founded by Minister Padma and famous globally for saffron",
        "meaning_hi": "पद्मपुर (पांपोर का ऐतिहासिक नाम: विश्वविख्यात केसर की भूमि)",
        "etymology": "Sanskrit: Padma-pura",
        "tags": ["history", "toponym", "pampore", "saffron"],
        "aliases": ["padmapura", "pampore", "padampur"]
    },
    {
        "lemma": "Mārtanda_Temple",
        "roman": "Mārtanda",
        "devanagari": "मार्तण्ड",
        "persoarabic": "مارْتَنڈ",
        "sharada": "𑆩𑆳𑆫𑇀𑆠𑆟𑇀𑆝",
        "pos": "noun",
        "meaning_en": "Colossal Sun Temple built by Emperor Lalitaditya atop the Mattan plateau overlooking the Valley",
        "meaning_hi": "मार्तण्ड सूर्य मंदिर (मट्टन करेवा पर सम्राट ललितादित्य द्वारा निर्मित सूर्य मंदिर)",
        "etymology": "Sanskrit: Mārtaṇḍa (The Sun God)",
        "tags": ["history", "archaeology", "temple", "sun_god"],
        "aliases": ["martand", "martanda", "sun temple"]
    },
    {
        "lemma": "Varāhamūla",
        "roman": "Varāhamūla",
        "devanagari": "वराहमूल",
        "persoarabic": "وَراہَمُول",
        "sharada": "𑆮𑆫𑆳𑆲𑆩𑆷𑆬",
        "pos": "noun",
        "meaning_en": "Ancient name of Baramulla, the Western gateway where Lord Vishnu's Boar incarnation bored through the mountain",
        "meaning_hi": "वराहमूल (बारामुला का प्राचीन नाम: भगवान वराह का पावन स्थल)",
        "etymology": "Sanskrit: Varāha-mūla (Root of the Boar)",
        "tags": ["history", "geography", "toponym", "baramulla"],
        "aliases": ["varahamula", "baramulla", "varaha"]
    },
    {
        "lemma": "Kārkōta_Empire",
        "roman": "Kārkōta",
        "devanagari": "कार्कोट",
        "persoarabic": "کارکوٹ",
        "sharada": "𑆑𑆳𑆫𑇀𑆑𑆾𑆛",
        "pos": "noun",
        "meaning_en": "Illustrious imperial dynasty of Kashmir (625–855 CE) under whose rule Kashmir commanded vast territories across Asia",
        "meaning_hi": "कार्कोट साम्राज्य (कश्मीर का प्रतापी राजवंश जिसके सम्राट ललितादित्य थे)",
        "etymology": "Sanskrit: Kārkoṭa-nāga (कार्कोटक नाग)",
        "tags": ["history", "dynasty", "monarchy"],
        "aliases": ["karkota", "karkota dynasty", "karkota empire"]
    },
    {
        "lemma": "Budshāh_King",
        "roman": "Budshāh",
        "devanagari": "बुडशाह",
        "persoarabic": "بُڈشاہ",
        "sharada": "𑆧𑆶𑆝𑆯𑆳𑆲",
        "pos": "noun",
        "meaning_en": "The Great King; affectionate Kashmiri title of Sultan Zain-ul-Abidin who introduced shawls, papermaking, and silk to Kashmir",
        "meaning_hi": "बुडशाह (महान सुल्तान ज़ैन-उल-आबिदीन का लोकप्रिय कश्मीरी नाम)",
        "etymology": "Kashmiri: Bod (great) + Persian: Shāh (king)",
        "tags": ["history", "monarch", "sultanate"],
        "aliases": ["budshah", "zain-ul-abidin", "badshah", "great king"]
    },
    {
        "lemma": "Lalitāditya",
        "roman": "Lalitāditya",
        "devanagari": "ललितादित्य",
        "persoarabic": "لَلِتادِتیَہ",
        "sharada": "𑆬𑆬𑆴𑆠𑆳𑆢𑆴𑆠𑇀𑆪",
        "pos": "noun",
        "meaning_en": "Celebrated 8th-century Emperor of Kashmir (Muktapida) who built Martand and unified northern India",
        "meaning_hi": "ललितादित्य मुक्तापीड (कश्मीर के महान दिग्विजयी चक्रवर्ती सम्राट)",
        "etymology": "Sanskrit: Lalita + Āditya (Playful Sun)",
        "tags": ["history", "monarch", "hero"],
        "aliases": ["lalitaditya", "muktapida", "emperor"]
    },
    {
        "lemma": "Avantivarman",
        "roman": "Avantivarman",
        "devanagari": "अवन्तिवर्मन",
        "persoarabic": "اَوَنتِیوَرْمَن",
        "sharada": "𑆃𑆮𑆤𑇀𑆠𑆴𑆮𑆫𑇀𑆩𑆤𑇀",
        "pos": "noun",
        "meaning_en": "Beloved 9th-century King of Kashmir who ushered in a Golden Age of art, architecture, and literature",
        "meaning_hi": "अवन्तिवर्मन (उत्पल वंश के धर्मप्रिय राजा जिन्होंने अवंतीपुर बसाया)",
        "etymology": "Sanskrit: Avanti-varman",
        "tags": ["history", "monarch", "peace"],
        "aliases": ["avantivarman", "king avantivarman"]
    },
    {
        "lemma": "Kalhana_Chronicler",
        "roman": "Kalhana",
        "devanagari": "कल्हण",
        "persoarabic": "کَلْہَن",
        "sharada": "𑆑𑆬𑇀𑆲𑆟",
        "pos": "noun",
        "meaning_en": "Great 12th-century historian-poet of Kashmir who authored the Sanskrit chronicle Rajatarangini",
        "meaning_hi": "कल्हण (राजतरंगिणी के अमर रचयिता व भारत के महान प्रथम इतिहासकार)",
        "etymology": "Sanskrit: Kalhaṇa (कल्हण)",
        "tags": ["history", "literature", "rajatarangini"],
        "aliases": ["kalhana", "kalhan", "rajatarangini author"]
    },
    {
        "lemma": "Kōta_Rānī",
        "roman": "Kōta Rānī",
        "devanagari": "कोटा रानी",
        "persoarabic": "کوٹہ رانی",
        "sharada": "𑆑𑆾𑆛𑆳 𑆫𑆳𑆤𑆵",
        "pos": "noun",
        "meaning_en": "Courageous last Hindu queen sovereign of Kashmir who governed and fortified Srinagar in 1339 CE",
        "meaning_hi": "कोटा रानी (मध्यकालीन कश्मीर की वीर वीरांगना व अंतिम हिंदू महारानी)",
        "etymology": "Kashmiri royal honorific",
        "tags": ["history", "queen", "monarch"],
        "aliases": ["kota rani", "queen kota"]
    },

    # -------------------------------------------------------------
    # 6. From Vigne & Bernier: Historical Toponyms & Landscapes
    # -------------------------------------------------------------
    {
        "lemma": "Pīr_Panjāl",
        "roman": "Pīr Panjāl",
        "devanagari": "पीर पंजाल",
        "persoarabic": "پیٖر پَنجال",
        "sharada": "𑆥𑆵𑆫 𑆥𑆚𑇀𑆘𑆳𑆬",
        "pos": "noun",
        "meaning_en": "Magnificent snow-capped mountain range bounding the southwestern flank of the Kashmir Valley",
        "meaning_hi": "पीर पंजाल (कश्मीर घाटी की दक्षिणी सीमा बनाने वाली भव्य पर्वतमाला)",
        "etymology": "Sanskrit: Pāñcāladeva / Persian: Pīr (saint)",
        "tags": ["geography", "mountains"],
        "aliases": ["pir panjal", "panjal", "peer panjal"]
    },
    {
        "lemma": "Zōjī_Lā",
        "roman": "Zōjī Lā",
        "devanagari": "ज़ोजिला",
        "persoarabic": "زوجی لا",
        "sharada": "𑆘𑆾𑆘𑆴𑆬𑆳",
        "pos": "noun",
        "meaning_en": "High Himalayan mountain pass (3,528 m) connecting the Kashmir Valley with Ladakh and Tibet",
        "meaning_hi": "ज़ोजिला दर्रा (कश्मीर को लद्दाख से जोड़ने वाला ऐतिहासिक दर्रा)",
        "etymology": "Tibetan: Zoji-La (Pass of Blizzards)",
        "tags": ["geography", "mountain_pass", "ladakh"],
        "aliases": ["zoji la", "zojila", "zojila pass"]
    },
    {
        "lemma": "Manasbal_Lake",
        "roman": "Manasbal",
        "devanagari": "मानसबल",
        "persoarabic": "مانَس\u200cبَل",
        "sharada": "𑆩𑆳𑆤𑆱𑆧𑆬",
        "pos": "noun",
        "meaning_en": "The deepest freshwater lake in Kashmir, famous for extensive lotus blooms and Mughal ruins",
        "meaning_hi": "मानसबल झील (कश्मीर की सर्वाधिक गहरी एवं निर्मल झील, कमल पुष्पों हेतु प्रसिद्ध)",
        "etymology": "Sanskrit: Mānasa-saras (Lake Manasarovar)",
        "tags": ["geography", "lake", "nature"],
        "aliases": ["manasbal", "manasbal lake", "deep lake"]
    },
    {
        "lemma": "Konsarnāg",
        "roman": "Konsarnāg",
        "devanagari": "कौंसरनाग",
        "persoarabic": "کَونسَرناگ",
        "sharada": "𑆑𑆿𑆤𑇀𑆱𑆫𑆤𑆳𑆓",
        "pos": "noun",
        "meaning_en": "Sacred high-altitude glacial lake shaped like an elongated foot in the Pir Panjal range (Kramasarovara)",
        "meaning_hi": "कौंसरनाग (पीर पंजाल पर्वतमाला में स्थित पवित्र हिम सरोवर / क्रमसरोवर)",
        "etymology": "Sanskrit: Krama-saras (Footprint of Lord Vishnu)",
        "tags": ["geography", "lake", "sacred", "mountains"],
        "aliases": ["konsarnag", "kaunsarnag", "kramasarovara"]
    },
    {
        "lemma": "Gangabal_Lake",
        "roman": "Gangabal",
        "devanagari": "गंगाबल",
        "persoarabic": "گَنگَہ\u200cبَل",
        "sharada": "𑆓𑆕𑇀𑆔𑆳𑆧𑆬",
        "pos": "noun",
        "meaning_en": "Sacred alpine lake at the foot of Mount Haramukh, known as the Uttaraganga of Kashmir",
        "meaning_hi": "गंगाबल झील (हरमुख पर्वत के चरणों में स्थित पवित्र तीर्थ / उत्तरगंगा)",
        "etymology": "Sanskrit: Gaṅgā-bala (Strength of Ganga)",
        "tags": ["geography", "lake", "sacred", "haramukh"],
        "aliases": ["gangabal", "gangabal lake", "uttaraganga"]
    },
    {
        "lemma": "Haramukh_Peak",
        "roman": "Haramukh",
        "devanagari": "हरमुख",
        "persoarabic": "ہَرَمُکھ",
        "sharada": "𑆲𑆫𑆩𑆶𑆒",
        "pos": "noun",
        "meaning_en": "Sacred mountain summit (5,142 m) towering over northern Kashmir, revered as the Throne of Lord Shiva",
        "meaning_hi": "हरमुख पर्वत (कश्मीर का पवित्र कैलास: भगवान शिव का दिव्य मुकुट शिखर)",
        "etymology": "Sanskrit: Hara-mukha (Face of Shiva)",
        "tags": ["geography", "mountains", "shiva", "sacred"],
        "aliases": ["haramukh", "mount haramukh", "shiva peak"]
    },
    {
        "lemma": "Verināg_Spring",
        "roman": "Verināg",
        "devanagari": "वेरीनाग",
        "persoarabic": "ویری ناگ",
        "sharada": "𑆮𑆼𑆫𑆵𑆤𑆳𑆓",
        "pos": "noun",
        "meaning_en": "Deep blue octagonal spring and Mughal pleasure pavilion considered the official geographic source of River Vitasta (Jhelum)",
        "meaning_hi": "वेरीनाग (वितस्ता नदी का ऐतिहासिक उद्गम स्थल व अष्टकोणीय चश्मा)",
        "etymology": "Sanskrit: Vīranāga (वीरनाग)",
        "tags": ["geography", "spring", "vitasta", "water"],
        "aliases": ["verinag", "virnag", "vitasta source"]
    },
    {
        "lemma": "Chashma_Shāhī",
        "roman": "Chashma Shāhī",
        "devanagari": "चश्मा शाही",
        "persoarabic": "چَشمَہ شاہی",
        "sharada": "𑆖𑆯𑇀𑆩𑆳 𑆯𑆳𑆲𑆵",
        "pos": "noun",
        "meaning_en": "The Royal Spring garden in Srinagar built by Ali Mardan Khan in 1632 CE, famed for cold medicinal water",
        "meaning_hi": "चश्मा शाही (श्रीनगर का प्रसिद्ध मुग़ल बाग़, अपने शीतल औषधीय जल हेतु विख्यात)",
        "etymology": "Persian: Chashmah-i Shāhī (Royal Spring)",
        "tags": ["geography", "spring", "garden", "mughal"],
        "aliases": ["chashma shahi", "chashmashahi", "royal spring"]
    },
    {
        "lemma": "Gurēz_Valley",
        "roman": "Gurēz",
        "devanagari": "गुरेज",
        "persoarabic": "گُریز",
        "sharada": "𑆓𑆶𑆫𑆼𑆘",
        "pos": "noun",
        "meaning_en": "Picturesque deep alpine valley along the Kishanganga river, ancient Dardic bastion and Silk Route link",
        "meaning_hi": "गुरेज घाटी (किशनगंगा नदी तट पर बसी सुरम्य हिमालयी घाटी)",
        "etymology": "Indigenous Dardic toponym",
        "tags": ["geography", "valley", "dardic"],
        "aliases": ["gurez", "gurez valley", "dardi"]
    }
]

def enrich_lexicon():
    print(f"Loaded {len(NEW_LEXICAL_CANDIDATES)} newly extracted candidate words from downloaded sources.")
    existing_lemmas = {w["lemma"].lower() for w in WORDS_DATA}
    added_count = 0
    words_to_add = []

    for cand in NEW_LEXICAL_CANDIDATES:
        if cand["lemma"].lower() not in existing_lemmas:
            words_to_add.append(cand)
            existing_lemmas.add(cand["lemma"].lower())
            added_count += 1
        else:
            print(f"Skipping duplicate: {cand['lemma']}")

    print(f"Unique new words to integrate into WORDS_DATA: {len(words_to_add)}")

    words_data_path = os.path.abspath(r"c:\Users\Ankush Pandita\Desktop\koshur\koshur\lexicon\words_data.py")
    with open(words_data_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Find the end of WORDS_DATA list
    # WORDS_DATA: List[Dict[str, Any]] = [ ... ]
    # We can append the new entries right before the closing bracket ']'
    pos = code.rfind("]")
    if pos == -1:
        raise ValueError("Could not find closing bracket in words_data.py")

    new_entries_code = ""
    for w in words_to_add:
        new_entries_code += f",\n    {repr(w)}"

    updated_code = code[:pos] + new_entries_code + "\n]" + code[pos+1:]

    with open(words_data_path, "w", encoding="utf-8") as f:
        f.write(updated_code)

    print(f"Successfully integrated {len(words_to_add)} new historical words into {words_data_path}!")
    
    # Reload and verify
    import importlib
    import koshur.lexicon.words_data
    importlib.reload(koshur.lexicon.words_data)
    print(f"New WORDS_DATA count: {len(koshur.lexicon.words_data.WORDS_DATA)}")

if __name__ == "__main__":
    enrich_lexicon()
