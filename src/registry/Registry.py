"""
Manage registry tables.
"""

from typing import Dict

from registry import RegistryKey, RegistryTable
from util import Identifier

_REGISTRY_TABLES: Dict[RegistryKey, RegistryTable]


def register(key: RegistryKey, identifier: Identifier, value: object) -> bool:
    """
    Register a value in the registry table (by given key).
    Return True if successful, False otherwise.
    """
    table = get_registry_table(key)
    if table is None:
        return False
    table[identifier] = value
    return True


def get_registry_table(key: RegistryKey,
                       default: RegistryTable | None = None) -> RegistryTable | None:
    return _REGISTRY_TABLES.get(key, default)
