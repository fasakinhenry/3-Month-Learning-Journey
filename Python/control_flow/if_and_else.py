#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Prints the output of number followed by "is negative/positive/zero"
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
