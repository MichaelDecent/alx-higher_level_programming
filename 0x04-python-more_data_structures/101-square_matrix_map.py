def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda y: [x ** 2 for x in y], matrix))
    return (new_matrix)
