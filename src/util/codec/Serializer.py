from abc import ABCMeta, abstractmethod
from typing import TypeVar

class Serializer(metaclass=ABCMeta):
    """
    wordcraft.util.codec.Serializer
    A class that can ONLY serialize objects to a another (usually string)
    """

    T = TypeVar('T')
    
    def __init__(self, serialize: callable) -> None:
        self.serialize = serialize
    
    @abstractmethod
    def serialize(self, source) -> T:
        pass