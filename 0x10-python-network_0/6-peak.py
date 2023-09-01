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
    if len(list_of_integers) == 0:
        return None
    peak = None
    if len(list_of_integers) > 2:
        for idx in range(len(list_of_integers) - 2):
            val = list_of_integers[idx + 1]
            if (val >= list_of_integers[idx] and val >=
                    list_of_integers[idx + 2]):
                peak = val
        return peak
    else:
        return max(list_of_integers)
