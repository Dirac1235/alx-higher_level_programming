#!/usr/bin/python3

for i in range(1, 100):
    if ((i % 10) * 10 + i // 10) > i:
        print("{:02}".format(i), end='')
        if i < 89:
            print(", ", end='')
print('')
