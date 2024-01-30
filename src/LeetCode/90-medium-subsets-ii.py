# Given an integer array nums that may contain duplicates, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans: List[List[int]] = [[]]
        prev, prev_count = None, 0
        for num in nums:
            copy = ans.copy()
            if num == prev:
                ext = [e + [num] for e in copy[-prev_count:]]
            else:
                ext = [e + [num] for e in copy]
            prev, prev_count = num, len(ext)
            ans.extend(ext)
        return ans


solution = Solution()
print(solution.subsetsWithDup(nums=[1, 2, 2]))
