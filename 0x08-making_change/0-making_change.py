#!/usr/bin/python3
"""mkaing change module"""

def makeChange(coins, total):
    """make change function"""
    if total <= 0:
        return 0
    n = len(coins) - 1
    coins.sort()
    ansList = []
    while n >= 0:
        while coins[n] <= total:
            total -= coins[n]
            ansList.append(coins[n])
        n -= 1
    return len(ansList) if total == 0 else -1
