from abc import ABC
from util.codec import Serializer

class Str(Serializer, ABC):
    @staticmethod
    def serialize(source: any) -> str:
        return str(source)