#!/usr/bin/python3
# Find if the status of the number from 2 to 10 is odd/even
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    else:
        print("Found an odd number", num)

# Printing using another approach can come in handy

print("\nPrint using the continue statement\n")
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
