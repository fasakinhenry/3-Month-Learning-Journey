#!/usr/bin/python3
if __name__ == "__main__":
    """Prints Argument counts and list of arguments"""
    from sys import argv
    num_args = len(argv) - 1
    print(f"{num_args}", "arguments" if num_args != 1 else "argument")
    for arg in range(1, len(argv)):
        print(f"{arg}: {argv[arg]}")

