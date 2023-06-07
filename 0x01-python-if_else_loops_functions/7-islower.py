#!/usr/bin/python3
def islower(c):
    upperLimit = 97
    lowerLimit = 122
    if ord(c) <= lowerLimit:
        if ord(c) >= upperLimit:
            return True
        else:
            return False
    else:
        return False
