from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        left = count = 0
        right = -1
        n = len(nums)
        result = 0
        while right < n:
            if count < k:
                right += 1
                count = count + 1 if right < n and nums[right] == max_val else count
            else:
                result += n - right
                if nums[left] == max_val:
                    count -= 1
                left += 1
        return result
