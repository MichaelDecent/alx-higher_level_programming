#!/usr/bin/python3
def magic_string():
    magic_string.no_times = getattr(magic_string, 'no_times', 0) + 1
    return ','.join(["BestSchool" for i in range(magic_string.no_times)])
