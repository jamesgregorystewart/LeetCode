from typing import List

"""
1584 76531

i = 4

"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        def reverse(start, end, nums) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        boundary = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                boundary = i + 1
                for j in range(len(nums) - 1, -1, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        reverse(boundary, len(nums) - 1, nums)
                        return

        reverse(0, len(nums) - 1, nums)
