#!/usr/bin/python3
""" This Module contains a function that appends a string at the
    end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
        Args:
            filename = name of the file
            text = text to be appended
        Returns:
            the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
