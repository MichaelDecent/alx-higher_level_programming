#!/usr/bin/python3
""" class Square: defines the class-square"""


class Square:
    """This is where the class is defined """
    def __init__(self, size=0):
        """
        initialization
        Args:
            size(int): the size of the square
        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
