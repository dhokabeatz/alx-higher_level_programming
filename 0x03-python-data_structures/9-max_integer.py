#!/usr/bin/python3


def max_integer(my_list=[]):
    max = 0
    if len(my_list) > 0:
        for number in my_list:
            if number > max:
                max = number
            else:
                max = max
        return max
    else:
        return None

