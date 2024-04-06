#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result
    Args:
    a: The first integer
    b: The second integer """
    try:
        x = a / b
    except ZeroDivisionError:
        x = None
    finally:
        print("Inside result: {}".format(x))
        return x
