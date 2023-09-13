# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#  
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

"""
Idea: Use Set to check if next number greater than num exists in O(1). Don't scan backwards to maintain O(n) linear time. 

Time: O(n) -- O(n + n) to be precise
Space: O(n) -- from the set that we use for O(1) lookup

Trick:
    - Using set for O(1) lookup instead of iterating through array
    - Using a less than check to make sure that we are not in the middle of a sequence, so we only scan in increasing order once
        per consecutive sequence.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_consecutive_sequence = 1
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                consecutive_sequence = 1
                current_num = num
                while current_num+1 in nums_set:
                    consecutive_sequence += 1
                    current_num += 1
                    longest_consecutive_sequence = max(longest_consecutive_sequence, consecutive_sequence)

        return longest_consecutive_sequence

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
