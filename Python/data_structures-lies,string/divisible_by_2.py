#!/usr/bin/python3
# Function that finds all the multiples of 2 in a list
def divisible_by_2(my_list=[]):
    # Longer method
    # new_list = []
    # for i in range(0, len(my_list)):
    #     if my_list[i] % 2 == 0:
    #         new_list.append(True)
    #     else:
    #         new_list.append(False)
    # return new_list
    return [num % 2 == 0 for num in my_list]
