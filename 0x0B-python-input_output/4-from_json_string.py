#!/usr/bin/python3
import json
""" This Module contains a function that returns an object
    (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string"""
    return (json.loads(my_str))
