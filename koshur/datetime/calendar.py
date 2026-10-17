"""
Kashmiri Date, Time & Calendar Formatting Engine.
Handles:
1. Kashmiri Days of the Week (Ādathvār to Bhaṭṭivār).
2. Traditional Kashmiri Lunar/Solar Calendar (Chetur to Phāgun; Navreh New Year system).
3. Gregorian Calendar localized into Kashmiri scripts.
4. Human-friendly Relative Time (e.g. 'Vuhein' [Just now], 'Rāth' [Yesterday], 'Pāgah' [Tomorrow]).
5. Kashmiri Times of Day (Subahan, Dopahar, Shāman, Rāthas).
"""

from typing import Dict, Any, Optional, Union
import datetime

# 7 Days of the Week
KASHMIRI_WEEKDAYS: Dict[int, Dict[str, str]] = {
    0: { # Monday
        "devanagari": "च़ांदुरवार",
        "persoarabic": "ژاندُروار",
        "sharada": "𑆖𑆳𑆁𑆢𑆶𑆫𑆮𑆳𑆫",
        "roman": "Tsāndurvār",
        "english": "Monday",
    },
    1: { # Tuesday
        "devanagari": "बोमवार",
        "persoarabic": "بوموار",
        "sharada": "𑆧𑆾𑆩𑆮𑆳𑆫",
        "roman": "Bōmvār",
        "english": "Tuesday",
    },
    2: { # Wednesday
        "devanagari": "बोधवार",
        "persoarabic": "بودھَوار",
        "sharada": "𑆧𑆾𑆣𑆮𑆳𑆫",
        "roman": "Bōdhavār",
        "english": "Wednesday",
    },
    3: { # Thursday
        "devanagari": "ब्रेसवार",
        "persoarabic": "برٛیسوار",
        "sharada": "𑆧𑇀𑆫𑆼𑆱𑆮𑆳𑆫",
        "roman": "Brēsvār",
        "english": "Thursday",
    },
    4: { # Friday
        "devanagari": "शुकरवार / जुमह",
        "persoarabic": "شُکُروار / جُمعہ",
        "sharada": "𑆯𑆶𑆑𑇀𑆫𑆮𑆳𑆫",
        "roman": "Shukurvār / Jummah",
        "english": "Friday",
    },
    5: { # Saturday
        "devanagari": "भटिवार",
        "persoarabic": "بَٹِوار",
        "sharada": "𑆨𑆛𑆴𑆮𑆳𑆫",
        "roman": "Bhaṭṭivār",
        "english": "Saturday",
    },
    6: { # Sunday
        "devanagari": "आदथवार",
        "persoarabic": "آدَتھوار",
        "sharada": "𑆄𑆢𑆡𑆮𑆳𑆫",
        "roman": "Ādathvār",
        "english": "Sunday",
    },
}

# Traditional 12 Kashmiri Calendar Months (starts with Chetur / Navreh in Spring)
KASHMIRI_MONTHS: Dict[int, Dict[str, str]] = {
    1: { # Chaitra
        "devanagari": "चेतुर",
        "persoarabic": "چیتُر",
        "sharada": "𑆖𑆼𑆠𑆶𑆫",
        "roman": "Chetur",
        "approx_gregorian": "March-April (Navreh Spring New Year)",
    },
    2: { # Vaishakha
        "devanagari": "वह्यक",
        "persoarabic": "وَہیَک",
        "sharada": "𑆮𑆲𑇀𑆪𑆑",
        "roman": "Vahyak",
        "approx_gregorian": "April-May",
    },
    3: { # Jyeshtha
        "devanagari": "ज़ेठ",
        "persoarabic": "زیٹھ",
        "sharada": "𑆘𑆼𑆜",
        "roman": "Zēṭh",
        "approx_gregorian": "May-June",
    },
    4: { # Ashadha
        "devanagari": "हार",
        "persoarabic": "ہار",
        "sharada": "𑆲𑆳𑆫",
        "roman": "Hār",
        "approx_gregorian": "June-July",
    },
    5: { # Shravana
        "devanagari": "श्रावुन",
        "persoarabic": "شراوُن",
        "sharada": "𑆯𑇀𑆫𑆳𑆮𑆶𑆤",
        "roman": "Shrāvun",
        "approx_gregorian": "July-August",
    },
    6: { # Bhadrapada
        "devanagari": "भादुर",
        "persoarabic": "بادُر",
        "sharada": "𑆨𑆳𑆢𑆶𑆫",
        "roman": "Bhādur",
        "approx_gregorian": "August-September",
    },
    7: { # Ashvina
        "devanagari": "आशिद",
        "persoarabic": "آشِد",
        "sharada": "𑆄𑆯𑆴𑆢",
        "roman": "Āshid",
        "approx_gregorian": "September-October",
    },
    8: { # Kartika
        "devanagari": "कार्तिक",
        "persoarabic": "کارتِک",
        "sharada": "𑆑𑆳𑆫𑇀𑆠𑆴𑆑",
        "roman": "Kārtik",
        "approx_gregorian": "October-November",
    },
    9: { # Margashirsha
        "devanagari": "मघर",
        "persoarabic": "مَگھَر",
        "sharada": "𑆩𑆔𑆫",
        "roman": "Maghar",
        "approx_gregorian": "November-December",
    },
    10: { # Pausha
        "devanagari": "पोह",
        "persoarabic": "پوہ",
        "sharada": "𑆥𑆾𑆲",
        "roman": "Pōh",
        "approx_gregorian": "December-January",
    },
    11: { # Magha
        "devanagari": "माघ",
        "persoarabic": "ماگھ",
        "sharada": "𑆩𑆳𑆔",
        "roman": "Māgh",
        "approx_gregorian": "January-February",
    },
    12: { # Phalguna
        "devanagari": "फागुन",
        "persoarabic": "فاگُن",
        "sharada": "𑆦𑆳𑆓𑆶𑆤",
        "roman": "Phāgun",
        "approx_gregorian": "February-March",
    },
}

