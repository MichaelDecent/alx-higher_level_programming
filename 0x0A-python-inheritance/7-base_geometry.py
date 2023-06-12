#!/usr/bin/python3
""" A Module that contains class BaseGeometry """


class BaseGeometry:
    """ contains a method that calculates area """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(self.value) not int:
            raise TypeError("self.value must be an integer")
        if self.value <= 0:
            raise ValueError("self.value must be greater than 0")
