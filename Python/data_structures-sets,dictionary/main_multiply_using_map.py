#!/usr/bin/python3
multiply_list_map = __import__('multiply_using_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
