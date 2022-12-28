#!/usr/bin/python3
""" class Square definition """


class Square:
    """ Represents a Square """
    def __init__(self, size=0):
        """ initializes a square
        Args:
            size(int): size of the square
        """
        if size < 0:
            raise TypeError("size must be an integer")
        elif type(size) is not int:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
