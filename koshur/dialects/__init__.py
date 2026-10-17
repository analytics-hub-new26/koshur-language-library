"""
Dialects subpackage for Koshur.
Preserves regional Kashmiri dialects: Kishtwari, Poguli, Siraji, and Rambani.
"""

from koshur.dialects.kishtwari import get_kishtwari_info, KISHTWARI_INFO
from koshur.dialects.poguli import get_poguli_info, POGULI_INFO
from koshur.dialects.siraji import get_siraji_info, get_rambani_info, SIRAJI_INFO, RAMBANI_INFO
from koshur.dialects.comparator import compare_dialects, get_dialect_info, DIALECT_REGISTRY

__all__ = [
    "get_kishtwari_info",
    "KISHTWARI_INFO",
    "get_poguli_info",
    "POGULI_INFO",
    "get_siraji_info",
    "get_rambani_info",
    "SIRAJI_INFO",
    "RAMBANI_INFO",
    "compare_dialects",
    "get_dialect_info",
    "DIALECT_REGISTRY",
]
