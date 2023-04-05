#!/usr/bin/python3
import re

def text_indentation(text):
    """ function that prints a text with 2 new lines\
        after each of these characters: ., ? and :
        Args:
            text(str): text to be broken into smaller strings
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text_1 = text.replace(".", ".\n\n")
        text_2 = text_1.replace("?", "?\n\n")
        text_3 = text_2.replace(":", ":\n\n")
        text_string = text_3.split("\n")
        for i in range(len(text_string)):
            text_string[i] = text_string[i].strip()
        print("\n".join(text_string), end="")

            
        
