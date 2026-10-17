"""
Authentic Kashmiri Classical Folk Songs, Ballads & Lyrics:
Transcribed with complete 4-script orthography, poet background,
musical modes, and literary translations.
"""

from typing import List, Dict, Any, Optional

TRADITIONAL_SONGS: List[Dict[str, Any]] = [
    {
        "id": "habba_khatoon_roshe",
        "title": "Cholhama Roshē (चोलहम रोशे / ژولہَم روشے)",
        "poet": "Habba Khatoon (हब्बा ख़ातून / حبہ خاتون, 16th Century)",
        "genre": "Lol-Lyric (Love Elegy)",
        "theme": "Yearning, abandonment, and intense emotional grief",
        "musical_genre": "Chakri / Sufiyana",
        "kashmiri_roman": "Tsholhama roshē roshē, myon dālay; Kāv pyom balay, wālō myon kāmēvān!",
        "kashmiri_dev": "छ़ोलहम रोशे रोशे, म्योन दालय; काव प्योम बलय, वालो म्योन कामेवान!",
        "kashmiri_arabic": "ژولہَم روشے روشے، میون دالَے؛ کاو پیوم بَلَے، والو میون کامیوَن!",
        "kashmiri_sharada": "𑆗𑆾𑆬𑆲𑆩 𑆫𑆾𑆯𑆼 𑆫𑆾𑆯𑆼 𑆩𑇀𑆪𑆾𑆤 𑆢𑆳𑆬𑆪𑇅 𑆑𑆳𑆮 𑆥𑇀𑆪𑆾𑆩 𑆧𑆬𑆪 𑆮𑆳𑆬𑆾 𑆩𑇀𑆪𑆾𑆤 𑆑𑆳𑆩𑆼𑆮𑆳𑆤𑇅",
        "translation_en": "You slipped away from me in anger and disdain, leaving my hem empty; May the evil omen fall on the crow instead—come back to me, my handsome beloved!",
        "historical_context": "Composed by Queen Habba Khatoon after Emperor Akbar exiled her husband King Yousuf Shah Chak to Bihar, leaving her to wander the saffron terraces of Pampore in grief."
    },
    {
        "id": "rasul_mir_posh_mal",
        "title": "Rinda Pōsh Māl Gindaney (रिन्द पोश माल गिन्दने / رِند پوش مال گِندَنے)",
        "poet": "Rasul Mir of Shahabad Dooru (रसूल मीर, 19th Century)",
        "genre": "Romantic Ghazal / Rouf",
        "theme": "Youthful joy, celebration of nature and blossoming spring flowers",
        "musical_genre": "Rouf / Chakri",
        "kashmiri_roman": "Rinda pōsh māl gindaney drāyī lōlē; Kastūri tōlay vanavun wōlē drāyī lōlē!",
        "kashmiri_dev": "रिन्द पोश माल गिन्दने द्रायी लोले; कस्तूरी तोलय वनवुन वोले द्रायी लोले!",
        "kashmiri_arabic": "رِند پوش مال گِندَنے درایی لولے؛ کَستوٗری تولَے وَنوُن وولے درایی لولے!",
        "kashmiri_sharada": "𑆫𑆴𑆤𑇀𑆢 𑆥𑆾𑆰 𑆩𑆳𑆬 𑆓𑆴𑆤𑇀𑆢𑆤𑆼 𑆢𑇀𑆫𑆳𑆪𑆵 𑆬𑆾𑆬𑆼𑇅 𑆑𑆱𑇀𑆠𑆷𑆫𑆵 𑆠𑆾𑆬𑆪 𑆮𑆤𑆮𑆶𑆤 𑆮𑆾𑆬𑆼 𑆢𑇀𑆫𑆳𑆪𑆵 𑆬𑆾𑆬𑆼𑇅",
        "translation_en": "Adorned with sweet flower garlands, my maiden steps out in love; Weighed against precious musk, the festive singers greet her arrival!",
        "historical_context": "Rasul Mir is renowned as the John Keats of Kashmiri romantic poetry, infusing sensual freshness into folk lyricism."
    },
    {
        "id": "traditional_wanvun_wedding",
        "title": "Puzhwani Wanvun (पुज़्वनि वन्वुन / پُزوَنِ ونوُن)",
        "poet": "Traditional Oral Tradition",
        "genre": "Wanvun (Antiphonal Choral Wedding Song)",
        "theme": "Invoking divine blessings for the bride and bridegroom",
        "musical_genre": "Choral A Capella",
        "kashmiri_roman": "Bismillāh karith wanvun wothu, dāpay shēhjar chhu phulyōmut; Shārikā māyē kar dayā, pōsh barkat bāranay!",
        "kashmiri_dev": "बिस्मिल्लाह करिथ वन्वुन वोथु, दापय शेहजर छु फुल्योमुत; शारिका माये कर दया, पोश बरकत बारनय!",
        "kashmiri_arabic": "بِسمِ اللہ کٔرِتھ وَنوُن ووتھُ، داپَے شیہجَر چھُ پھُلیومُت؛ شارِکا مایے کَر دَیا، پوش بَرکَت بارَنَے!",
        "kashmiri_sharada": "𑆧𑆴𑆱𑇀𑆩𑆴𑆬𑇀𑆬𑆳𑆲 𑆑𑆫𑆴𑆡 𑆮𑆤𑇀𑆮𑆶𑆤 𑆮𑆾𑆡𑆶 𑆢𑆳𑆥𑆪 𑆯𑆼𑆲𑆘𑆫 𑆗𑆶 𑆦𑆶𑆬𑇀𑆪𑆾𑆩𑆶𑆠𑇅 𑆯𑆳𑆫𑆴𑆑𑆳 𑆩𑆳𑆪𑆼 𑆑𑆫 𑆢𑆪𑆳 𑆥𑆾𑆯 𑆧𑆫𑇀𑆑𑆠 𑆧𑆳𑆫𑆤𑆪𑇅",
        "translation_en": "With sacred blessings the wedding song rises; cool soothing shade has blossomed in our courtyard; O Divine Mother shower Thy grace, and rain petals of abundance!",
        "historical_context": "Sung collectively by women as the bridegroom arrives at the bride's gate in Kashmir."
    },
    {
        "id": "arnimal_jasmine",
        "title": "Tsholhama Hyokum Na Thahar (छ़ोलहम ह्योकुम न ठहर / ژولہَم ہیوکُم نہ ٹَہر)",
        "poet": "Arnimal (अर्णिमाल / اَرنِی مال, 18th Century)",
        "genre": "Lol-Lyric",
        "theme": "The tender beauty of jasmine and unrequited longing",
        "musical_genre": "Chakri",
        "kashmiri_roman": "Tsholhama hyokum na thahar kithkan karay; Arni rang dryāv pōshē vanas manz!",
        "kashmiri_dev": "छ़ोलहम ह्योकुम न ठहर किथकन करय; अर्णि रंग द्र्याव पोशे वनस मन्ज़!",
        "kashmiri_arabic": "ژولہَم ہیوکُم نہ ٹَہر کِتھ کَن کَرَے؛ اَرنِ رَنگ دِریاو پوشے وَنَس مَنز!",
        "kashmiri_sharada": "𑆗𑆾𑆬𑆲𑆩 𑆲𑇀𑆪𑆾𑆑𑆶𑆩 𑆤 𑆜𑆲𑆫 𑆑𑆴𑆡𑆑𑆤 𑆑𑆫𑆪𑇅 𑆃𑆫𑇀𑆟𑆴 𑆫𑆕𑇀𑆔 𑆢𑇀𑆫𑇀𑆪𑆳𑆮 𑆥𑆾𑆰𑆼 𑆮𑆤𑆱 𑆩𑆤𑇀𑆘𑇅",
        "translation_en": "You slipped away, and I cannot bear this stillness—how shall I live? The wild yellow rose has bloomed inside the forest of my heart!",
        "historical_context": "Arnimal, wife of Munshi Bhawani Das Kachroo, composed exquisite lyrics comparing human love to delicate Kashmiri flowers."
    },
    {
        "id": "lal_ded_vakh_song",
        "title": "Gorun Wōnnam Kunuy Vatsun (गोरुन वोन्नम कुनुय वचुन / گورُن ونّم کُنُے وَژُن)",
        "poet": "Lal Ded (Lalleshwari, 14th Century)",
        "genre": "Vakh (Mystical Verse)",
        "theme": "Spiritual liberation through turning inward to the divine Self",
        "musical_genre": "Sufiyana / Classical Chant",
        "kashmiri_roman": "Gwarun wōnnam kunuy watsun, nēbrā dōpnam andray atsun; Tawa Lali mē gāv lūkh-thārun, natsun dyutnam vāryāh!",
        "kashmiri_dev": "ग्वरुन वोन्नम कुनुय वचुन, नेब्रा दोपनम अन्दरय अचुन; तव ललि मे गाव लूख-थारुन, नचुन द्युतनम वारियाह!",
        "kashmiri_arabic": "گورُن ونّم کُنُے وَژُن، نیبرا دوپنم اَندرَی اَژُن؛ تَوہ لَلِ میہ گاو لوٗکھ تھارُن، نَژُن دیُتنَم واریاہ!",
        "kashmiri_sharada": "𑆔𑇀𑆮𑆫𑆶𑆤 𑆮𑆾𑆤𑇀𑆤𑆩 𑆑𑆶𑆤𑆶𑆪 𑆮𑆖𑆶𑆤 𑆤𑆼𑆧𑇀𑆫𑆳 𑆢𑆾𑆥𑆤𑆩 𑆃𑆤𑇀𑆢𑇀𑆫𑆪 𑆃𑆖𑆶𑆤𑇅 𑆠𑆮 𑆬𑆬𑆴 𑆩𑆼 𑆓𑆳𑆮 𑆬𑆷𑆒𑆡𑆳𑆫𑆶𑆤 𑆤𑆖𑆶𑆤 𑆢𑇀𑆪𑆶𑆠𑆤𑆩 𑆮𑆳𑆫𑆴𑆪𑆳𑆲𑇅",
        "translation_en": "My Guru gave me but one single precept: 'Turn from the outward world and enter inward within thyself!' That became Lal Ded's supreme revelation, and I began dancing in ecstacy!",
        "historical_context": "The pinnacle vakh of Kashmir Trika Shaivism taught by Siddha Srikantha to Lalleshwari."
    }
]

