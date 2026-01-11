import pytest


def test_are(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_perimetr(my_rectangle):
    assert my_rectangle.perimetr() == (10 * 2) + (20 * 2)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
