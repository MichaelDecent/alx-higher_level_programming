#!/usr/bin/python3
"""
This module contains a function that finds
the peak of a list of an unsorted array
"""


def find_peak(list_of_integers):
    """
    finds and returns the peak of a list of an unsorted array
        Args:
            list_of_integers(list)
    """
    no_list = len(list_of_integers)
    if no_list == 0 or type(list_of_integers) != list:
        return None

    if not all(type(n) == int for n in list_of_integers):
        raise TypeError("list_of_integer must be a list of integers")

    if no_list < 3:
        return max(list_of_integers)
    else:
        mid = no_list // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid:])

    return list_of_integers[mid]
