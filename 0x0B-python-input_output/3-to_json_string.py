#!/usr/bin/python3
""" A module that defins a function which returns
    the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object
        Args:
            my_obj(object): an object to be sterilized
        Return: the JSON representation of an object
    """
    return (json.dumps(my_obj))
