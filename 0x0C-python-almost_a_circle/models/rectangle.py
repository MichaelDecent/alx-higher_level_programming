#!/usr/bin/python3
""" This Module contains class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initailization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # getters
    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @property
    def y(self):
        """ getter for y """
        return self.__y

    # setters
    @width.setter
    def width(self, new_width):
        """ setter for height """
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        """ setter for height """
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @x.setter
    def x(self, new_x):
        """ setter for x """
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        """ setter for y """
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """ returns the area value of the Rectangle instance """
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for vet in range(self.__y):
            print()
        for col in range(self.__height):
            for row in range(self.__width + self.__x):
                if row < self.__x:
                    print(" ", end='')
                else:
                    print("#", end='')
            if col < self.__height:
                print()

    def __str__(self):
        """ returns '[Rectangle] (<id>) <x>/<y> - <width>/<height>' """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ upadtes the attributes of the class """
        if args and len(args) != 0:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.__width = arg
                elif n == 2:
                    self.__height = arg
                elif n == 3:
                    self.__x = arg
                elif n == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
