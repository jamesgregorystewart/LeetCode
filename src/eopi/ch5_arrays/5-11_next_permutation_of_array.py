""" Next Permutation of Array 

Given an Array, return the next permutation in lexicographical order.

"""


"""
Idea:
    1) identify right-most index where A[i] < A[i+1]
    2) swap A[i] with smallest element greater tthan A[i] in range [i, len(A)]
    3) sort subarray A[i+1:]

"""

from typing import List

def next_permutation(A: List[int]) -> None:
    swap_index, replacement, replacement_index = -1, float('inf'), -1
    # Find the swap index
    for i in range(len(A)-1, 0, -1):
        if A[i-1] < A[i]:
            swap_index = i-1
            break

    print(swap_index)

    # Find replacement
    for i in range(len(A)-1, swap_index, -1):
        if A[i] > A[swap_index]:
            if A[i] < replacement:
                replacement = A[i]
                replacement_index = i
    print(replacement_index)

    # Perform replacement
    A[swap_index], A[replacement_index] = A[replacement_index], A[swap_index]
    print(A)
    
    # Sort the subarray remaining
    A = A[:swap_index+1] + sorted(A[swap_index+1:])

    return [] if swap_index == -1 else A

print(next_permutation([1,3,2,1]))
