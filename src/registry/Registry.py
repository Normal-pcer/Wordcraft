"""
Manage registry tables.
"""

from typing import Dict

from registry import RegistryKey, RegistryTable
from util import Identifier

_REGISTRY_TABLES: Dict[RegistryKey, RegistryTable] = dict()


def register(key: RegistryKey, identifier: Identifier, value: object):
    """
    Register a value in the registry table (by given key).
    """
    table = get_registry_table(key)
    if table is None:
        _REGISTRY_TABLES[key] = table = dict()
    table[identifier] = value


def get_registry_table(key: RegistryKey,
                       default: RegistryTable | None = None) -> RegistryTable | None:
    return _REGISTRY_TABLES.get(key, default)
