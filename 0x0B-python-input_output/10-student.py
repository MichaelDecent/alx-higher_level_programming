#!/usr/bin/python3
""" A module that defines a class Student """


class Student:
    """ it defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        return (self.__dict__)
