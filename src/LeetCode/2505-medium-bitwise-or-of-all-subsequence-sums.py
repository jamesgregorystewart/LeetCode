import functools
from typing import List


class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans |= sum | nums[i]
        return ans
