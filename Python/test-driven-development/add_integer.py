#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns the integer addtion of a and b

    Float arguments are typecasted to int before addition is performed
    
    Raises:
        TypeError if a or b is a non-integer or non-float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
