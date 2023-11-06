#!/usr/bin/python3
class MyList(list):
    """
    Sorts the list in ascending order and prints it.

    Parameters:
        self (list): The list to be sorted and printed.

    Returns:
        None
    """
    def print_sorted(self):
        list.sort(self)
