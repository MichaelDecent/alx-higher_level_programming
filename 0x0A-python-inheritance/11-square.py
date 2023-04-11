#!/usr/bin/python3
""" This Module inherits from class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a Square by inheriting Rectangle """

    def __init__(self, size):
        """ Initialization """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Prints the square description: [Square] <width>/<height> """
        return (f"[Square] {self.__size}/{self.__size}")
