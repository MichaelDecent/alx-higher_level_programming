#!/usr/bin/python3
from models.base import Base
""" A Module that defines a class Retangle 
    that inherits from super class Base
"""


class Rectangle(Base):
    """ defines a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    #getter and setter function for width
    @property
    def width(self):
        """ width setter """
        return (self.__width)

    @width.setter
    def width(self, new_width):
        """ width setter """
        if type(new_width) != int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    #getter and setter function for height
    @property
    def height(self):
        """ height getter """
        return (self.__height)

    @height.setter
    def height(self, new_height):
        """ height settter """
        if type(new_height) != int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height
    
    #getter and setter function for x
    @property
    def x(self):
        """ x getter """
        return (self.__x)
    
    @x.setter
    def x(self, new_x):
        """ height setter """
        if type(new_x) != int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    #getter and setter function for y
    @property
    def y(self):
        """ y getter """
        return (self.__y)
    
    @y.setter
    def y(self, new_y):
        """ y setter """   
        if type(new_y) != int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """ calculates the area of the rectangle """
        return (self.height * self.width)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for y in range(self.y):
            print()
        for row in range(self.height):
            x = 0
            for col in range(self.width):
                while (x < self.x):
                    print(' ', end='')
                    x += 1
                else:
                    print('#', end='')
            print()

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args):
        """ updates the values of the argument """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

