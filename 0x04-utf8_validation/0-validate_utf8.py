#!/usr/bin/python3
"""utf-8 valdiation"""
from typing import List


def to_binary(num: int) -> list:
    """convert number to binary"""
    ret = ""
    for x in range(8):
        ret += (str(num % 2))
        num = num // 2
    return ret[::-1]

def validUTF8(data: List[int]) -> bool:
    """test if the number is valid to utf-8"""
    patterns = {
        1: ['0'],
        2: ['110', '10'],
        3: ['1110', '10', '10'],
        4: ['11110', '10', '10', '10']
    }
    conv_num = []
    length = len(data)
    size = 1
    count = 0
    for num in data:
        conv_num.append(to_binary(num))
    while count < len(conv_num):
        for byte, pattern in patterns.items():
            if conv_num[count].startswith(pattern[0]):
                size = byte
        char = conv_num[count:size + count]
        if len(char) < size:
            return False
        for pat, binary in zip(patterns[size], char):
            if not binary.startswith(pat):
                return False
        count += size
    return True
