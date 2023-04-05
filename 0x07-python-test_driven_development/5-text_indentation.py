#!/usr/bin/python3
import re

def text_indentation(text):
    """ function that prints a text with 2 new lines\
        after each of these characters: ., ? and :
        Args:
            text(str): text to be broken into smaller strings
    """
    delimiters = ".:?"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text_string = re.split("[" + re.escape(delimiters) + "]", text)
        for text_str in text_string:
            print(text_str, '\n')
