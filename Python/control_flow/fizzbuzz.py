#!/usr/bin/python3
''' Fizz buzz challenge in Python
For multiples of 3 Print Fizz, 5 print Buzz
for multiples of 3 and 5 print fizzbuzz
'''
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
