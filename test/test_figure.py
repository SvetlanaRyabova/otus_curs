from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


def test_circle():
    c = Circle(4)
    assert isinstance(c, Figure)
    assert int(c.area()) == 50
    assert int(c.perimeter()) == 25


def test_triangle():
    r = Triangle(2, 3, 4)
    assert isinstance(r, Figure)
    assert int(r.area()) == 2
    assert int(r.perimeter()) == 9


def test_rectangle():
    r = Rectangle(2, 5)
    assert isinstance(r, Figure)
    assert int(r.area()) == 10
    assert int(r.perimeter()) == 14


def test_square():
    s = Square(6)
    assert isinstance(s, Figure)
    assert int(s.area()) == 36
    assert int(s.perimeter()) == 24


def test_add_area():
    r = Triangle(2, 3, 4)
    s = Square(6)
    assert int(r.add_area(s)) == 38


def test_add_area_not_figure():
    r = Triangle(2, 3, 4)
    s = ''
    with pytest.raises(ValueError):
        int(r.add_area(s)).add(task='Передана не геометрическая фигура')
