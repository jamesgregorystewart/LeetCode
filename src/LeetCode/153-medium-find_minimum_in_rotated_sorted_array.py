""" 153 MEDIUM Find Minimum in Rotated Sorted Array """

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
#  
#
# Example 1:
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
#  
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.

"""
Time: O(logn)
Space: O(1)
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r] or (r != mid and nums[mid + 1] < nums[mid]):
                l = mid + 1
            elif nums[mid] > nums[l] or (l != mid and nums[mid - 1] < nums[mid]):
                r = mid - 1
            else:
                if l != mid != r and nums[mid -1] > nums[mid] and nums[mid + 1] > nums[mid]:
                    return nums[mid]
                break
        return nums[l]


solution = Solution()
print(solution.findMin([3,4,5,1,2]))
print(solution.findMin([4,5,6,7,0,1,2]))
print(solution.findMin([11,13,15,17]))
print(solution.findMin([0,1,2,3,4,5,6,7,8]))
print(solution.findMin([3,1,2]))
print(solution.findMin([5,1,2,3,4]))
