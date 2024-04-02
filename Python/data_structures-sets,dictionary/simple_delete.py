#!/usr/bin/python3
"""
Function that deletes a key in a dictionary
"""
def simple_delete(a_dictionary, key=""):
    if a_dictionary == {}:
        return
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
