from typing import List
import collections


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = collections.defaultdict(int)
        ans = 0
        left, right = 0, 0
        while right < len(nums):
            counts[nums[right]] += 1
            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
