#!/usr/bin/python3
for number in range(0, 10):
    for value in range((number + 1), 10):
        if number == 8 and value == 9:
            print("{}{}".format(number, value))
        else:
            print("{}{}".format(number, value), end=", ")
