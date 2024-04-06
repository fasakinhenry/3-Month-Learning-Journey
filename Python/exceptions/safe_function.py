#!/usr/bin/python3
# Import system module to print to standard error
import sys
def safe_function(fct, *args):
    # executes a function safely
    try:
        result = fct(*args)
        return result
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
