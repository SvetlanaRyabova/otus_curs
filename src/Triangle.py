from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, a,b,c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'
        self.is_possible()

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def is_possible(self) -> object:
        if self.a + self.b > self.c:
            if self.b + self.c > self.a:
                if self.a + self.c > self.b:
                    return self
                else:
                    raise ValueError('введите другие значения сторон')