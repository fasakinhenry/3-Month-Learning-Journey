#!/usr/bin/python3
# Function that squares value of all integers using map
def square_matrix_map(matrix=[]):
    return list(map(lambda sublist: list(map(lambda x: x**2, sublist)), matrix))
