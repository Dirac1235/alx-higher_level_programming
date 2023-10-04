#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit = last if number > 0 else -last_digit
info = "0"
if last_digit > 5:
    info = "greater than 5"
elif last_digit != 0:
    info = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {info}")
