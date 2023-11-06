#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of valid attributes and methods for the given object.
    """
    return (dir(obj))
