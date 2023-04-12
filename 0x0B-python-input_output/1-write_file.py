#!/usr/bin/python3
""" This Module defines a funtion that writes a function """


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8) """
    with open(filename, 'w', encoding="utf-8") as fp:
        return (fp.write(text))
