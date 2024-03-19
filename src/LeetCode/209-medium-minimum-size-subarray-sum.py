from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        sum = nums[0]
        min_length = float("inf")
        while r < len(nums):
            if sum >= target:
                min_length = min(min_length, r - l + 1)
                sum -= nums[l]
                l += 1
            else:
                if r == len(nums) - 1:
                    break
                r += 1
                sum += nums[r]

        return min_length if min_length != float("inf") else 0
