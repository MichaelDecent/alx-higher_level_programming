#!/usr/bin/python3
""" Module to add two integer """


def add_integer(a, b=98):
    """ adds two integers
        Args:
            a(int): 1st integer
            b(int): 2nd integer
        Return: the sum of two integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
