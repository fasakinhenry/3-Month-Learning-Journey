#!/usr/bin/python3
""" Returns a list with all the values multiplied by a number
Without using loops """
def multiply_list_map(my_list=[], number = 0):
    return list(map(lambda x: x * number, my_list))
