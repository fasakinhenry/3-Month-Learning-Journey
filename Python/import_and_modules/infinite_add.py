#!/usr/bin/python3
if __name__ == "__main__":
    """Infinitely adds the number passed to the script call"""
    from sys import argv
    running_sum = 0
    for arg in range(1, len(argv)):
        running_sum += int(argv[arg])
    print(f"{running_sum}")
