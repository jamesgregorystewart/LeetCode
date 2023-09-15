""" Generate Nonuniform Random Numbers

Write a program which given an array of ints, and an array of corresponding probabilities, will return
a number form the array of ints based on the probabilities in the probabilities array"""

"""
Idea:
    - Consider the probabilities array to be ranges from [0.0, 1.0], where each range exists in this super range
        like p0,p0+p1,...,p0+...+pn-1 where each range corresponds to an index in the array of provide ints with
        which to return
    - Generate a float from [0.0,1.0] and return the int at the index that this range falls within. random.random
        generates a random float 0.0 <= x < 1.0.
    - Binary search for the index in probabilities corresponding to the generated number

Time: O(n)
Space: O(n)

"""

from bisect import bisect
from typing import List
from random import random
import itertools


def gen_nonuniform_random_number(values: List[int], probabilities: List[float]) -> int:
    probability_ranges = list(itertools.accumulate(probabilities)) # accumulate creates -> 
    probability_index = bisect(probability_ranges, random()) #random() generates a random float 0.0 <= x < 1.0
    return values[probability_index]

print(gen_nonuniform_random_number([3,5,7,1], [9/18,6/18,2/18,1/18]))
