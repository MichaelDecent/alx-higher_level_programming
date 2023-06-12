#!/usr/bin/python3
""" This Module contains a function that checks if the
    object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """  a function that returns True if the object is
        exactly an instance of the specified class ; otherwise False
        Args:
            obj: the object
            a_class: the class
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
