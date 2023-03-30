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

    @property
    def size(self):
        """ Gets the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates the area of the sqauare """
        return (self.__size ** 2)

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

