#!/usr/bin/python3
""" class Rectangle: defines a retangle """


class Rectangle:
    """ Defines a rectangle """
    
    def __init__(self, width=0, height=0):
        """ Initialization 
            Args:
                width(int): width of the rectangle
                height(int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter fot the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, w_value):
        """ setter fot the width of the rectangle 
            Args:
                w_value(int): the new value of width of the rectangle
        """
        if not isinstance(w_value, int):
            raise TypeError("width must be an integer")
        if w_value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = w_value

    @property
    def height(self):
        """ getter for the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, h_value):
        """ setter for the height of the rectangle 
            Args:
                h_value(int): the value of new height of the rectangle
        """
        if not isinstance(h_value, int):
            raise TypeError("height must be an integer")
        if h_value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h_value
