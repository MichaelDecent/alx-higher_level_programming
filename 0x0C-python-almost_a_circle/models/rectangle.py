#!/usr/bin/python3
from models.base import Base
""" A Module that defines a class Retangle 
    that inherits from super class Base
"""


class Rectangle(Base):
    """ defines a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    #getter and setter function for width
    @property
    def width(self):
        """ width setter """
        return (self.__width)

    @width.setter
    def width(self, new_width):
        """ width setter """
        self.__width = new_width

    #getter and setter function for height
    @property
    def height(self):
        """ height getter """
        return (self.__height)

    @height.setter
    def height(self, new_height):
        """ height settter """
        self.__height = new_height
    
    #getter and setter function for x
    @property
    def x(self):
        """ x getter """
        return (self.__x)
    
    @x.setter
    def x(self, new_x):
        """ x stter """
        self.__x = new_x

    #getter and setter function for y
    @property
    def y(self):
        """ y getter """
        return (self.__y)
    
    @y.setter
    def y(self, new_y):
        """ y setter """
        self.__y = new_y
