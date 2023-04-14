#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
        Args:
        filename(str) = Name of file
        search_strings = string to replace
        new_string = the new string
    """
    new_text = ""
    with open(filename) as fp:
        for line in fp:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, 'w') as fp:
        fp.write(new_text)
