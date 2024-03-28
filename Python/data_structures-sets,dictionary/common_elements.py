#!/usr/bin/python3
"""
Returns a set of common elements in two sets
"""
def common_elements(set_1, set_2):
    # This method is not efficient use & operator instead
    # common_set = set()
    # for member in set_1:
    #     if member in set_2:
    #         common_set.add(member)
    # return common_set
    return set_1 & set_2
