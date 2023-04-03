#!/usr/bin/python3
""" class Rectangle: defines a retangle """


class Rectangle:
    """ Defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialization
            Args:
                width(int): width of the rectangle
                height(int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Returns the area of the rectangle """
        return (self.height * self.width)

    def perimeter(self):
        """ return the perimeter of the rectangle """
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))

    def __str__(self):
        """ prints the rectangle using # """
        rect_str = ""
        if self.height == 0 or self.width == 0:
            return (rect_str)
        for h in range(self.height):
            for w in range(self.width):
                try:
                    rect_str += str(self.print_symbol)
                except Exception:
                    rect_str += type(self).print_symbol
            if h == self.height - 1:
                break
            rect_str += '\n'

        return (rect_str)

    def __repr__(self):
        """ prints the formal rectangle string """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """ prints a message when a method or an attribute is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares between two rectangle
            Args:
                rect_1(object): 1st rectangle
                rect_2(object): 2nd rectangle
            Return: the biggest rectangle based on the area
        """
        if not isinstance(rect_1, object):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, object):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
