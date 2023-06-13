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
        """ Returns the area of the Rectangle """
        return (self.__size ** 2)
