#!/usr/bin/python3
"""solution of prime game"""


def isWinner(x, nums):
    """function decide if Maria or Ben is wins"""
    win = {0: 0, 1: 0}
    prime_numbers = []
    if x < 0 or len(nums) < x or max(nums) < 1: 
        return None
    
    for role in range(x):
        current_player = 0
        prime = [False, False] + [True for i in range(2, nums[role] + 1)]
        for i in range(2, nums[role] + 1):
            if prime[i] == True:
                prime_numbers.append(i)
                for j in range(i * i, nums[role] + 1, i):
                    prime[j] = False
        for num in prime_numbers:
            prime_numbers.remove(num)
            current_player = 1 - current_player
        win[current_player] += 1
    return 'Maria' if win[0] > win[1] else 'Ben' if win[0] < win[1] else None
