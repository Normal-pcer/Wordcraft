from abc import ABC
from util.codec import Serializer

class Repr(Serializer, ABC):
    @staticmethod
    def serialize(source: any) -> str:
        return repr(source)