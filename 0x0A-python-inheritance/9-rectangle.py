#!/usr/bin/python3
""" A Module that contains a Base class BaseGeometry  subclass Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """
    def __init__(self, width, height):
        """ instantiation
            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('heigth', height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        """ prints tjhe rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height}")
