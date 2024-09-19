#!/usr/bin/python3
"""make change problem"""


def makeChange(coins, total):
    """return the minumum coins to make the total"""
    length = len(coins) - 1
    coins.sort()
    ans_list = []
    while length >= 0:
        while coins[length] <= total:
            total -= coins[length]
            ans_list.append(coins[length])
        length -= 1
    return len(ans_list) if total == 0 else -1
