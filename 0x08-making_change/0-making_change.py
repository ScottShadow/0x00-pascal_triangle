#!/usr/bin/python3
"""
Change comes from within
Before Creation ...
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    dp = [0] + [float("inf")] * (total)
    dp[0] = 0
    for coin in coins:
        if coin < 0:
            continue
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
