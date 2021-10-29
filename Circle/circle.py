import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"{__class__.__name__}({self.radius!r})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    c1 = Circle()
    print(c1.radius)
    print(c1.diameter)
    print(c1.area)
    c1.radius = 5
    print(c1)
