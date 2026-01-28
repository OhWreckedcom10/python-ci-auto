import pytest
from services.calculator_service import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply1():
    assert multiply(10, 3) == 30


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_correct():
    assert add(5, 4) == 9


def test_failed_fix():
    assert multiply(4, 6) == 24


def test_failed_for_example():
    assert add(10, 15) == 25
