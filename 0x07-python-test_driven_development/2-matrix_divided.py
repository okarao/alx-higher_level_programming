#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for elements in matrix:
        if not isinstance(elements, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for items in elements:
            if not isinstance(items, (int,float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for elements in matrix:
        if len(elements) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(elements) != len(matrix[0]) for elements in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    new_matrix = [[round(items / div, 2) for items in elements] for elements in matrix]

    return new_matrix
