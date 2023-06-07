#!/usr/bin/python3
""" A Module thta contains a function that prints a
    text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """  prints a text with 2 new lines after
        each of these characters: ., ? and :
        Args:
            text(str): text to be indented
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    nstr = text.replace(".", ".\n\n")
    nstr2 = nstr.replace("?", "?\n\n")
    nstr3 = nstr2.replace(":", ":\n\n")
    nstr4 = nstr3.strip(" ")
    nstr5 = nstr4.split("\n")
    for i in range(len(nstr5)):
        nstr5[i] = nstr5[i].strip(" ")
    print("\n".join(nstr5), end="")
