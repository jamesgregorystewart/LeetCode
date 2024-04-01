from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        left, right, saved = 0, -1, -1
        n = len(nums)
        result = 0
        while right < n:
            if len(counts) < k:
                right += 1
                if right == n:
                    break
                counts[nums[right]] += 1
            else:
                saved = right
                result += 1
                # try moving forward and see how many we can add
                while right < n - 1 and nums[right + 1] in counts:
                    right += 1
                    result += 1
                right = saved
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1
        return result
