import random
import math


class Paral:
    def __init__(self, _a=random.randint(1, 100), _b=random.randint(1, 100), _c=random.randint(1, 100),
                 _density=random.randint(1, 100) + (1 / random.randint(1, 100))):
        self.a = int(_a)
        self.b = int(_b)
        self.c = int(_c)
        self.density = float(_density)
        self.volume = self.calculateVolume()

    def calculateVolume(self):
        return self.a * self.b * self.c

    def representIntoString(self):
        return f"Perpendicular parallelepiped with sides {self.a}, {self.b} and {self.c},\n" \
               f" density of {self.density} and volume of {self.volume}"
