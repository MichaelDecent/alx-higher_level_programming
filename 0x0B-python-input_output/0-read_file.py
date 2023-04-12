#!/usr/bin/python3
""" A Module that reads a file """


def read_file(filename=""):
    """  a function that reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r', encoding="utf-8") as fp:
        print(fp.read(), end='')
