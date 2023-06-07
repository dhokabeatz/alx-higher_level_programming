#!/usr/bin/python3
startPoint = 97
endPoint = 123

for letter in range(startPoint, endPoint):
    if chr(letter) is not 'e' and chr(letter) is not 'q':
        print('{}'.format(chr(letter)), end='')
