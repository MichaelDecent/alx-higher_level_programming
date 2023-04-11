#!/usr/bin/python3
""" This Module inherits from class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """ Defines a Square by inheriting Rectangle """

    def __init__(self, width, height):
        """ Initialization """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates Area"""
        return (self.__width ** 2)

    def __str__(self):
        """ return, the following rectangle description:
            [Square] <width>/<height>
        """
        return (f"[Square] {self.__width}/{self.__height}")
