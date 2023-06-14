#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Calculates the sum of unique elements in the list."""
    uniqueElements = set(my_list)
    number = sum(uniqueElements)
    return number