# Gregorian Months Transliterated
GREGORIAN_MONTHS_KASHMIRI: Dict[int, Dict[str, str]] = {
    1: {"devanagari": "जनवरी", "persoarabic": "جَنوری", "sharada": "𑆘𑆤𑆮𑆫𑆵", "roman": "Janvarī", "english": "January"},
    2: {"devanagari": "फ़रवरी", "persoarabic": "فَروری", "sharada": "𑆦𑆫𑆮𑆫𑆵", "roman": "Farvarī", "english": "February"},
    3: {"devanagari": "मार्च", "persoarabic": "مارچ", "sharada": "𑆩𑆳𑆫𑇀𑆖", "roman": "Mārtsh", "english": "March"},
    4: {"devanagari": "अप्रैल", "persoarabic": "اَپریل", "sharada": "𑆃𑆥𑇀𑆫𑆽𑆬", "roman": "Aprēl", "english": "April"},
    5: {"devanagari": "मई", "persoarabic": "مئی", "sharada": "𑆩𑆆", "roman": "Mayī", "english": "May"},
    6: {"devanagari": "जून", "persoarabic": "جوٗن", "sharada": "𑆘𑆷𑆤", "roman": "Jūn", "english": "June"},
    7: {"devanagari": "जुलाई", "persoarabic": "جُلائی", "sharada": "𑆘𑆶𑆬𑆳𑆅", "roman": "Julāyī", "english": "July"},
    8: {"devanagari": "अगस्त", "persoarabic": "اَگَست", "sharada": "𑆃𑆓𑆱𑇀𑆠", "roman": "Agast", "english": "August"},
    9: {"devanagari": "सितंबर", "persoarabic": "سِتَمبَر", "sharada": "𑆱𑆴𑆠𑆩𑇀𑆧𑆫", "roman": "Sitambar", "english": "September"},
    10: {"devanagari": "अक्टूबर", "persoarabic": "اَکتوٗبَر", "sharada": "𑆃𑆑𑇀𑆛𑆷𑆧𑆫", "roman": "Aktūbar", "english": "October"},
    11: {"devanagari": "नवंबर", "persoarabic": "نَوَمبَر", "sharada": "𑆤𑆮𑆩𑇀𑆧𑆫", "roman": "Navambar", "english": "November"},
    12: {"devanagari": "दिसंबर", "persoarabic": "دِسَمبَر", "sharada": "𑆢𑆴𑆱𑆩𑇀𑆧𑆫", "roman": "Disambar", "english": "December"},
}

def get_weekday_name(weekday_idx: int, script: str = "devanagari") -> str:
    """
    Returns weekday name for index (0 = Monday, 6 = Sunday, matching datetime.weekday()).
    """
    idx = weekday_idx % 7
    s = script.lower().strip()
    entry = KASHMIRI_WEEKDAYS[idx]
    if s in ["persoarabic", "arab", "arabic", "nastaliq"]:
        return entry["persoarabic"]
    elif s in ["sharada", "sharda", "shrd"]:
        return entry["sharada"]
    elif s in ["roman", "latin"]:
        return entry["roman"]
    elif s in ["english", "en"]:
        return entry["english"]
    return entry["devanagari"]

