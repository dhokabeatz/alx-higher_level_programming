#!/usr/bin/python3

output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    diff = 0 if i % 2 == 0 else 32
    output += '{}'.format(chr(i - diff))
print('{}'.format(output),end=" ")
