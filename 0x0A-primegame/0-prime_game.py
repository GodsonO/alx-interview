#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive"""
    primeNums = []
    filters = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filters[prime]):
            primeNums.append(prime)
            for i in range(prime, n + 1, prime):
                filters[i] = False
    return primeNums


def isWinner(x, nums):
    """Determines winner of Prime Game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNums = primeNumbers(nums[i])
        if len(primeNums) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
