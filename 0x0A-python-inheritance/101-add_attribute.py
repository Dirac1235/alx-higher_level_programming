#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute.
        att (str): The name of the attribute to add to obj.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if getattr(obj, "__dict__", 1) == 1:
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
