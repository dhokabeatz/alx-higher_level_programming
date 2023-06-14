#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Searches for elements in the list and replaces them with the specified value."""
    def find_search(element):
        return element if element != search else replace
    return [find_search(element) for element in my_list]
