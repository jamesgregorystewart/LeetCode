from typing import List
from collections import defaultdict


# O(n^2) / O(1)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        n = len(nums)
        for left in range(n):
            cur = 0
            for right in range(left, n):
                cur |= nums[right]
                if cur >= k:
                    ans = min(ans, right - left + 1)
                    break
        return ans if ans != float("inf") else -1
