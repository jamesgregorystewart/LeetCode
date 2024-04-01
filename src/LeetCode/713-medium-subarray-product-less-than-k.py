from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product, totalCount = 1, 0
        left = 0
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[left]
                left += 1
            totalCount += right - left + 1
        return totalCount
