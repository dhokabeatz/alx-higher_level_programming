#!/usr/bin/python3


def no_c(my_string):
    container = ''
    if my_string:
        for letter in my_string:
            if letter != 'c' and letter != 'C':
                container += letter
    return container
