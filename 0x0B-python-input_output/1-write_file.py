#!/usr/bin/python3
""" This Module contains a function that writes a string to a
    text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
        Args:
             filename: name of the file
            text: text to written
        Returns:
            the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
