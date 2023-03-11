#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    tuple_list = []
    for i in range(len(tuple_a)):
        if tuple_a[i] == None:
            tuple_a[i] = 0
        elif tuple_b[i] == None:
            tuple_b[i] = 0

        tuple_list.append(tuple_a[i] + tuple_b[i])

    final_tuple = tuple(tuple_list)
    return (final_tuple)
