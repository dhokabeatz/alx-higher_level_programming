#!/usr/bin/python3
def uppercase(str):
    upperLimit = 122
    loweLimit = 97
    for str in str:
        if ord(str) >= loweLimit and ord(str) <= upperLimit:
            str = chr(ord(str) - 32)
        print("{}".format(str), end="")
    print("")
