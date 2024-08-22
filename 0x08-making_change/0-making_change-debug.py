#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    try:
        dp = [0] + [float("inf")] * (total)
        print(f"{dp}\n")
        for coin in coins:
            print(f"i in ({coin}, {total})")
            if coin < 0:
                return -1
            for i in range(coin, total + 1):

                print(f"dp[{i}] = min(dp[{i}], dp[{i - coin}] + 1)")
                print(
                    f"-{dp[i]}-------{dp[i]}----{dp[i-coin]+1}---------------------")
                dp[i] = min(dp[i], dp[i - coin] + 1)
                print(f"{dp}\n")
            print("-" * 20)
            print(f"{dp}\n")
    except IndexError:
        return -1
    return dp[-1] if dp[-1] != float("inf") else -1