def get_month_name(month_idx: int, script: str = "devanagari", traditional: bool = False) -> str:
    """
    Returns month name (1 = January / Chetur, 12 = December / Phāgun).
    traditional: True uses the Kashmiri solar/lunar calendar, False uses Gregorian.
    """
    m = max(1, min(12, month_idx))
    table = KASHMIRI_MONTHS if traditional else GREGORIAN_MONTHS_KASHMIRI
    entry = table[m]
    s = script.lower().strip()
    if s in ["persoarabic", "arab", "arabic", "nastaliq"]:
        return entry["persoarabic"]
    elif s in ["sharada", "sharda", "shrd"]:
        return entry["sharada"]
    elif s in ["roman", "latin"]:
        return entry["roman"]
    return entry["devanagari"]

def format_date(
    dt: Optional[Union[datetime.date, datetime.datetime]] = None,
    script: str = "devanagari",
    include_weekday: bool = True,
    traditional: bool = False
) -> str:
    """
    Format a Python date or datetime object in the Kashmiri language.
    Example:
        format_date(datetime.date(2026, 10, 8), script='devanagari')
        -> 'ब्रेसवार, ८ अक्टूबर २०२६'
    """
    if dt is None:
        dt = datetime.datetime.now()

    day_num = dt.day
    year_num = dt.year
    month_name = get_month_name(dt.month, script=script, traditional=traditional)
    weekday_name = get_weekday_name(dt.weekday(), script=script) if include_weekday else ""

    # Native script numerals
    s = script.lower().strip()
    if s in ["persoarabic", "arab", "arabic", "nastaliq"]:
        # Arabic-Indic digits
        digit_map = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
        d_str = str(day_num).translate(digit_map)
        y_str = str(year_num).translate(digit_map)
        if include_weekday:
            return f"{weekday_name}، {d_str} {month_name} {y_str}"
        return f"{d_str} {month_name} {y_str}"
    elif s in ["sharada", "sharda", "shrd"]:
        sharada_digits = ["𑇐", "𑇑", "𑇒", "𑇓", "𑇔", "𑇕", "𑇖", "𑇗", "𑇘", "𑇙"]
        d_str = "".join(sharada_digits[int(c)] for c in str(day_num))
        y_str = "".join(sharada_digits[int(c)] for c in str(year_num))
        if include_weekday:
            return f"{weekday_name}, {d_str} {month_name} {y_str}"
        return f"{d_str} {month_name} {y_str}"
    elif s in ["devanagari", "deva"]:
        deva_digits = str.maketrans("0123456789", "०१२३४५६७८९")
        d_str = str(day_num).translate(deva_digits)
        y_str = str(year_num).translate(deva_digits)
        if include_weekday:
            return f"{weekday_name}, {d_str} {month_name} {y_str}"
        return f"{d_str} {month_name} {y_str}"
    else: # Roman
        if include_weekday:
            return f"{weekday_name}, {day_num} {month_name} {year_num}"
        return f"{day_num} {month_name} {year_num}"

