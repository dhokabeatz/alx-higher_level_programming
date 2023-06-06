#!/usr/bin/python3
import random as r

number = r.randint(-100,100)

if number > 0:
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
else:
    print(f'{number} is zero')
