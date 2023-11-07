#!/usr/bin/python3
""" contains function that reads file and prints it"""


def read_file(filename=""):
    """ function that reads from file and prints to stdout"""
    with open(filename) as file:
        print(file.read())
