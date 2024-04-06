from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_val, min_val = max(nums), min(nums)
        buckets = [False] * (max_val - min_val + 1)

        for num in nums:
            buckets[num - min_val] = True

        prev = max_val - min_val
        max_gap = 0
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                max_gap = max(max_gap, prev - i)
                prev = i
        return max_gap
