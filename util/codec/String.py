from abc import ABC

from util.codec import Codec


class String(Codec, ABC):
    def serialize(self, source: str) -> str:
        return source

    def deserialize(self, source: str) -> str:
        return source
