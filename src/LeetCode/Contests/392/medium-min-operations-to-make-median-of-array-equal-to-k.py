from typing import List
import math


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        operations = 0
        m = n // 2
        for i, x in enumerate(nums):
            if i < m and nums[i] > k:
                operations += nums[i] - k
            if i == m and nums[i] != k:
                operations += abs(nums[i] - k)
            if i > m and nums[i] < k:
                operations += k - nums[i]
        return operations


solution = Solution()
print(solution.minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=4))
print(solution.minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=7))
print(solution.minOperationsToMakeMedianK(nums=[1, 2, 3, 4, 5, 6], k=4))
print(solution.minOperationsToMakeMedianK(nums=[1], k=10))
