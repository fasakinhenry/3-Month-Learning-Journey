#!/usr/bin/python3
if __name__ == "__main__":
    """A simple calculator
    It allows you to add, sub, mul and div
    It uses code from the module calculator_module
    If error, 1 is returned else 0
    It takes three more arguments in the argv
    usage: ./this_filename a operator b"""
    from sys import argv
    from calculator_module import add, sub, mul, div
    operators = ["+", "-", "*", "/"]
    if len(argv) !=  4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == "+":
            print(f"{a} + {b} = {add(a, b)}")
        elif operator == "-":
            print(f"{a} {operator} {b} = {sub(a, b)}")
        elif operator == "*":
            print(f"{a} {operator} {b} = {mul(a, b)}")
        elif operator == "/":
            print(f"{a} {operator} {b} = {div(a, b)}")
    

