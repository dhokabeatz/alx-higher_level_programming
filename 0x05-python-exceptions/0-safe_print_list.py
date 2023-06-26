#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elementCount = 0
    for number in range(x):
        try:
            print(f"{my_list[number]}", end="")
            elementCount += 1
        except IndexError:
            break
    print()
    return (elementCount)
