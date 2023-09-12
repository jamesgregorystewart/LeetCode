""" Making an Alternation
Given an Array A, return an array B, such that B[0] <= B[1] >= B[2] <= B[3] >= B[4] ...

"""

""" 
Idea:
    1) Sort
    2) Arrange as: A[0], A[2], A[1], A[3], A[5], A[4], A[6], A[8], A[7]

Time: O(nlog(n))
Space: O(1)
"""

from typing import List
from math import ceil

def make_it_alternate(A: List[int]) -> List[int]:
    B = [None] * ((len(A) // 2) * 2)
    A.sort() # nlog(n) operation
    for i in range(0, len(A), 2):
        try:
            B[i], B[i+1] = A[i//2], A[ceil(len(A)/2) + (i//2)] 
        except:
            break
    return B


A = [0,1,2,3,4,5,6]
B = make_it_alternate(A)
print(B)


"""
Idea:
    Localized approach. iterate through array, sorting each two adjacent elements in ascending, then descending order
    Alternating on each iteration (i % 2)

Trick:
    Noticing that you can locally rearrange each pair of elements in asc/desc order.

Time: O(n)
Space: O(1)
"""

from typing import List

def rearrange(A: List[int]) -> None:
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=bool(i%2))

C = [0,1,2,3,4,5,6]
rearrange(C)
print(C)
