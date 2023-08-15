# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#  
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#  
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

'''
O(n) O(n):
    maintain a set of values seen, return true when value is seen again


'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set(nums)
        return len(seen) != len(nums)


solution: Solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
