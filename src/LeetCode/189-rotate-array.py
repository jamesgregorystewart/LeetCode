# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
#
#
# Follow up:
#
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

"""
Idea is that we will circularly replace each character, storing the replaced character in temp, and when we have gone in a full circle
and end up back at the beginning (if before we are done doing replacements) then we will increment i by one and do another loop
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k == 0 or k == n:
            return
        k %= n
        i = starting_index = 0
        temp = nums[0]
        for iteration in range(n):
            temp, nums[(i + k) % n] = nums[(i + k) % n], temp
            i = (i + k) % n
            if iteration == n - 1:
                break
            if i == starting_index:
                starting_index += 1
                temp, i = nums[starting_index], starting_index


solution = Solution()
print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))
