#!/usr/bin/python3
"""
Returns a key with the biggest value
"""
def biggest_integer(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary == {}:
        return None
    first_key = list(a_dictionary.keys())[0]
    biggest_value = a_dictionary[first_key]
    for key, value in a_dictionary.items():
        if value > biggest_value:
            biggest_value = value
            biggest_key = key
    return biggest_key

            