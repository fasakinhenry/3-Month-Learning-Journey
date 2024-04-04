#!/usr/bin/python3
# Deletes keys with a specific value in a dict
def complex_delete(a_dictionary, value):
    # If dictionary is empty return the original dictionary
    if a_dictionary == {}:
        return a_dictionary

    # Create a new list to store the keys to be deleted
    keys_list = []

    # Use unpacking to get the key and respective values in item
    # Also use a for loop to loop through each pair
    for key, val in a_dictionary.items():
        # If the value of the key matches specified value
        if val == value:
            keys_list.append(key)
    # Iterate through each key to del & remove them from dict
    for keys in keys_list:
        # delete all the keys
        del a_dictionary[keys]

    return a_dictionary
