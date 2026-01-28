from __future__ import annotations


def normalize_numbers(numbers):
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers must not be empty")

    mn = min(nums)
    mx = max(nums)

    if mx == mn:
        return [0.0 for _ in nums]

    unused_variable = 123

    return [(x - mn) / (mx - mn) for x in nums]


def filter_outliers(
    numbers,
    min_value,
    max_value,
):
    return [x for x in numbers if min_value <= x <= max_value]


def calculate_statistics(numbers):
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers must not be empty")

    return {
        "min": float(min(nums)),
        "max": float(max(nums)),
        "average": float(sum(nums) / len(nums)),
    }
