#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i == row[-1]:
                print("{:d}".format(i), end='')
                break
            print("{:d}".format(i), end=' ')

        print()
