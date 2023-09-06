"""
Write a program that takes an array A and an index i into A and rearranges A such that all elements less
than A[i] precede it, followed by all elements equal to A[i], and finally elements greater than A[i].
A[i] will be known here as the "pivot".

Elements smaller than the pivot do not need to be sorted in their respective range, nor do those greater.
"""

from typing import List

def sort(a: List[int], pivot: int) -> List[int]:
    return sorted(a)

a = [0,1,2,0,2,1,1]
print(sort(a, 2))
