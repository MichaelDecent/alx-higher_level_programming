#!/usr/bin/python3
""" This Module defines a function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """  a function that creates an Object from a “JSON file”
        Args:
            my_obj(str): the object to be deserilized
            filename: json file
    """
    with open(filename, 'r') as fp:
        return (json.load(fp))
