#!/usr/bin/python3
""" This Module inherits from class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
