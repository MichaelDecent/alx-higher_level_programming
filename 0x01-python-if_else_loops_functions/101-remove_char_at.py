#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = str

    for i in range(len(str_copy)):
        if i == n:
            return (str_copy.replace(str_copy[i], ''))
    return (str_copy)
