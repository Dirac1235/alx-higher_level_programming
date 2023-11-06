#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the
        specified class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
