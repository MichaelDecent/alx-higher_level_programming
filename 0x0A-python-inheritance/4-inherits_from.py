#!/usr/bin/python3
""" This Module contains a function that checks if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class
"""


def inherits_from(obj, a_class):
    """ checks if a  object is an instance of a class that
        inherited (directly or indirectly) from the specified class
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return (True)
    return (False)
