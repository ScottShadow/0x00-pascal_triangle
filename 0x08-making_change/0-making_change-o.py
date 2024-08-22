#!/usr/bin/python3
"""
makeChange module
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    sum = total
    coins = sorted(coins, reverse=True)
    count = 0
    i = 0
    while sum > 0:
        if i > (len(coins)-1):
            return -1

        if (sum - coins[i] >= 0):
            count += 1
            sum -= coins[i]
        else:
            i += 1

    return count
