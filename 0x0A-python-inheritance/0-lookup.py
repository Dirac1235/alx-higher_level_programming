#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of valid attributes and methods for the given object.

    :param obj: The object to look up.
    :type obj: Any
    :return: A list of valid attributes and methods for the object.
    :rtype: List[str]
    """
    return (dir(obj))
