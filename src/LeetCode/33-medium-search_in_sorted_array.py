""" 33 MEDIUM Search in Sorted Array """

# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#  
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#  
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

"""
Time: O(log(n))
Space: O(1)

Tricks:
    - When search a sorted, but rotated array, find the min first. 
        This requires check mid-adjacent values for rotation point
    - To prevent integer overflow (not possible in python) - use mid = left + (right - left) // 2
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First, find the min/pivot in O(log(n))
        pivot = -1
        l, r = 0, len(nums)-1
        
        # Array is of length 1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        # Array not sorted, pivot at 0th index
        if nums[0] < nums[len(nums)-1]:
            pivot = 0

        while l <= r and pivot == -1:
            mid = l + (r - l) // 2 # prevents overflow, though that's not a problem in python
            if nums[mid-1] > nums[mid]:
                pivot = mid
                break
            elif nums[mid] > nums[mid + 1]:
                pivot = mid + 1
                break
            if nums[0] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        # Quick check to see if target is in the array
        if target < nums[pivot]:
            return -1
        
        # Second, search in the sorted range for the target
        if target <= nums[len(nums)-1]:
            # Target is r of pivot
            l, r = pivot, len(nums)-1
        else:
            # Target is l of pivot
            l, r = 0, pivot - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return l if nums[l] == target else -1

solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))
print(solution.search([4,5,6,7,0,1,2], 4))
print(solution.search([4,5,6,7,0,1,2], 7))
print(solution.search([4,5,6,7,0,1,2], 2))
print(solution.search([4,5,6,7,0,1,2], 3))
print(solution.search([0,1,2,3,4,5,6], 0))
print(solution.search([0,1,2,3,4,5,6], 3))
print(solution.search([0,1,2,3,4,5,6], 6))
print(solution.search([0,1,2,3,4,5,6], 7))
print(solution.search([0,1,2,3,4,5,6], -1))

