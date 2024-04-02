#!/usr/bin/python3
"""
Prints a dictionary by ordered keys
"""
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == {}:
        return
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
