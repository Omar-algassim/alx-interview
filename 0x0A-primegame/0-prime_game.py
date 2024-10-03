#!/usr/bin/python3
"""solution of prime game"""


def isWinner(x, nums):
    """function decide if Maria or Ben is wins"""
    win = {'maria': 0, 'ben': 0}
    if x < 0 or len(nums) < x or max(nums) < 1:
        return None

    for round in range(x):
        prime_numbers = []
        current_player = 0
        prime = [False, False] + [True for i in range(2, nums[round] + 1)]
        for i in range(2, nums[round] + 1):
            if prime[i] is True:
                prime_numbers.append(i)
                for j in range(i * i, nums[round] + 1, i):
                    prime[j] = False
        for _ in prime_numbers:
            current_player = 1 - current_player
        win['maria' if current_player == 1 else 'ben'] += 1
    return 'Maria' if win['maria'] > win['ben'] else 'Ben'
