#!/usr/bin/python3
""" A Module that contains a function that prints a name """


def say_my_name(first_name, last_name=""):
    """ says my name
    Args:
        first_name(str): first name
        last_name(str): last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
