#!/usr/bin/python3
import sys


def summer():
    totalSum = 0
    args = sys.argv
    for arg in range(len(args) - 1):
        totalSum += int(args[arg + 1])
    print("{}".format(totalSum))


if __name__ == "__main__":
    summer()
