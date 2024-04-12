from typing import List

"""
 2 3 2   i = 0
 
"""


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sum = 0
        for i, num in enumerate(tickets):
            if i <= k:
                sum += min(num, tickets[k])
            else:
                sum += min(num, tickets[k] - 1)

        return sum
