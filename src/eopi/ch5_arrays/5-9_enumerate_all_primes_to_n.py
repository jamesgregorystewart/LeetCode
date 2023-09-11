""" Enumerate all Primes to n

Write a program that given an integer n, returns an array of all primes less than or equal to n

"""

"""
Idea:
    Use a boolean array to determine whether an integer is a prime or not. Initialize array with all indices True,
    except for 0 and 1. If element at index is True, then add to list of primes, and Falsify all its multiples up to 
    and including n. 

Time: O(nlogn)
Space: O(n)

Possible optimizations:
    - Only check odd numbers
    - falsification can increment by 2i+i
"""

from typing import List

def enumerate_primes(n: int) -> List[int]:
    primes = []
    is_prime = [False, False] + [True] * (n-1)

    if n < 2:
        return []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return primes


print(enumerate_primes(121))
