#!/usr/bin/python3
"""islan perimeter problem"""


def island_perimeter(grid):
    """return the island perimeter"""
    islan_perimeter = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                islan_perimeter += 4
                if (i + 1) < row and grid[i + 1][j] == 1:
                    islan_perimeter -= 1
                if (i - 1) >= 0 and grid[i - 1][j] == 1:
                    islan_perimeter -= 1
                if (j + 1) < col and grid[i][j + 1] == 1:
                    islan_perimeter -= 1
                if (j - 1) >= 0 and grid[i][j - 1] == 1:
                    islan_perimeter -= 1
    return islan_perimeter
