#!/usr/bin/python3
""" class Square definition """


class Square:
    """ Represents a square """
    def __init__(self, size=0):
        """ initializes the square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ a method that calculate the area of the square
        given the size of the square"""
        return self.__size ** 2
