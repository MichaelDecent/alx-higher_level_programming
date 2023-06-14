#!/usr/bin/python3
""" This Module cotanins a class Student """


class Student:
    """ a prototype of individual student """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary representation of a Student instance """
        if type(attrs) is list and all([type(attr) == str for attr in attrs]):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}      
        return (self.__dict__)
