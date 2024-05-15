from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        max_seen = -1
        for num in nums:
            if -num in seen:
                max_seen = max(max_seen, abs(num))
            seen.add(num)

        return max_seen
