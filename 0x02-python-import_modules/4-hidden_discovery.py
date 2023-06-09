#!/usr/bin/python3
import hidden_4


def printNames():
    allNames = dir(hidden_4)
    for everyname in allNames:
        if everyname[:2] != "__":
            print(everyname)


if __name__ == "__main__":
    printNames()
