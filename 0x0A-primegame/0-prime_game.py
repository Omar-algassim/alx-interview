#!/usr/bin/python3
"""solution of prime game"""


def isWinner(x, nums):
    """function decide if Maria or Ben is wins"""
    win = {0: 0, 1: 0}
    prime_numbers = []
    current_player = 0
    if x < 0 or len(nums) < x or max(nums) < 1: 
        return None
    
    for role in range(x):
        prime = [False, False] + [True for i in range(2, nums[role] + 1)]
        for i in range(2, nums[role] + 1):
            if prime[i] == True:
                prime_numbers.append(i)
                for j in range(i * i, nums[role] + 1, i):
                    prime[j] = False
        i = 0
        while prime_numbers and i < len(prime_numbers):
            num = prime_numbers[i]
            prime_numbers.remove(num)
            current_player = 1 - current_player
            i += 1
        win[current_player] += 1
    return 'Maria' if win[0] > win[1] else 'Ben' if win[0] < win[1] else None

print(isWinner(5, [2, 5, 1, 4, 3]))