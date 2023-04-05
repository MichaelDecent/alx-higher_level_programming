#!/usr/bin/python3
""" a function that prints My name """


def say_my_name(first_name, last_name=""):
    """ a function that prints My name 
        Args:
            first_name(string): the first name
            last_name(string): the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")

