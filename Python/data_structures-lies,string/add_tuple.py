#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has atleast two elements, fill with 0
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    """ Return a list of elements with the sum of a corresponding
    elements from tuple_a and tuple_b"""
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]) 

