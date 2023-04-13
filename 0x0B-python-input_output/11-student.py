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
        if (attrs == list and all(type(attr) == str for attr in attr)):
            return (attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr))
        return (self.__dict__)

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student
        """
        for key, value in json.items():
            setattr(self, key, value)
