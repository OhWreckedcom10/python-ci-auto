import pytest
from src.processor import normalize_numbers, filter_outliers, calculate_statistics


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([0, 10], [0.0, 1.0]),
        ([5, 15, 25], [0.0, 0.5, 1.0]),
        ([-5, 0, 5], [0.0, 0.5, 1.0]),
    ],
)
def test_normalize_numbers_basic(numbers, expected):
    result = normalize_numbers(numbers)
    assert result == expected


def test_normalize_numbers_empty_raises():
    with pytest.raises(ValueError):
        normalize_numbers([])


def test_normalize_numbers_all_equal():
    assert normalize_numbers([3, 3, 3]) == [0.0, 0.0, 0.0]


@pytest.mark.parametrize(
    "numbers,minv,maxv,expected",
    [
        ([1, 2, 3, 4], 2, 3, [2, 3]),
        ([-2, -1, 0, 1], -1, 0, [-1, 0]),
        ([10, 20], 0, 5, []),
    ],
)
def test_filter_outliers(numbers, minv, maxv, expected):
    assert filter_outliers(numbers, minv, maxv) == expected


def test_filter_outliers_inclusive_edges():
    assert filter_outliers([0, 1, 2], 0, 2) == [0, 1, 2]


def test_calculate_statistics_basic():
    stats = calculate_statistics([1, 2, 3])
    assert stats["min"] == 1.0
    assert stats["max"] == 3.0
    assert stats["average"] == 2.0


def test_calculate_statistics_single_value():
    assert calculate_statistics([7]) == {"min": 7.0, "max": 7.0, "average": 7.0}


def test_calculate_statistics_negative_values():
    stats = calculate_statistics([-5, -1, -3])
    assert stats["min"] == -5.0
    assert stats["max"] == -1.0
    assert stats["average"] == pytest.approx((-5 - 1 - 3) / 3)


def test_calculate_statistics_empty_raises():
    with pytest.raises(ValueError):
        calculate_statistics([])
