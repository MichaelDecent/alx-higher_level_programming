#!/usr/bin/python3n
""" This Module that contains a function that writes an
    Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a JSON representation """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
