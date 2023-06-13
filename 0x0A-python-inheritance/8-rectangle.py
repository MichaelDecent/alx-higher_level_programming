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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("heigth", height)
        self.__height = height
