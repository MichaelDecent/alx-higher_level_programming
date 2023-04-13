#!/usr/bin/python3
""" A module that defines a class Student """


class Student:
    """ it defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return (self.__dict__)
    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
