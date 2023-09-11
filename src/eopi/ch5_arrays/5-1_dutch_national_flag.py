"""
Write a program that takes an array A and an index i into A and rearranges A such that all elements less
than A[i] precede it, followed by all elements equal to A[i], and finally elements greater than A[i].
A[i] will be known here as the "pivot".

Elements smaller than the pivot do not need to be sorted in their respective range, nor do those greater.
"""

""" Idea:
    Manage sections of array which are less than, equal to, or greater than the pivot. The equal to section
    will serve as that unclassified set. Move items less than or greater than to the far end of the array.

"""

from typing import List

def dutch_flag_sort(A: List[int], p: int) -> List[int]:
    pivot = A[p] 
    smaller, equal, larger = 0, 0, len(A) - 1

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            # A[equal] > pivot
            A[equal], A[larger] = A[larger], A[equal]
            larger -= 1
    return A 

a = [0,1,2,0,2,1,1]
print(dutch_flag_sort(a, 2))
b = [0,1,2,0,2,1,1]
print(dutch_flag_sort(b, 5))
