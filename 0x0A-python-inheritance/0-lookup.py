#!/usr/bin/python3
""" This Module contains a function that returns the
list of available attributes and methods of an object """


def lookup(obj):
    """ a function that returns the list of
        available attributes and methods of an object
        Args:
            obj: the object
        Returns:
            the list of available attributes and methods of an object
    """
    return (dir(obj))
