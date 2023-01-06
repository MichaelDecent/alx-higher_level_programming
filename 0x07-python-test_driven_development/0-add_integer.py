#!/usr/bin/python3
"""
Contains  module that adds two integers
it has a function with two integer arguments
and returns an integer
"""


def add_integer(a, b=98):
    """ this function adds two integer
    Args:
        a(int): first integer
        b(int): second integer
    Returns:
        the addition of two integer
    """
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    elif (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
