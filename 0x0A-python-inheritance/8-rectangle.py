#!/usr/bin/python3
"""Defines a BaseGeometry subclass Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initializes a new instance of the class with the given width and height.

    :param width: An integer representing the width of the instance.
    :type width: int
    :param height: An integer representing the height of the instance.
    :type height: int
    :return: None
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
