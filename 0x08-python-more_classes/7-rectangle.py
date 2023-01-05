#!/usr/bin/python3
""" class Rectangle defines a class """


class Rectangle:
    """ defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization
        args:
            width(int): width of the Rectangle
            height(int): height of the Rectangle
        Returns:
            None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ the Area od the retangle
        Returns:
            area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ the perimeter of a rectangle
        Returns:
            the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """print the rectangle with the characte"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle += str(self.print_symbol)
            if h < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """  return a string representation of the rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """prints a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
