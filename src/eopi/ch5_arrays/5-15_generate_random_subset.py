""" Generate Random Subset

Write a program that takes as input a positive integer n and size k <= n and returns a size-k subset of {0,1,2,...,n-1}.
"""

"""
Idea:
    1) Generate a sample population of 0 -> n-1
    2) Create the sample of size k

Time: O(n)
Space: O(n) probably

Trick:
    - Knowing that you can create a random permutation of size k from a population using random.sample.
"""

from typing import List
from random import sample

def generate_random_subset(n: int, k: int) -> List[int]:
    population = list(range(n))
    return sample(population, k)

print(generate_random_subset(5, 3))
