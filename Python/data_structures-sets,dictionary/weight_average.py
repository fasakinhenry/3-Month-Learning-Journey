#!/usr/bin/python3
# Returns the weighted average of the all integers tuple
def weight_average(my_list=[]):
    # Return O if the list is empty
    if not my_list:
        return 0
    # Initialize the result of the weighted average
    running_sum = 0
    # let accumulated multiplier be 1
    multiplier = 0
    for i in my_list:
        multiplier += i[0] * i[1]
        running_sum += i[1]
    return multiplier / running_sum
            

