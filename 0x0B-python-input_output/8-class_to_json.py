#!/usr/bin/python3
""" A module that defines a class to JSON function """


def class_to_json(obj):
    """ it returns a ictionary description or
        JSON serialization of an object
    """
    return (obj.__dict__)
