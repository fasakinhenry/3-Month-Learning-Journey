#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x = 0):
    """Prints the first x elements of a list an only integers
    Args:
    my_list (list): The list of elements to print from
    x (int): The number of elements of my_list to print
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except:
            pass
    print()
    return count
