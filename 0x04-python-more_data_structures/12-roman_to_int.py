#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): Roman numeral string.

    Returns:
        int: Integer representation of the Roman numeral.

    """
    if not roman_string or type(roman_string) != str:
        return 0

    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for roman in reversed(roman_string):
        arab = digits.get(roman, 0)
        total += arab if total < arab * 5 else -arab

    return total
