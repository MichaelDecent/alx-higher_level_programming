#!/usr/bin/python3
""" A Module that contains a function thta prints a Square """


def print_square(size):
    """ prints a Square with the character '#'
        Args:
            size(int): size of the Square
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
