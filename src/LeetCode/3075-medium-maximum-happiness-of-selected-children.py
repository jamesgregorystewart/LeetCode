from typing import List
import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiest = heapq.nlargest(k, happiness)

        # happiest.sort(reverse=True)
        offset = 0
        ans = 0
        for child in happiest:
            ans += max(child - offset, 0)
            offset += 1
        return ans