def format_relative_time(
    delta_seconds_or_dt: Union[int, float, datetime.datetime, datetime.timedelta],
    script: str = "devanagari"
) -> str:
    """
    Format human-friendly relative time (e.g. 'Just now', 'Yesterday', '3 hours ago').
    Supports integer seconds or datetime objects.
    """
    if isinstance(delta_seconds_or_dt, datetime.datetime):
        seconds = (datetime.datetime.now() - delta_seconds_or_dt).total_seconds()
    elif isinstance(delta_seconds_or_dt, datetime.timedelta):
        seconds = delta_seconds_or_dt.total_seconds()
    else:
        seconds = float(delta_seconds_or_dt)

    abs_sec = abs(seconds)
    is_past = seconds >= 0

    s = script.lower().strip()
    is_arab = s in ["persoarabic", "arab", "arabic", "nastaliq"]
    is_shrd = s in ["sharada", "sharda", "shrd"]
    is_roman = s in ["roman", "latin"]

    if abs_sec < 60:
        if is_arab: return "وُہؠن (اَز کَل)"
        if is_shrd: return "𑆮𑆶𑆲𑆽𑆤"
        if is_roman: return "Vuhein (Just now)"
        return "वुहैन (अभी)"

    minutes = int(abs_sec // 60)
    if minutes < 60:
        if is_past:
            if is_arab: return f"{minutes} مِنَٹ برٛونٛہہ"
            if is_shrd: return f"{minutes} 𑆩𑆴𑆤𑆛 𑆧𑇀𑆫𑆶𑆁𑆲"
            if is_roman: return f"{minutes} minut bronh"
            return f"{minutes} मिनट ब्रुंह"
        else:
            if is_arab: return f"{minutes} مِنَٹ پَتہٕ"
            if is_shrd: return f"{minutes} 𑆩𑆴𑆤𑆛 𑆥𑆠"
            if is_roman: return f"{minutes} minut patah"
            return f"{minutes} मिनट पतॳ"

    hours = int(abs_sec // 3600)
    if hours < 24:
        if is_past:
            if is_arab: return f"{hours} گَنٹہٕ برٛونٛہہ"
            if is_shrd: return f"{hours} 𑆓𑆟𑇀𑆛 𑆧𑇀𑆫𑆶𑆁𑆲"
            if is_roman: return f"{hours} ganta bronh"
            return f"{hours} गंटॳ ब्रुंह"
        else:
            if is_arab: return f"{hours} گَنٹہٕ پَتہٕ"
            if is_shrd: return f"{hours} 𑆓𑆟𑇀𑆛 𑆥𑆠"
            if is_roman: return f"{hours} ganta patah"
            return f"{hours} गंटॳ पतॳ"

    days = int(abs_sec // 86400)
    if days == 1:
        if is_past:
            if is_arab: return "راتھ (Yesterday)"
            if is_shrd: return "𑆫𑆳𑆡"
            if is_roman: return "Rāth (Yesterday)"
            return "राथ (कल)"
        else:
            if is_arab: return "پاگَہ (Tomorrow)"
            if is_shrd: return "𑆥𑆳𑆓𑆲"
            if is_roman: return "Pāgah (Tomorrow)"
            return "पागह (कल)"
    elif days == 2:
        if is_past:
            if is_arab: return "اوترُم (Day before yesterday)"
            if is_shrd: return "𑆏𑆠𑇀𑆫𑆶𑆩"
            if is_roman: return "Otrum (Day before yesterday)"
            return "ओत्रुम (परसों)"
        else:
            if is_arab: return "کالَم (Day after tomorrow)"
            if is_shrd: return "𑆑𑆳𑆬𑆩"
            if is_roman: return "Kālam (Day after tomorrow)"
            return "कालम (परसों)"

    if is_past:
        if is_arab: return f"{days} دۄہ برٛونٛہہ"
        if is_shrd: return f"{days} 𑆢𑆾𑆲 𑆧𑇀𑆫𑆶𑆁𑆲"
        if is_roman: return f"{days} dohi bronh"
        return f"{days} दोह ब्रुंह"
    else:
        if is_arab: return f"{days} دۄہ پَتہٕ"
        if is_shrd: return f"{days} 𑆢𑆾𑆲 𑆥𑆠"
        if is_roman: return f"{days} dohi patah"
        return f"{days} दोह पतॳ"

def get_time_of_day(hour: Optional[int] = None, script: str = "devanagari") -> str:
    """
    Returns time-of-day period in Kashmiri:
    - 05:00 - 11:59 : Subahan (Morning / सुबहन् / صُبحَن)
    - 12:00 - 16:59 : Dopahar (Afternoon / दुपहर / دُپَہَر)
    - 17:00 - 20:59 : Shāman (Evening / शामन् / شامَن)
    - 21:00 - 04:59 : Rāthas (Night / राथस् / راتَس)
    """
    if hour is None:
        hour = datetime.datetime.now().hour

    s = script.lower().strip()
    is_arab = s in ["persoarabic", "arab", "arabic", "nastaliq"]
    is_shrd = s in ["sharada", "sharda", "shrd"]
    is_roman = s in ["roman", "latin"]

    if 5 <= hour < 12:
        if is_arab: return "صُبحَن"
        if is_shrd: return "𑆱𑆶𑆧𑆲𑆤"
        if is_roman: return "Subahan"
        return "सुबहन"
    elif 12 <= hour < 17:
        if is_arab: return "دُپَہَر"
        if is_shrd: return "𑆢𑆶𑆥𑆲𑆫"
        if is_roman: return "Dopahar"
        return "दुपहर"
    elif 17 <= hour < 21:
        if is_arab: return "شامَن"
        if is_shrd: return "𑆯𑆳𑆩𑆤"
        if is_roman: return "Shāman"
        return "शामन"
    else:
        if is_arab: return "راتَس"
        if is_shrd: return "𑆫𑆳𑆡𑆱"
        if is_roman: return "Rāthas"
        return "राथस"
