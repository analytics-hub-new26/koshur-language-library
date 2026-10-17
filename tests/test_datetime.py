"""
Unit tests for koshur.datetime calendar and date formatting.
"""

import pytest
import datetime
import koshur
from koshur.datetime import (
    format_date,
    format_relative_time,
    get_weekday_name,
    get_month_name,
    get_time_of_day,
    KASHMIRI_WEEKDAYS,
    KASHMIRI_MONTHS
)

def test_weekdays():
    # 0 = Monday, 6 = Sunday
    assert get_weekday_name(0, script="devanagari") == "च़ांदुरवार"
    assert get_weekday_name(6, script="devanagari") == "आदथवार"
    assert get_weekday_name(6, script="roman") == "Ādathvār"
    assert "آدَتھوار" in get_weekday_name(6, script="persoarabic")

def test_months():
    # 1 = January / Chetur
    assert get_month_name(1, script="devanagari") == "जनवरी"
    assert get_month_name(1, script="devanagari", traditional=True) == "चेतुर"
    assert get_month_name(1, script="roman", traditional=True) == "Chetur"
    assert "چیتُر" in get_month_name(1, script="persoarabic", traditional=True)

def test_format_date():
    dt = datetime.date(2026, 10, 8)
    # 2026-10-08 is Thursday (index 3: Brēsvār / ब्रेसवार)
    res_deva = format_date(dt, script="devanagari")
    assert "ब्रेसवार" in res_deva
    assert "अक्टूबर" in res_deva
    assert "२०२६" in res_deva

    res_arab = format_date(dt, script="persoarabic")
    assert "برٛیسوار" in res_arab

def test_format_relative_time():
    # Just now
    assert "वुहैन" in format_relative_time(20, script="devanagari")
    assert "وُہؠن" in format_relative_time(20, script="persoarabic")

    # Yesterday
    assert "राथ" in format_relative_time(86400, script="devanagari")
    assert "راتھ" in format_relative_time(86400, script="persoarabic")

    # Tomorrow
    assert "पागह" in format_relative_time(-86400, script="devanagari")
    assert "پاگَہ" in format_relative_time(-86400, script="persoarabic")

def test_get_time_of_day():
    assert get_time_of_day(8, script="devanagari") == "सुबहन"
    assert get_time_of_day(14, script="devanagari") == "दुपहर"
    assert get_time_of_day(19, script="devanagari") == "शामन"
    assert get_time_of_day(23, script="devanagari") == "राथस"
