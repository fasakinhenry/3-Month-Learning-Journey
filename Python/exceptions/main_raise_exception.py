#!/usr/bin/python3
raise_exception = __import__('raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
