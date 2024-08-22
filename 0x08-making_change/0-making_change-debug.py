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
    coins.sort(reverse=True)
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


def makeChange2(coins, total):
    """
    my own version of makechange
    """
    coins = list(set(coins))
    if not coins:
        return -1
    coins = [i for i in coins if i != 0]
    if (not isinstance(coins, list) and not all(isinstance(i, (int, float)) for i in coins)):
        return -1
    for coin in coins:
        if not isinstance(coin, (float, int)) or coin <= 0:
            return -1
    if total <= 0:
        return 0
    my_sum = total
    count = 0
    coins.sort(reverse=True)

    def makeChangeHelper(coins, my_sum, count):
        """
        an attempt at backtracking
        """
        last_coin = 0
        if not coins:
            return -1

        my_sum -= coins[0]
        last_coin = coins[0]
        count += 1

        if my_sum == 0:
            return count

        if my_sum > 0:
            result = makeChangeHelper(coins, my_sum, count)
            if result != -1:
                return result

        my_sum = my_sum + last_coin

        if len(coins) > 1:
            coins = coins[1:]
        else:
            return -1

        count = count - 1

        result = makeChangeHelper(coins, my_sum, count)
        return result
    return makeChangeHelper(coins, my_sum, count)
