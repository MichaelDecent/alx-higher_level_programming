#!/usr/bin/python3
""" class Square definition """


class Square:
    """ Represents a square """
    def __init__(self, size=0):
        """ initializes the square
        Args:
            size (int): size of the square
        Returns:
            None
        """
        self.__size = size
    @property
    def size(self):
        """ getter of __size
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ settet of __size
        Args:
            value(int):
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates the area of the square
        Return:
            The area of the square
        """
        return self.__size ** 2

