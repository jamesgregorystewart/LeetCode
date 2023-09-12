""" Sample Offline Data 

Given an array of integers, and an integer k, return a random subset of A of size k. All possible samples should
be equally likely.
"""

""" Idea:
    Generate a random number [i, k]. Swapping A[i] and A[swap].
    Return A[:k]

Time: O(k)
Space: O(1)

"""

from typing import List
from random import randrange

def generate_sample_data(A: List[int], k: int) -> List[int]:
    for i in range(k):
        swap = randrange(i,len(A))
        A[swap], A[i] = A[i], A[swap]
    return A[:k]


print(generate_sample_data([3,7,5,11], 3))

