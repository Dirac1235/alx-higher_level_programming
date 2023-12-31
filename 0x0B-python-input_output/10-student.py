#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=[]):
        """Get a dictionary representation of the Student."""
        diction = self.__dict__
        if attr == []:
            return diction

        def my_filter_fun(pair):
            """used to filter the dictionary"""
            keys, value = pair
            return keys in attr
        diction = dict(filter(my_filter_fun, diction.items()))
        return diction
