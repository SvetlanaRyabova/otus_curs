from src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self.r = r
        self.name = 'Circle'

    def area(self):
        return pi * (self.r ** 2)

    def perimeter(self):
        return 2 * self.r * pi




