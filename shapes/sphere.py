import random
import math


class Sphere:
    def __init__(self, _radius=random.randint(1, 100),
                 _density=random.randint(1, 100) + (1 / random.randint(1, 100))):
        self.radius = int(_radius)
        self.density = float(_density)
        self.volume = self.calculateVolume()

    def calculateVolume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def representIntoString(self):
        return f"Sphere with radius {self.radius}, density of {self.density} and volume of {self.volume}"
