#!/usr/bin/python3
""" class Rectangle: defines a rectangle """


class Rectangle:
    """ defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for width of the rectangle
            Returns:
                width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, new_width):
        """ setter for width of the rectangle
            Args:
                new_width(int): new width of the rectangle
        """
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = new_width

    @property
    def height(self):
        """ getter for height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, new_height):
        """ setter for height of )the rectangle
            Args:
                new_height(int): new height of the rectangle
        """
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = new_height

    def area(self):
        """ area of the the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle """
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ prints the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = ""
            for col in range(self.__height):
                for row in range(self.__width):
                    rect += str(self.print_symbol)
                if col < self.__height - 1:
                    rect += "\n"
        return (rect)

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ prints a message when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares between two rectangles and returns the bigger
            rectangle based on their area
            Args:
                rect_1(int): first rectangle
                rect_2(int): second rec
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
