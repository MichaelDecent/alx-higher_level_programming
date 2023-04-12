#!/usr/bin/python3
""" A module defines a JSON to string function """


def from_json_string(my_str):
    """ a function that returns an object
        (Python data structure) represented by a JSON string:
        Args:
            my_str(str): The string to be desterilized
        Return: an object (Python data structure) represented by a JSON string
    """
    return (json.loads(my_str))


