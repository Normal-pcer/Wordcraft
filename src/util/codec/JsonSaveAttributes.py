import json
from abc import ABC
from typing import Tuple, Union, Type
from copy import deepcopy

from util.codec import Codec, Serializer

NAME_TO_EMPTY = {
    'Callable': lambda: None
}


def _rollback_empty(type: Type) -> object:
    try:
        return type.__new__(type)
    except TypeError:
        try:
            return type.__origin__.__new__(type.__origin__)
        except TypeError:
            try:
                name = type._name
                return deepcopy(NAME_TO_EMPTY[name])
            except ValueError:
                return object.__new__(object)  # 回天乏术


def _default_empty(type: Type) -> object:
    try:
        return type()
    except TypeError:
        return _rollback_empty(type)


def _default_serialize(obj: any) -> dict:
    # Check if method obj.to_dict() is available
    if hasattr(obj, 'to_dict') and callable(obj.to_dict):
        return obj.to_dict()
    elif hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return dict()


def _safe_instance(obj: any, type: Type) -> bool:
    try:
        return isinstance(obj, type)
    except TypeError:
        return False


def _initialize_if_available(obj: any) -> None:
    if (hasattr(obj, 'after_deserialization') and
            callable(getattr(obj, 'after_deserialization'))):
        obj.after_deserialization()


class JsonSaveAttributes(Serializer, Codec, ABC):
    """
    A class to serialize and deserialize objects to and from json.

    It will convert objects to a dict first, by calling to_dict() method if available, otherwise it 
    will use __dict__, or using an empty dict if nothing available.

    after_deserialization() method will be called automatically after deserialization.
    """
    sourceType: Type
    ignoreCallable: bool = True

    def __init__(self, source_type: Type = object, ignore_callable=True):
        self.sourceType = source_type
        self.ignoreCallable = ignore_callable

    def serialize(self, source: any) -> str:
        return json.dumps(source, default=_default_serialize)

    def deserialize(self, source: str, force_type=True, default: callable = _default_empty) -> any:
        """Deserialize a json string to a python object (based on type self.sourceType).

        :param source: Json string to deserialize.
        :type source: str
        :param force_type: Whether to force the deserialized object to be of type self.sourceType, 
            defaults to True. It will NOT always output target type if this param is set to False.
        :param default: Will output when source type is not desired, defaults to lambdatype:type.__init__()
        :return: Deserialized object.
        :rtype: any
        """
        target: Union[int, float, str, list, dict] = json.loads(source)
        return self._deserialize_loop(target, force_type, default)

    def _deserialize_loop(self, target: any, force_type=True,
                          default: callable = _default_empty) -> any:
        if _safe_instance(target, self.sourceType):
            return target
        else:
            if isinstance(target, dict):
                empty_target_object: object = default(self.sourceType)
                # Try to convert
                for key in target:
                    key: str
                    value = target[key]
                    if empty_target_object.__annotations__.get(key) is not None:
                        # Defined
                        value_type: Type = empty_target_object.__annotations__.get(key)
                        if _safe_instance(value, value_type):
                            setattr(empty_target_object, key, value)
                        elif isinstance(value, list):
                            # Deserialize recursively
                            try:
                                setattr(empty_target_object, key, list())
                                lis = getattr(empty_target_object, key)

                                # Deserialize each element
                                for index in range(len(value)):
                                    i = value[index]
                                    args_len = len(value_type.__args__)
                                    arg: Type = value_type.__args__[0 if args_len <= i else i]

                                    new_codec = JsonSaveAttributes(arg)

                                    lis.append(new_codec._deserialize_loop(i, force_type, default))
                                    _initialize_if_available(lis[-1])

                                # Check if value_type is typing.Tuple
                                if isinstance(value_type, tuple) or (hasattr(value_type, '__origin__') and
                                                                     isinstance(value_type.__origin__, tuple)):
                                    # Convert to tuple
                                    setattr(empty_target_object, key, tuple(lis))
                            except AttributeError:
                                # Not able to convert
                                setattr(empty_target_object, key,
                                        default(value_type) if force_type else value)
                        elif (isinstance(value, dict) and value_type.__origin__ == dict):
                            try:
                                args: Type = value_type.__args__[1]
                                new_codec = JsonSaveAttributes(args)
                                setattr(empty_target_object, key, dict())
                                dic = getattr(empty_target_object, key)

                                # Deserialize each element
                                for i in value:
                                    dic[i] = new_codec._deserialize_loop(value[i], force_type, default)
                                    _initialize_if_available(dic[i])
                            except AttributeError:
                                # Not able to convert
                                setattr(empty_target_object, key,
                                        default(value_type) if force_type else value)
                        elif isinstance(value, dict) and not (self.ignoreCallable and callable(value_type)):
                            # Deserialize recursively
                            new_codec = JsonSaveAttributes(value_type)
                            setattr(empty_target_object, key,
                                    new_codec._deserialize_loop(value, force_type, default))
                            # Initialize if able via calling after_deserialization
                            _initialize_if_available(empty_target_object)
                        else:
                            # Not able to convert
                            setattr(empty_target_object, key,
                                    default(value_type) if force_type else value)
                return empty_target_object
            elif (isinstance(target, list) and self.sourceType.__origin__ == list):
                empty_target_object: list = list()
                # Try to convert
                for element in target:
                    try:
                        element_type: Type = self.sourceType.__args__[0]
                        new_codec = JsonSaveAttributes(element_type)
                        empty_target_object.append(new_codec._deserialize_loop(element, force_type, default))
                        _initialize_if_available(empty_target_object[-1])
                    except AttributeError:
                        empty_target_object.append(default(self.sourceType) if force_type else target)
                return empty_target_object
            else:
                # Not able to convert
                return default(self.sourceType) if force_type else target
