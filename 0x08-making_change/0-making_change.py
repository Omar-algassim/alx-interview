#!/usr/bin/python3
"""make change problem"""


def makeChange(coins, total):
    """return the minumum coins to make the total"""
    memo = {}

    def dp(temp_amount):
        """decide if the amount can be made with the coins"""
        if temp_amount == 0:
            return 0
        if temp_amount < 0:
            return -1
        if temp_amount in memo:
            return memo[temp_amount]

        min_coins = float('inf')

        for coin in coins:
            result = dp(temp_amount - coin)
            if result >= 0:
                min_coins = min(min_coins, result + 1)

        memo[temp_amount] = min_coins if min_coins != float('inf') else -1
        return memo[temp_amount]
    return dp(total)
