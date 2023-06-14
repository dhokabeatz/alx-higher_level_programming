#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Finds the elements that are unique to each set."""
    different = set_1 ^ set_2
    return different
