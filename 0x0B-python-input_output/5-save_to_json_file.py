#!/usr/bin/python3
""" This Module defines a function that writes an 
    Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation
        Args:
            my_obj(str): the object to be serilized
            filename: json file
    """
    with open(filename, 'w') as fp:
        json.dump(my_obj, fp)
