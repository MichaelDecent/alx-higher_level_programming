#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        n_matrix = []
        for i in rows:
            n_matrix.append(i**2)
        new_matrix.append(n_matrix)

    return new_matrix



