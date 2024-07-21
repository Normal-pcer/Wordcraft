from abc import ABCMeta, abstractmethod


class Codec(metaclass=ABCMeta):
    """
    wordcraft.util.codec.Codec

    A class that serializes / deserializes an object to another.
    """

    @abstractmethod
    def serialize(self, source: any) -> any:
        pass

    @abstractmethod
    def deserialize(self, source: any) -> any:
        pass
