import math

from util.math import Vec2f


class Vec2i:
    """
    util.math.Vec2i
    Vector with two int components
    """

    x: int
    y: int

    def __init__(self, x: int = 0, y: int = 0):
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vec2i({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vec2i") -> "Vec2i":
        return Vec2i(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2i") -> "Vec2i":
        return Vec2i(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> "Vec2i":
        return Vec2i(self.x * other, self.y * other)

    def to_vec2f(self) -> "Vec2f":
        return Vec2f(self.x, self.y)

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
