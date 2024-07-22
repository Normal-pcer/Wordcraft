from abc import ABCMeta, abstractmethod
from util.codec import Serializer
from typing import TypeVar


class Codec(metaclass=ABCMeta):
    """
    wordcraft.util.codec.Codec

    A class that serializes / deserializes an object to another.
    """

    T = TypeVar('T')
    
    @abstractmethod
    def serialize(self, source: any) -> T:
        pass

    @abstractmethod
    def deserialize(self, source: T) -> any:
        pass

    def to_serializer(self) -> Serializer:
        return Serializer(self.serialize)