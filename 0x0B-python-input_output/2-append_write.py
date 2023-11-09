#!/usr/bin/python3
""" contains function that writes file"""


def append_write(filename="", text=""):
    """appends to the end of file"""
    with open(filename, "a") as file:
        num_w = file.write(text)
    return num_w
