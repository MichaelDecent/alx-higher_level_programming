#!/usr/bin/python3
""" This Module defines a function that creates an Object from a “JSON file” """
import json


def save_to_json_file(my_obj, filename):
    """  a function that creates an Object from a “JSON file”
        Args:
            my_obj(str): the object to be deserilized
            filename: json file
    """
    with open(filename, 'r') as fp:
        return (json.load(fp))
