#!/usr/bin/python3
""" A Module that contains class BaseGeometry """


class BaseGeometry:
    """ contains a method that calculates area """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
