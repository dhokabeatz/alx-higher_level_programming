#! /usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elementCount = 0

    try:
        for number in range(x):
            print("{}".format(number),end="")
            elementCount +=1
    except IndexError:
        print()
    
    return elementCount

        