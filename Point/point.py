from dataclasses import dataclass, astuple
from operator import add, sub, mul
from itertools import repeat

@dataclass
class Point(object):
    x: int
    y: int
    z: int
    def __add__(self, other):
        return Point(*map(add, self, other))
    def __sub__(self, other):
        return Point(*map(sub, self, other))
    def __mul__(self, scalar):
        return Point(*map(mul, self, repeat(scalar)))
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    def __iter__(self):
        yield from astuple(self)

if __name__ == "__main__":
    p1 = Point(1, 1, 1)
    p2 = Point(2, 2, 2)
    p1_1 = Point(1, 1, 1)
    print(p1 == p1_1)
    print(p1 == p2)
    print(p1)
    print(p2 * 3)
    x, y, z = Point(1, 2, 3)
    print(x, y, z)