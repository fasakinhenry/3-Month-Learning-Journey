#!/usr/bin/python3
"""
Replaces all the occurrences of an element by another
in a new list
"""
def search_replace(my_list, search, replace):
    if my_list == []:
        return my_list
    return [replace if x == search else x for x in my_list]
