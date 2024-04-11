#!/usr/bin/python3
Square = __import__('print_square_instance').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
