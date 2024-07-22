from typing import Type


class RegistryKey:
    """
    wordcraft.registry.RegistryKey
    """

    dataType: Type
    name: str

    def __init__(self, data_type: Type, name: str):
        self.dataType = data_type
        self.name = name

    def __eq__(self, other: "RegistryKey") -> bool:
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

