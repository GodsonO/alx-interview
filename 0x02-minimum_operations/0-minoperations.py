#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    minoperations = 2
    while n > 1:
        while n % minoperations == 0:
            operations += minoperations
            n /= minoperations
        minoperations += 1
    return operations
