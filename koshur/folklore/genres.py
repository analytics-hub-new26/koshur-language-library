"""
Kashmiri Folk Music Genres, Dance Traditions & Theatre:
Authentic documentation of Wanvun (wedding songs), Rouf (folk dance),
Chakri, Sufiyana Kalam, Ladishah, and Bhand Pather.
"""

from typing import List, Dict, Any, Optional

FOLKLORE_GENRES: List[Dict[str, Any]] = [
    {
        "id": "wanvun",
        "name": "Wanvun",
        "devanagari": "वन्वुन",
        "persoarabic": "ونوُن",
        "sharada": "𑆮𑆤𑇀𑆮𑆶𑆤",
        "category": "vocal_folk_ritual",
        "description": "Antiphonal choral singing tradition performed exclusively by women during weddings and auspicious family ceremonies. Sung without any musical instruments in slow, sustained undulating cadence.",
        "subtypes": [
            "Manzirāt Wanvun (Henna night songs)",
            "Devagōn Wanvun (Purificatory bathing & yajnopavita rituals)",
            "Lagn Wanvun (Nuptial union hymns)",
            "Phirlath Wanvun (Post-wedding welcome songs)"
        ],
        "cultural_significance": "Sanctifies household milestones in both Kashmiri Pandit and Muslim traditions. Kashmiri Pandits invoke Goddess Sharika, Maharagnya, and the Vitasta River; Kashmiri Muslims invoke the Prophet, Bibi Fatima, and Sufi saints.",
        "sample_verse": {
            "kashmiri_roman": "Shārikā māyē kar dayā, Mahārāgnyē kar dayā...",
            "kashmiri_dev": "शारिका माये कर दया, महाराज्ञे कर दया...",
            "kashmiri_arabic": "شارِکا مایے کَر دَیا، مَہاراگنے کَر دَیا...",
            "kashmiri_sharada": "𑆯𑆳𑆫𑆴𑆑𑆳 𑆩𑆳𑆪𑆼 𑆑𑆫 𑆢𑆪𑆳 𑆩𑆲𑆳𑆫𑆳𑆘𑇀𑆚𑆼 𑆑𑆫 𑆢𑆪𑆳𑇅",
            "translation_en": "O Mother Sharika shower Thy divine grace; O Mother Maharagnya bless this home with auspiciousness..."
        }
    },
    {
        "id": "rouf",
        "name": "Rouf",
        "devanagari": "रूफ़",
        "persoarabic": "روٗف",
        "sharada": "𑆫𑆷𑆦",
        "category": "folk_dance_song",
        "description": "The quintessential celebratory Kashmiri women's dance and lyrical song. Performed in two facing rows with arms linked across shoulders, moving forward and backward in synchronized rhythmic footwork.",
        "occasions": ["Eid-ul-Fitr", "Navreh (New Year)", "Spring harvest", "Weddings"],
        "musical_tempo": "Starts in graceful slow lilt (Mandra) and accelerates to jubilant climax (Drut).",
        "sample_verse": {
            "kashmiri_roman": "Valo veso gatsav vanas, sonth āv...",
            "kashmiri_dev": "वलो वेसो गछ़व वनस, सोन्थ आव...",
            "kashmiri_arabic": "وَلو ویسو گَژھَو وَنَس، سونتھ آو...",
            "kashmiri_sharada": "𑆮𑆬𑆾 𑆮𑆼𑆱𑆾 𑆓𑆗𑆳𑆮 𑆮𑆤𑆱 𑆱𑆾𑆤𑇀𑆡 𑆄𑆮𑇅",
            "translation_en": "Come, dear companions, let us wander into the fragrant forest, for spring has arrived in the valley..."
        }
    },
    {
        "id": "chakri",
        "name": "Chakri",
        "devanagari": "चाक्री",
        "persoarabic": "چاکری",
        "sharada": "𑆖𑆳𑆑𑇀𑆫𑆵",
        "category": "polyphonic_folk_ensemble",
        "description": "The most widely beloved, dynamic traditional folk music of Kashmir. Sung by a group in call-and-response style, backed by traditional instruments.",
        "instruments": ["Harmonium", "Rabab", "Sarangi", "Tumbaknari (goblet drum)", "Not (earthen/copper pitcher)"],
        "poetic_themes": ["Romantic lol-lyrics", "Sufi ghazals", "Folk epics (Gulrez, Akanandun)"]
    },
    {
        "id": "sufiyana_kalam",
        "name": "Sūfiyāna Kalām",
        "devanagari": "सूफ़ीयाना कलाम",
        "persoarabic": "صوفیانَہ کَلام",
        "sharada": "𑆱𑆷𑆦𑆵𑆪𑆳𑆤𑆳 𑆑𑆬𑆳𑆩",
        "category": "classical_modal_music",
        "description": "The aristocratic classical music tradition of Kashmir, closely related to Persian Dastgah and Indian Ragas. Organized around 54 classical Maqams.",
        "instruments": ["Santoor (100-string struck zither)", "Saz-i-Kashmir (bowed spike lute)", "Setar", "Dukra / Tabla"],
        "cultural_significance": "Regarded as sacred spiritual meditation combining Persian Sufi poetry (Hafiz, Rumi, Jami) and Kashmiri mystical verses (Lal Ded, Sheikh-ul-Alam)."
    },
    {
        "id": "ladishah",
        "name": "Lādīshāh",
        "devanagari": "लडिशा",
        "persoarabic": "لٔڈِ شاہ",
        "sharada": "𑆬𑆝𑆴𑆯𑆳𑆲",
        "category": "satirical_musical_ballad",
        "description": "Traditional musical street journalism and satire. A minstrel in a pheran sings humorous and biting social and political commentaries while rhythmically playing the iron rings on an iron rod.",
        "instruments": ["Duhra (iron rod fitted with jingling brass/iron rings)"],
        "themes": ["Social justice", "Price inflation", "Bureaucratic folly", "Historic floods & blizzards"]
    },
    {
        "id": "bhand_pather",
        "name": "Bhānd Pāther",
        "devanagari": "भांड पाथर",
        "persoarabic": "بھانٛڈ پاتھَر",
        "sharada": "𑆧𑇀𑆲𑆳𑆟𑇀𑆝 𑆥𑆳𑆡𑆫",
        "category": "traditional_folk_theatre",
        "description": "Centuries-old Kashmiri open-air folk theatre performed by hereditary actors known as Bhānds in village squares (Pather). Combines farce, social satire, mime, music, and acrobatics.",
        "key_characters": ["Maskhara (the witty clown jester)", "Waza", "Darogha (corrupt official)", "Raza (king)"],
        "instruments": ["Shehnai (Surna)", "Dhol (kettle drum)", "Nagada"]
    },
    {
        "id": "lol_lyric",
        "name": "Lōl-Lyric",
        "devanagari": "लोल",
        "persoarabic": "لول",
        "sharada": "𑆬𑆾𑆬",
        "category": "romantic_lyric_poetry",
        "description": "The immortal secular poetry of love, sorrow, and yearning (Lol = intense love/heart's fire). Pioneer: Queen Habba Khatoon (16th c.) and Arnimal (18th c.).",
        "characteristics": ["Short, melodious stanzas", "Deep longing for the beloved", "Vivid imagery of Kashmiri saffron valleys and rivers"]
    },
    {
        "id": "leela",
        "name": "Līlā",
        "devanagari": "लीला",
        "persoarabic": "لیٖلا",
        "sharada": "𑆬𑆵𑆬𑆳",
        "category": "devotional_hymnody",
        "description": "Kashmiri Hindu devotional songs composed in adoration of Shiva, Krishna, and the Divine Mother. Chanted with cymbals and harmonium in temple gatherings.",
        "celebrated_poets": ["Krishna Joo Razdan", "Parmanand", "Prakash Ram Kurigami"]
    }
]

def get_folklore_genre(genre_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve details for a specific Kashmiri folk musical or theatrical genre."""
    for g in FOLKLORE_GENRES:
        if g["id"] == genre_id.lower() or g["name"].lower() == genre_id.lower():
            return g
    return None

def get_all_folklore_genres() -> List[Dict[str, Any]]:
    """Return all cataloged Kashmiri folklore and music genres."""
    return FOLKLORE_GENRES
