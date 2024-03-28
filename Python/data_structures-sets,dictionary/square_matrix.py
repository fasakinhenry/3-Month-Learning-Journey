#!/usr/bin/python3
"""
Completes the square of all integers of a matrix
"""
def square_matrix(matrix=[]):
    if matrix ==[]:
        return matrix
    new_matrix = [[x**2 for x in i] for i in matrix]
    return new_matrix
