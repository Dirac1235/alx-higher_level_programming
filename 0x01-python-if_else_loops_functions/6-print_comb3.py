#!/usr/bin/python3

for i in range(0, 100):
    if i < 12:
        print("{:02}".format(i), end=', ')
        continue
    if ((i % 10) * 10 + i // 10) > i:
        print(i, end='')
        if i < 89:
            print(", ", end='')
