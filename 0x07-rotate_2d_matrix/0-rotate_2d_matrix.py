#!/usr/bin/python3
"""rotate matrix """


def rotate_2d_matrix(matrix) -> None:
    """rotate the given n * n matrix"""
    row = len(matrix) - 1
    temp = []
    for i in range(len(matrix)):
        temp.append(matrix[i].copy())

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = temp[row - j][i]
