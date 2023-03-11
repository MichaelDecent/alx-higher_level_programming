#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_len1 = len(tuple_a)
    tuple_len2 = len(tuple_b)

    if tuple_len1 == 0:
        tuple_a = tuple_a + (0, 0)
    if tuple_len2 == 0:
        tuple_b = tuple_b + (0, 0)
    if tuple_len1 == 1:
        tuple_a = tuple_a + (0,)
    if tuple_len2 == 1:
        tuple_b = tuple_b + (0,)

    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
