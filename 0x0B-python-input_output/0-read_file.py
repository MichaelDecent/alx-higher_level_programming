#!/usr/bin/python3
""" This Module contains a function that reads
    a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout
        Args:
            filename: name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
