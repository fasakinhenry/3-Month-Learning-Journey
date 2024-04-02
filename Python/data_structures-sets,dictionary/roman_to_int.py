#!/usr/bin/python3
"""
Converts Roman Numerals into integers
"""
def roman_to_int(roman_string):
    # Validate roman numeral string
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    # Use a dict to store each representation of numerals
    numeral_table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    # store previous values for cases like IV
    previous_value = 0
    # Store the value of the result
    result = 0
    # for loop to loop through roman_string to get each character
    for numeral in range(len(roman_string)):
        if roman_string[numeral] not in numeral_table:
            return 0
        value = numeral_table[roman_string[numeral]]
        # Check if next numeral exists and has greater value
        if numeral + 1 < len(roman_string) and numeral_table[roman_string[numeral + 1]] > value:
            result -= value
        else:
            result += value
    # Return the value of the result
    return result
