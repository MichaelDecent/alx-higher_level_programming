#!/usr/bin/python3
""" A Module that contains a function that checks if the object
    is an instance of, or if the object is an instance of a class
    that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """ checks if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class
        Args:
            obj: the object
            a_class: the class
    """
    return (isinstance(obj, a_class))
