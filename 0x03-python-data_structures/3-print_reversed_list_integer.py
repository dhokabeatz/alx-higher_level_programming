#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        reverse_list = reversed(my_list)
        for item in reverse_list:
            print('{:d}'.format(item))
