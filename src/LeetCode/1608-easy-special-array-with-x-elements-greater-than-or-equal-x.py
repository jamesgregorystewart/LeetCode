from typing import List


"""
3 5 7 9 

3 5
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        N = len(nums)
        for i, num in enumerate(nums):
            x = N - i
            if num >= x and ((i > 0 and nums[i - 1] < x) or i == 0):
                return x
        return -1
