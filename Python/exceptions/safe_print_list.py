#!/usr/bin/python3
# function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
        count = 0
        try:
            for element in range(x):
                print(my_list[element], end="")
                count += 1
        except IndexError:
            # Handle case where index is out of range
            pass
        # Print newline if all elements are printed
        print()
        return count
