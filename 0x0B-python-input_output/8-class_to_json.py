#!/usr/bin/python3
"""contains funciton that returns json representation of class"""


def class_to_json(obj):
    """returns the json representation of class """
    return obj.__dict__
