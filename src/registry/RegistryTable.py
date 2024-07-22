from typing import Dict, TypeVar

from util import Identifier


class RegistryTable:
    T = TypeVar('T')
    data: Dict[Identifier, T]

    def get(self, identifier: Identifier, default: T | None = None) -> T | None:
        return self.data.get(identifier, default)

    def set(self, identifier: Identifier, value: T) -> None:
        self.data[identifier] = value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)
