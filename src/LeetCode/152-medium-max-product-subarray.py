# Given an integer array nums, find a
# subarray
#  that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

from typing import List


# O(N^2) Solution
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         product = max_product = nums[0]
#         for i in range(len(nums)):
#             product = nums[i]
#             max_product = max(max_product, product)
#             for j in range(i + 1, len(nums)):
#                 product *= nums[j]
#                 max_product = max(max_product, product)
#
#         return max_product


# O(N) Solution
"""
This implementation is a highly modified version of Kadane's Algorithm
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_seg = nums[0]
        min_seg = nums[0]
        result = max_seg

        for i in range(1, len(nums)):
            curr = nums[i]
            # forcefully reset to 0 when encountered
            temp_max = max(curr, max_seg * curr, min_seg * curr)
            min_seg = min(curr, max_seg * curr, min_seg * curr)

            # max_seg is used in both previous computations, so assign it here
            max_seg = temp_max

            # result will make sure previous max segments are retained
            result = max(max_seg, result)

        return result


solution = Solution()
print(solution.maxProduct(nums=[2, 3, -2, 4]))
print(solution.maxProduct(nums=[2, 3, -2, 4]))
