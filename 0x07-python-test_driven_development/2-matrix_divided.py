#!/usr/bin/python3
# 2-matrix_divided.py
''' Define a function matrix_divded that returns a new matrix'''


def matrix_divided(matrix, div):
    '''Checks if matrix is a list of list of integers or float
    raise a TypeError
    Checks if each row of the matrix has the same size
    raise a TypeError
    Checks if div is a number (float or integer)
    checks if div is not equal to zero (0)
    Perform the division and round the result to 2 decimal places
    '''
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
