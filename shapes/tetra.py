import random
import math


class Tetra:
    def __init__(self, _a=random.randint(1, 100),
                 _density=random.randint(1, 100) + (1 / random.randint(1, 100))):
        self.a = int(_a)
        self.density = float(_density)
        self.volume = self.calculateVolume()

    def calculateVolume(self):
        return (self.a ** 3) * (math.sqrt(2) / 12)

    def representIntoString(self):
        return f"Regular tetrahedron with side {self.a}, density of {self.density} and volume of {self.volume}"
