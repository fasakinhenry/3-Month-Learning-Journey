#!/usr/bin/python3
# Print the different combination of 2digit numbers
# The two digits must be different
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", "
              if i != 8 or j != 9 else "\n")
