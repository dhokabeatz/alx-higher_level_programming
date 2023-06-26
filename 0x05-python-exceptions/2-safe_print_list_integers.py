#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    elementCount = 0
    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end="")
            elementCount += 1
        except (TypeError, ValueError, IndexError):
            pass
    print()
    return (elementCount)
