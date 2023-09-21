""" Two Sum II - Input Array is Sorted """

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
#  
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#

"""
Idea:
    - move one pointer from left to right, doing a binary search for its complement in log(n)

Time: O(nlog(n))
Space: O(1)
"""

from bisect import *
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr = 0
        while ptr < len(numbers):
            complement_ptr = bisect_left(numbers, target - numbers[ptr])
            if ptr == complement_ptr:
                complement_ptr += 1
            if complement_ptr < len(numbers) and numbers[complement_ptr] == target - numbers[ptr]:
                return [ptr+1, complement_ptr+1]
            ptr += 1

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
print(solution.twoSum([-1, 0], -1))
print(solution.twoSum([0,0,3,4], 0))
print(solution.twoSum([5, 25, 75], 100))

