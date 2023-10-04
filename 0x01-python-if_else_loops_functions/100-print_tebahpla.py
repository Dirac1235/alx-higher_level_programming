#!/usr/bin/python3

for i in range(26, 0, -1):
    if i % 2 == 0:
        print("{}".format(chr(i+96)), end='')
    else:
        print("{}".format(chr(i+64)), end='')
