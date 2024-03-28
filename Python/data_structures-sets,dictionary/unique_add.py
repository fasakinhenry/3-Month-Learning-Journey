#!/usr/bin/python3
"""
Adds all unique integers in a list(only once for each integer)
"""
def unique_add(my_list=[]):
    if my_list == []:
        return
    unique_numbers = []
    running_sum = 0
    for num in my_list:
        if num not in unique_numbers:
            running_sum += num
            unique_numbers.append(num)
    return running_sum
