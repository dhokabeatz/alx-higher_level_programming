#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Square each element in the matrix."""
    return [[x ** 2 for x in row] for row in matrix]
