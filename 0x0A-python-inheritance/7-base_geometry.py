#!/usr/bin/python3
""" A Module that defines BaseGeometry """


class BaseGeometry:
    """ Defines BaseGeometry """
    def area(self):
        """ Calculates the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value and name
        Args:
            name(string) = Name
            value(int) = value
        """
        self.name = name
        if type(value) != int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        self.vaue = value
