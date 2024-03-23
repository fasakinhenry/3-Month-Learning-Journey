#!/usr/bin/python3
# Implement binary search algorithm to sarch for a value in an array
# To use binary search, the array must be ordered
def binary_search(array, search_value):
    # Get the lower and upperbound of the array
    # Lower bound is the first value in the array
    # Upper bound is the last value in an array
    lower_bound = 0
    upper_bound = len(array) - 1

    # Create a loop to keep inspecting the value of the midpoint of array
    while lower_bound <= upper_bound:
        # Get midpoint since binary sort uses midpoint to remove unwanted parts of array
        midpoint = int((lower_bound + upper_bound) / 2)
        # Get the value at the midpoint of the array each time
        value_at_midpoint = array[midpoint]

        # If the value at the midpoint is what we are looking for, we're done
        # if not we change the lower or upper bound depending on whether
        # we are guessing higher or lower
        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

binary_search([3, 17, 75, 80, 202], 22)
