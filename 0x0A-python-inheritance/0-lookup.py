#!/usr/bin/python3
""" This Module returns the list of available 
    attributes and methods of an object
"""


def lookup(obj):
    """ A function that returns the list of available
        attributes and methods of an object
        Args:
            obj(object): the object
        Return: the list of available attributes and methods of an object

    """
    return (dir(obj))
