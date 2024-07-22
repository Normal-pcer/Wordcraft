import math
from util.math import Vec2i


class Vec2f:
    """
    util.math.Vec2f
    Vector with two float components
    """

    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0):
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vec2f({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vec2f") -> "Vec2f":
        return Vec2f(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2f") -> "Vec2f":
        return Vec2f(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vec2f":
        return Vec2f(self.x * other, self.y * other)

    def __floor__(self) -> "Vec2i":
        return Vec2i(math.floor(self.x), math.floor(self.y))

    def __trunc__(self) -> "Vec2i":
        return Vec2i(math.trunc(self.x), math.trunc(self.y))

    def __ceil__(self) -> "Vec2i":
        return Vec2i(math.ceil(self.x), math.ceil(self.y))

    def __round__(self) -> "Vec2i":
        return Vec2i(round(self.x), round(self.y))

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
