#!/usr/bin/python3
""" class Rectangle defines a class """


class Rectangle:
    """ defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """ initialization
        args:
            width(int): width of the Rectangle
            height(int): height of the Rectangle
        Returns:
            None
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of the Rectangle
        Return:
            the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width of the Rectangle
        Args:
            value(int): the value of the width
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height of Rectangle
        Return:
            the height of the Retangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height of the Rectangle
        Args:
            value(int): the value for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
