#!/usr/bin/python3
""" This Module cotanins a class Student """


class Student:
    """ a prototype of individual student """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """  retrieves a dictionary representation of a Student instance """
        return (self.__dict__)
