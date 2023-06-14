#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in a list by a given number using map.

    Args:
        my_list (list): List of numbers.
        number (int): Number to multiply each element by.

    Returns:
        list: List with each element multiplied by the given number.

    """
    return list(map(lambda x: x * number, my_list))
