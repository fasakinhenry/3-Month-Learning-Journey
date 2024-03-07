#!/usr/bin/python3
from datetime import datetime
name = "Henry"
age = 25

# Using f-strings to print values
print(f"Hello {name}, you are {age} years old")

# Using methods in f string
print(f"Hello {name.upper()}, you are {age} years old")

# Using embedded list comprehension in f string
print(f"{[2**n for n in range(3, 9)]}")

balance = 5425.9256

# Using f-strings with format specifiers(float)
print(f"Balance: {balance:.2f}")

heading = "Centered user"

# Using f-strings with format specifiers(string)
print(f"{heading:=^30}")

# Elaborate examples on using f-strings with different format specifiers
integer = -123456789
print(f"Comma as thousand seperators: {integer:,}")

seperator = "_"
print(f"Using custom seperator: {integer:{seperator}}")

floating_point = 1234567.8912
print(f"Comma as thousand seperator and two decimals: {floating_point:,.2f}")

date = (3, 7, 2024)
print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")

# Using the datetime with f-string
date = datetime(2023, 9, 26)
print(f"{date:%m/%d/%Y}")

# Using f-string to print self documented expressions
variable = "Some value"
print(f"{variable = }")
