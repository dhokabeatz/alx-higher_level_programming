#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Multiplies the values in a dictionary by 2 and returns a new dictionary."""
    return {key: val * 2 for key, val in a_dictionary.items()}
