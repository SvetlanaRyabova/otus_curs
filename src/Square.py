from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.name = 'Square'

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return 4 * self.a
