#!/usr/bin/python3
""" This Module inherits from class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a Rectangle by inheriting BaseGeometry """

    def __init__(self, width, height):
        """ Initialization """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculates Area """
        return (self.__width * self.__height)

    def __str__(self):
        """ return, the following rectangle description:
            [Rectangle] <width>/<height>
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
