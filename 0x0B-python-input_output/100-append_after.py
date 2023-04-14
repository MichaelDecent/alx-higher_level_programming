#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
        Args:
        filename(str) = Name of file
        search_strings = string to replace
        new_string = the new string
    """
    with open(filename, 'a+') as fp:
        for line in fp:
            if search_string in line:
                fp.write('\n')
                fp.write(new_text)
