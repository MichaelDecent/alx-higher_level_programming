#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary, key=lambda k: a_dictionary[k])\
        if a_dictionary else None
