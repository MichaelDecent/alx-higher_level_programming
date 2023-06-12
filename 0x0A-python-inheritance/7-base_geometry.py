#!/usr/bin/python3
""" A Module that contains class BaseGeometry """


class BaseGeometry:
    """ contains a method that calculates area """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
