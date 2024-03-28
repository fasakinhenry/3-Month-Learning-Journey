#!/usr/bin/python3
square_matrix = __import__('square_matrix').square_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new = square_matrix(matrix)
print(new)
print(matrix)
