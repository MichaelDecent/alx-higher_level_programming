#!/usr/bin/python3
""" This Module contains a a class Square that inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """  inherits from Rectangle """
    def __init__(self, size):
        """ instanciation
        Args:
            size: size of the Square
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ return the area of the Square """
        return (self.__size ** 2)

    def __str__(self):
        """ returns the square description: [Square] <width>/<height> """
        return (f"[] {self.__size}/{self.__size}")
