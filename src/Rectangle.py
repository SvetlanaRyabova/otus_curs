from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.name = 'Rectangle'

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

