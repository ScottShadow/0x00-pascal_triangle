#!/usr/bin/python3
"""
    This module contains a function to calculate the minimum number
    of operations required to reach a certain number of characters.
"""


def minOperations(n: int) -> int:
    """
        This function calculates the minimum number of operations required
        to reach a certain number of characters.
    Args:
        n (int): The number of characters to reach.
    Returns:
        int: The minimum number of operations required to reach the number
        of characters.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    string = 1
    tempstring = 0
    copyall = 0
    paste = 0
    while string < n:
        if n % string == 0:
            tempstring = string
            copyall += 1

        string = string + tempstring
        paste += 1
    return paste + copyall
