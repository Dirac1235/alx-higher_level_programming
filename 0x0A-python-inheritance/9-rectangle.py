#!/usr/bin/python3
"""Defines a BaseGeometry subclass Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
        Initializes a new instance of the class with
        the given width and height.

        :param width: An integer representing the width of the object.
        :param height: An integer representing the height of the object.
        :return: None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangel] " + str(self.__width) + "/" + str(self.__height)
