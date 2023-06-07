#!/usr/bin/python3
""" 
    This Module contains a function
    that adds two integers
    and returns an integer
"""


def add_integer(a, b=98):
    """ Adds two integers
        Args:
            a(int or float) = first integer
            b(int of float) = second integer
        Returns:
            the sum of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
