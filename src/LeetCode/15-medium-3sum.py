""" 3Sum """

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#  
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#  
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

"""
Idea:
    - Double for loop on sorted input with O(1) lookup into complements dict
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,complements = [], {}

        # First sort in O(nlog(n))
        nums.sort()

        # Do some input trimming to get rid of impossible solutions
        l,r = 0, len(nums)-1
        while nums[l] + nums[r] + nums[r] < 0 and l < r + 1:
            l += 1
        while nums[l] + nums[l+1] + nums[r] > 0 and l < r + 1:
            r -= 1

        # Create dict of complements in O(n), creating O(n) space utilization
        for i, num in enumerate(nums):
            if num in complements.keys():
                complements[num].append(i)
            else:
                complements[num] = [i]
        
        # Two Pointer Technique 
        for front in range(l, r):
            if front < len(nums)-1 and nums[front] == nums[front+1]:
                continue
            for back in range(r, front, -1):
                if back > 1 and nums[back] == nums[back-1]:
                    continue
                two_sum = nums[front] + nums[back]
                if 0 - two_sum in complements.keys():
                    for i in complements[0-two_sum]:
                        if i != front and i != back and sorted([nums[front], 0-two_sum, nums[back]]) not in [sorted(ans) for ans in res]:
                            res.append([nums[front],0-two_sum,nums[back]])
                            break

        return res


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,1,1]))
print(solution.threeSum([0,0,0]))
print(solution.threeSum([-2,0,1,1,2]))
print(solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
