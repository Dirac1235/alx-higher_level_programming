#!/usr/bin/python3
""" contains function that writes file"""


def write_file(filename="", text=""):
    """ function that writes to file and returns the number
    of characters written
    """
    with open(filename, "w") as file:
        num_w = file.write(text)
    return num_w
