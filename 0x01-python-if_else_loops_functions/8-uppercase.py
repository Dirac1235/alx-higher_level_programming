#!/usr/bin/python3

def uppercase(str):
    for i in str:
        n = ord(i)
        if n > 96 and n < 123:
            n = 65 + n - 97
        print("{}".format(chr(n)), end='')
    print("")
