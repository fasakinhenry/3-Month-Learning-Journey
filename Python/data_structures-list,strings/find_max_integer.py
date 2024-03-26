#!/usr/bin/python3
# Find the biggest integer of a list
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_value = my_list[0]
    for value in range(0, len(my_list)):
        if my_list[value] > max_value:
            max_value = my_list[value]
    return max_value
