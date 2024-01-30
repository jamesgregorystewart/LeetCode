# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

"""
Time: O(n*n!)
Space: O(n)

Time complexity is such because given a set of length n, the number of permutations is n!. There are n options for the first position, n-1 for the second, and so on.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm):
            if len(perm) == len(nums):
                results.append(perm[:])
                return
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm)
                    perm.pop()

        results: List[List[int]] = []
        backtrack([])
        return results


solution = Solution()
print(solution.permute(nums=[1, 2, 3]))
