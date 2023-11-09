#!/usr/bin/python3
"""Defines a text file inserting function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): File name.
        new_string (str): The string to insert.
        search_string (str): The string to search in file.
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
