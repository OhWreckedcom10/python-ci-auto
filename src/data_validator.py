def is_positive(number):
    return number > 0


def is_in_range(number, min_value, max_value):
    return min_value <= number <= max_value


def is_integer(value):
    # בודק גם int וגם float ששווה לערך שלם
    if isinstance(value, bool):
        return False  # כי True/False הם תת־סוג של int
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return value.is_integer()
    return False
