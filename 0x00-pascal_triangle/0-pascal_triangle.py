#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists
    of integers representing the Pascal's triangle of n
    """
    p_triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            x = 1
            for j in range(1, i + 1):
                row.append(x)
                x = x * (i - j) // j
            p_triangle.append(row)
    return p_triangle
