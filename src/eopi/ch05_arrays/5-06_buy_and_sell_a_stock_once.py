""" Buy and Sell a Stock Once 
Write a program that returns the max profit if you bought and sold a stock once given the opening price for N days

"""

"""
Idea:
    Two pointer technique. Move left and right pointers from left to right, tracking the max difference between them.
    If right pointer value is less than left pointer value, move left pointer to right pointer, and increment right pointer.
    Else iterate right pointer.

Time: O(n)
Space: O(1)

"""

from typing import List

def get_max_profit(A: List[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r < len(A):
        max_profit = max(max_profit, A[r] - A[l])
        if A[l] > A[r]:
            l, r = r, r + 1
        else:
            r += 1
         
    return max_profit

print(get_max_profit([1,2,3,4]))
print(get_max_profit([1,10,2,4,6,4,2,3,6,8]))
print(get_max_profit([310,315,275,295,260,270,290,230,255,250]))
