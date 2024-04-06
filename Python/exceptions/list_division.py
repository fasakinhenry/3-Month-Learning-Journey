#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element in 2 lists
    Args:
    my_list_1 (list): The first list
    my_list_2 (list): The second list
    list_integer (int): The length of the list to be printed"""
    # store the value of each division in x
    x = 0
    final_list = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
            final_list.append(x)
        except TypeError:
            x = "wrong type"
            final_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            final_list.append(0)
        except IndexError:
            print("out of range")
            final_list.append(0)
        finally:
            pass
    return final_list
