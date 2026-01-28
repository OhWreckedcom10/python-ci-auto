from __future__ import annotations

from typing import Iterable, List, Dict


def normalize_numbers(numbers: Iterable[float]) -> List[float]:
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers must not be empty")

    mn = min(nums)
    mx = max(nums)
    if mx == mn:
        # כל הערכים זהים -> נמפה ל-0.0 (נורמלי, אין טווח)
        return [0.0 for _ in nums]

    return [(x - mn) / (mx - mn) for x in nums]

def filter_outliers(numbers: Iterable[float], min_value: float, max_value: float) -> List[float]:
    return [x for x in numbers if min_value <= x <= max_value]


def calculate_statistics(numbers: Iterable[float]) -> Dict[str, float]:
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers must not be empty")

    return {
        "min": float(min(nums)),
        "max": float(max(nums)),
        "average": float(sum(nums) / len(nums)),
    }
