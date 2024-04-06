#!/usr/bin/python3
# Prints an integer with the "{:d}".format()
def safe_print_integer(value):
    """ Print an integer with "{:d}".format().
    Args:
        value (int): The integer to be print
    Returns:
        if a TypeError or ValueError occurs - False
        Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
