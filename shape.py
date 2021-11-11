from shapes.paral import Paral
from shapes.tetra import Tetra
from shapes.sphere import Sphere
import random


class Shape:
    def __init__(self, _randomShape=True, _shapeType=0, _sides=[0, 0, 0], _dens=0.0):
        if _randomShape:
            self.type = random.randint(1, 3)
            if self.type == 1:
                # generate sphere
                self.content = Sphere(random.randint(1, 100),
                                      random.randint(1, 100) + (1 / random.randint(1, 100)))
            elif self.type == 2:
                # generate paral
                self.content = Paral(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
                                     random.randint(1, 100) + (1 / random.randint(1, 100)))
            else:
                self.content = Tetra(random.randint(1, 100), random.randint(1, 100) + (1 / random.randint(1, 100)))
        else:
            self.type = int(_shapeType)
            if self.type == 1:
                # generate sphere
                self.content = Sphere(_sides[0], _dens)
            elif self.type == 2:
                # generate paral
                self.content = Paral(_sides[0], _sides[1], _sides[2], _dens)
            else:
                self.content = Tetra(_sides[0], _dens)
