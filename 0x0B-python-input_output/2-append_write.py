#!/usr/bin/python3
""" This Module that defines a function that appends 
    a string to the end of a text file 
"""


def append_write(filename="", text=""):
    """  a function that appends a string at the end of a text file 
        Args:
            filename(str) = Name of the file
            text(str) = text to be appended
        Return: the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        return (fp.write(text))
