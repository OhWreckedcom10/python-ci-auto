import pytest
from data_validator import is_positive, is_in_range, is_integer


def test_is_positive_true():
    assert is_positive(1) is True


def test_is_positive_false_zero():
    assert is_positive(0) is False


def test_is_positive_false_negative():
    assert is_positive(-5) is False


def test_is_in_range_true_edges():
    assert is_in_range(0, 0, 10) is True
    assert is_in_range(10, 0, 10) is True


def test_is_in_range_false_below():
    assert is_in_range(-1, 0, 10) is False


def test_is_in_range_false_above():
    assert is_in_range(11, 0, 10) is False


def test_is_integer_true_int():
    assert is_integer(7) is True


def test_is_integer_true_float_integer_value():
    assert is_integer(7.0) is True


def test_is_integer_false_float_non_integer():
    assert is_integer(7.2) is False


def test_is_integer_false_string():
    assert is_integer("7") is False


def test_is_integer_false_bool_edge():
    assert is_integer(True) is False


def test_expected_failure_demo():
    # "בדיקה אחת שמוודאת כישלון צפוי" באמצעות xfail
    pytest.xfail("דוגמה לכישלון צפוי כחלק מהדרישה")
    assert is_positive(-1) is True
