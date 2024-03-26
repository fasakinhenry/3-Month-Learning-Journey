#!/usr/bin/python3
# The sum of the two elements define the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
