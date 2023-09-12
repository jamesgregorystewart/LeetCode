""" Permute the Elements of an Array 

Given an array and a permutation, apply the permutation to the array.
"""

"""
Idea: Try and use no additional memory... Apply each permutation to the permutation array itself. And encode those 
completed permutations into the permutation array with a -1 codifying it has been done.

Time: O(n)
Space: O(1)

"""

from typing import List

def permute_array(A: List[str], P: List[int]) -> None:
    i = 0
    while i < len(P):
        if i == P[i] or P[i] == -1:
            i += 1
        else:
            A[P[i]], A[i] = A[i], A[P[i]]
            P[i], P[P[i]] = P[P[i]], -1

A = ['a','b','c','d']
P = [2,0,1,3]

permute_array(A, P)
print(A)
