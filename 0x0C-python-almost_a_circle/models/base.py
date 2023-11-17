#!/usr/bin/python3
""" contains base class """


class Base(object):
    """ contains a Base class modules """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ initalizes id"""
        if id is not None:
            self.id = id
        else:
            Base.id += 1

    __nb_objects += 1
