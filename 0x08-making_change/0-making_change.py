#!/usr/bin/python3
"""make change problem"""


def makeChange(coins, total):
    """return the minumum coins to make the total"""
    n = len(coins) - 1
    coins.sort()
    ansList = []
    while n >= 0:
        while coins[n] <= total:
            total -= coins[n]
            ansList.append(coins[n])
        n -= 1
    return len(ansList) if total == 0 else -1
