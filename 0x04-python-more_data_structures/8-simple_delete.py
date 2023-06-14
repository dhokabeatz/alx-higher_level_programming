#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key-value pair from a dictionary if the key exists."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
