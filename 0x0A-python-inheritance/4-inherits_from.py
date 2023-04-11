#!/usr/bin/python3
""" This Module checks if the object is an instance
    of a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object is an
        instance of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False
    """
    if issubclass(obj, a_class):
        return True
    return False
