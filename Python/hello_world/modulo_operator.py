#!/usr/bin/python3
name = "Henry"
age = 25

# Printing one value
print("Hello %s" % name)

# Printing one values using tuples
print("Hello %s! You are %s years old" % (name, age))

# printing multiple values using dictionaries
print("Hello %(name)s! You are %(age)s years old" % {"name": "Henry", "age": 25})

# printing values using specific formats(float numbers)
print("Balance: %.2f" % 54.2876)

# printing specific values using specific format(strings)
print("Name: %s\nAge: %5s" % (name, age))