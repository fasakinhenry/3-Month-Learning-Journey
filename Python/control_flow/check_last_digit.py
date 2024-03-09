#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
""" Checks if the last digit of number is
greater than 5, equals 0 or less than 6 and not 0"""
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
match last_digit:
    case 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    case x if (x < 6 and x != 0):
        print(f"Last digit of {number} is {last_digit}",
              "and is less than 6 and not 0")
    case x if x > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
