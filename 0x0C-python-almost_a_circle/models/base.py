#!/usr/bin/python3
""" This Module defines a class Base model """


class Base:
    """ A Base Class for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
