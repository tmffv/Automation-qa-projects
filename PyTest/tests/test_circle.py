import pytest
import source.shapes as shape
import math


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shape.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        result = self.circle.area()
        expected = math.pi * self.circle.radius ** 2
        assert result == expected

    def test_perimetr(self):
        result = self.circle.perimetr()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()

