""" Write a program that returns the max profit if you bought and sold a stock once given the opening price for N days"""

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
