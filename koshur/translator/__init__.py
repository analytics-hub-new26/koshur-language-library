"""
Translator subpackage for Jammu & Kashmir Historical Land Records and Administrative Documents.
Supports decipherment from raw text or uploaded documents (images, PDFs, scanned records).
"""

from koshur.translator.record_translator import (
    translate_record,
    translate_record_file,
    generate_html_certificate,
    generate_cadastral_table_markdown,
    generate_technical_glossary,
    calculate_record_integrity_hash,
    LEGAL_PHRASE_DICTIONARY,
    LEGAL_PHRASE_DICTIONARY_EN,
    LEGAL_PHRASE_DICTIONARY_HI
)

from koshur.translator.entity_extractor import (
    extract_all_entities,
    classify_document,
    extract_land_measurements,
    extract_survey_identifiers,
    extract_administrative_jurisdiction,
    extract_dates_and_calendars,
    extract_financial_consideration,
    extract_parties_and_roles,
    extract_soil_classifications,
    detect_shikasta_formulas
)

from koshur.translator.ocr_engine import (
    extract_document_text,
    preprocess_image,
    extract_text_from_pdf,
    match_archival_sample,
    detect_script
)

from koshur.translator.sample_records import (
    get_sample_record,
    list_sample_records,
    SAMPLE_RECORDS
)

__all__ = [
    # Main translation APIs
    "translate_record",
    "translate_record_file",
    "generate_html_certificate",
    "generate_cadastral_table_markdown",
    "generate_technical_glossary",
    "calculate_record_integrity_hash",
    "LEGAL_PHRASE_DICTIONARY",
    "LEGAL_PHRASE_DICTIONARY_EN",
    "LEGAL_PHRASE_DICTIONARY_HI",

    # Entity extraction & decipherment
    "extract_all_entities",
    "classify_document",
    "extract_land_measurements",
    "extract_survey_identifiers",
    "extract_administrative_jurisdiction",
    "extract_dates_and_calendars",
    "extract_financial_consideration",
    "extract_parties_and_roles",
    "extract_soil_classifications",
    "detect_shikasta_formulas",

    # Document OCR & preprocessing
    "extract_document_text",
    "preprocess_image",
    "extract_text_from_pdf",
    "match_archival_sample",
    "detect_script",

    # Archival Sample Corpus
    "get_sample_record",
    "list_sample_records",
    "SAMPLE_RECORDS"
]
