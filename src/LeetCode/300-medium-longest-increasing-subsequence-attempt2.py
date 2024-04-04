from functools import lru_cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        ans = 1

        for i in range(len(nums) - 2, -1, -1):
            max_val = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_val = max(max_val, dp[j] + 1)
            dp[i] = max_val
            ans = max(ans, dp[i])
        return ans
