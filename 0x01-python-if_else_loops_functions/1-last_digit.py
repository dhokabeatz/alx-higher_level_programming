#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
string = "Last digit of "
verb = "is"
lastDigitOfNumber =  str(number)[-1]
last = int(lastDigitOfNumber)
moreThanFive = "and is greater than 5"
equalToZero = "and is 0"
zeroToSix = "and is less than 6 and not 0"

if last > 5:
    print(f'{string} {number} {verb} {lastDigitOfNumber} {moreThanFive}')
elif last == 0:
    print(f'{string} {number} {verb} {lastDigitOfNumber} {equalToZero}')
elif last < 6 and last != 0:
    print(f'{string} {number} {verb} {lastDigitOfNumber} {zeroToSix}')
