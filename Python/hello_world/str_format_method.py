#!/usr/bin/python3
name = "Henry"
age = 25

# Print and interpolate strings using the str.format method
print("Hello {}!, You are {} years old".format(name, age))

# Interpoloate string using the str.format method and also specifiy order
print("Hello {1}, You are {0} years old".format(age, name))

# Interpolating strings using replacement fields and the str.format method
print("Hello {name}, you are {age} years old".format(name="Henry", age=25))

person = {"name": "Henry", "age": 25}

# Interpolate strings using the str.format method and keyword arguments
print("Hello {name}, you are {age} years old".format(**person))

# Using str.format method with format specifiers(float)
print("Balance: {:.2f}".format(54.2967))

# Using str.format method with str.format method(strings)
print("{:=^30}".format("centered string"))