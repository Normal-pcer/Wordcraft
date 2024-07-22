import json
from abc import ABC
from typing import Union, Type

from util.codec import Codec, Serializer


def _rollback_empty(type: Type) -> object:
    return object.__new__(type)


def _default_empty(type: Type) -> object:
    try:
        return type()
    except TypeError:
        return _rollback_empty(type)


def _default_serialize(obj: any) -> dict:
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return dict()


class JsonSaveAttributes(Serializer, Codec, ABC):
    sourceType: Type

    def __init__(self, source_type: Type = object):
        self.sourceType = source_type

    def serialize(self, source: any) -> str:
        return json.dumps(source, default=_default_serialize)

    def deserialize(self, source: str, force_type=True, default: callable = _default_empty) -> any:
        """Deserialize a json string to a python object (based on type self.sourceType).

        :param source: Json string to deserialize.
        :type source: str
        :param force_type: Whether to force the deserialized object to be of type self.sourceType, 
            defaults to True. It will NOT always output target type if this param is set to False.
        :type force_type: bool, optional
        :param default: Will output when source type is not desired, defaults to lambdatype:type.__init__()
        :type default: callable, optional
        :return: Deserialized object.
        :rtype: any
        """
        target: Union[int, float, str, list, dict] = json.loads(source)
        return self._deserialize_loop(target, force_type, default)

    def _deserialize_loop(self, target: any, force_type=True,
                          default: callable = _default_empty) -> any:
        if isinstance(target, self.sourceType):
            return target
        else:
            if isinstance(target, dict):
                empty_target_object: object = default(self.sourceType)
                # Try to convert
                for key in target:
                    value = target[key]
                    if empty_target_object.__annotations__.get(key) is not None:
                        # Defined
                        value_type: Type = empty_target_object.__annotations__.get(key)
                        if isinstance(value, value_type):
                            setattr(empty_target_object, key, value)
                        elif isinstance(value, dict):
                            # Deserialize recursively
                            new_codec = JsonSaveAttributes(value_type)
                            setattr(empty_target_object, key,
                                    new_codec._deserialize_loop(value, force_type, default))
                        else:
                            # Not able to convert
                            setattr(empty_target_object, key,
                                    default(value_type) if force_type else value)
                return empty_target_object

            else:
                # Not able to convert
                return default(self.sourceType) if force_type else target
