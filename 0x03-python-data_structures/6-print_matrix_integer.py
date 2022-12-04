#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in matrix[0]:
            if i == len(matrix[0]):
                print("{}".format(row[i - 1]))
                break
            print("{}".format(row[i - 1]), end=" ")
    print()