def get_song(song_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a traditional Kashmiri song by its ID."""
    for s in TRADITIONAL_SONGS:
        if s["id"] == song_id.lower():
            return s
    return None

import unicodedata

def _clean_str(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()

def search_songs(query: str) -> List[Dict[str, Any]]:
    """Search traditional songs by title, poet, lyric keywords, or theme (diacritic-insensitive)."""
    raw_q = query.strip()
    clean_q = _clean_str(raw_q)
    results = []
    for s in TRADITIONAL_SONGS:
        roman_clean = _clean_str(s.get("kashmiri_roman", ""))
        trans_clean = _clean_str(s.get("translation_en", ""))
        title_clean = _clean_str(s.get("title", ""))
        poet_clean = _clean_str(s.get("poet", ""))
        theme_clean = _clean_str(s.get("theme", ""))
        
        if (
            clean_q in s["id"]
            or clean_q in title_clean
            or clean_q in poet_clean
            or clean_q in roman_clean
            or clean_q in trans_clean
            or clean_q in theme_clean
            or raw_q in s.get("kashmiri_dev", "")
            or raw_q in s.get("kashmiri_arabic", "")
            or raw_q in s.get("kashmiri_sharada", "")
        ):
            results.append(s)
    return results

def get_all_songs() -> List[Dict[str, Any]]:
    """Return all cataloged traditional Kashmiri songs."""
    return TRADITIONAL_SONGS
