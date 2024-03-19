from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start, prefix_zeros, sum, subarrays = 0, 0, 0, 0
        for end, num in enumerate(nums):
            sum += num

            while start < end and (nums[start] == 0 or sum > goal):
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1

                sum -= nums[start]
                start += 1

            if sum == goal:
                subarrays += 1 + prefix_zeros

        return subarrays
