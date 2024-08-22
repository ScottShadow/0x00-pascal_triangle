#!/usr/bin/python3

def makeChange(coins, total):
    print("===================================================================")
    print("makeChange function called with coins:", coins, "and total:", total)
    sum = total
    coins = sorted(coins, reverse=True)
    count = 0
    i = 0
    while sum > 0:
        print("Loop iteration:", count+1)
        print("Current sum:", sum)
        print("Current coin:", coins[i])
        if (sum - coins[i] > 0):
            count += 1
            print("Adding", coins[i], "to the count")
            sum -= coins[i]
        elif (sum - coins[i] <= 0):
            i += 1
            print("Incrementing the coin index to", i)
            if i > (len(coins)-1):
                print("Reached end of coins list. Breaking the loop.")
                print(
                    "===================================================================")
                return -1
    print("Final count:", count)
    print("===================================================================")
    return count
