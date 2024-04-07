#!/usr/bin/python3
Square = __import__('square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
