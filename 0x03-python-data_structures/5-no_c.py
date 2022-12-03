#!/usr/bin/python3

def no_c(my_string):
    n_string = my_string.translate({ord('c'): None})
    n_string = n_string.translate({ord('C'): None})

    return n_string
