""" Delete all duplicate elements in a sorted array, shifting remaining elements left. 

    Seek an O(n) / O(1) solution
"""

"""
Idea:
    Two pointer technique. First pointer tracks index of unique elements. Second pointer finds next unique index.
    Following full array scan, slice the array to just those unique elements found and repositioned.

Time: O(n)
Space: O(1)
"""

from typing import List

def delete_duplicates(A: List[int]) -> List[int]:
    i = 0
    rp = i + 1
    while rp < len(A):
        while A[i] == A[rp] and rp < len(A):
            rp += 1
        A[i+1] = A[rp]
        i += 1
        rp += 1

    return A[:i+1]


print(delete_duplicates([2,3,5,5,6,6,6,7,11,11,11,13]))
