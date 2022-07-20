class Figure:
    def __init__(self):
        self.name = None

    def area(self):
        pass

    def add_area(self, some_figure):
        print(isinstance(some_figure, Figure))
        if isinstance(some_figure, Figure):
            sum_area = int(self.area()) + int(some_figure.area())
            return sum_area
        else:
            raise ValueError('Передана не геометрическая фигура')


