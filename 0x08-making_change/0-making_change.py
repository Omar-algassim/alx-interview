#!/usr/bin/python3
"""make change problem"""


def makeChange(coins, total):
    """return the minumum coins to make the total"""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    length = len(coins) - 1
    coins.sort()
    change = 0
    while length >= 0:
        while coins[length] <= total:
            total -= coins[length]
            change += 1
        length -= 1
    return change if total == 0 else -1
