"""
Revenue & Land Records subpackage for Koshur.
Handles historical J&K land records terminology, cadastral registers,
Shikasta deed forms, tenancy classifications, land unit conversions, and cadastral references.
"""

from koshur.revenue.land_records import (
    lookup_revenue_term,
    convert_land_area,
    explain_record_type,
    list_revenue_terms,
    get_terms_by_category,
    list_categories,
    search_revenue_terms,
    REVENUE_TERMS,
    SQ_FEET_PER_MARLA,
    SQ_FEET_PER_KANAL,
    SQ_FEET_PER_GHUMAON,
    SQ_METERS_PER_SQ_FOOT,
)

__all__ = [
    "lookup_revenue_term",
    "convert_land_area",
    "explain_record_type",
    "list_revenue_terms",
    "get_terms_by_category",
    "list_categories",
    "search_revenue_terms",
    "REVENUE_TERMS",
    "SQ_FEET_PER_MARLA",
    "SQ_FEET_PER_KANAL",
    "SQ_FEET_PER_GHUMAON",
    "SQ_METERS_PER_SQ_FOOT",
]
