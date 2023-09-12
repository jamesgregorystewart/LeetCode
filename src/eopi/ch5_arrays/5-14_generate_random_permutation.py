""" Generate Random Permutation

Given an integer n, generate a random permutation of the form {0,1,2,3,...,n-1}
"""

"""
Idea:
    1) Maintain a list of values yet to be used in the resultant permutation
    2) generate a random number which is actually an index into the list of unused values
    3) append the value into the resultant array; and move the end element into the used element's position,
        finally deleting the tail element

Time: O(n)
Space: O(n)

Tricks:
    - list(range(n)) returns a list of incrementing values
    - random.sample(list_name, size) returns a sample (permutation) of a population at provided size
"""

from typing import List
from random import randrange, sample

def generate_permutation(n: int) -> List[int]:
    unused = list(range(n))
    res = []

    while len(unused) > 0:
        r = randrange(len(unused))
        res.append(unused[r])
        unused[r] = unused[len(unused)-1]
        del unused[len(unused)-1]

    return res

print(generate_permutation(3))

print(sample(list(range(3)), 3))
