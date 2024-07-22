from typing import TypeVar, Dict, List, Generic
T = TypeVar('T')
V = TypeVar('V')


class SerializableDict(Generic[T, V]):
    _data: Dict[T, V]
    _initialized: bool = False

    _keys: List[T]
    _values: List[V]

    def init(self):
        # convert _keys & _values to _data: {key: value}
        self._data = dict(zip(self._keys, self._values))
        self._initialized = True

    def __init__(self, data: Dict[T, V] | None = None) -> None:
        if data is not None:
            self._data = data
            self._initialized = True
            self._keys: List[T] = []
            self._values: List[V] = []
        else:
            self._data: Dict[T, V] = dict()
            self._keys: List[T] = []
            self._values: List[V] = []

    def __getitem__(self, key: T) -> V:
        if not self._initialized:
            self.init()
        return self._data.get(key)

    def __setitem__(self, key: T, value: V) -> None:
        self._data[key] = value

    def to_dict(self) -> Dict:
        if not self._initialized:
            self.init()
        self._keys = list(self._data.keys())
        self._values = list(self._data.values())
        return dict(_keys=self._keys, _values=self._values)
