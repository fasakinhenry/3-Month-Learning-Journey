#!/usr/bin/python3
# Prints the values of integer in a matrix
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()
