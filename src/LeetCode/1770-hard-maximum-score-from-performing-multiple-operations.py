# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.
#
# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:
#
# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
# Remove x from nums.
# Return the maximum score after performing m operations.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# Example 2:
#
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
#
#
# Constraints:
#
# n == nums.length
# m == multipliers.length
# 1 <= m <= 300
# m <= n <= 105
# -1000 <= nums[i], multipliers[i] <= 1000

"""
TAKEAWAYS

This is a great example of a problem that is easy to solve top-down, and more difficult as bottom-up

Converting to Bottom up requires the derivation of a state variable 'r', and the tricky
iterative looping through the states which is difficult to fully understand.
"""

from re import A
from typing import List


# Bottom Up Solution
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp: List[List[int]] = [
            [0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)
        ]

        for i in range(len(multipliers) - 1, -1, -1):
            # we iterate through all possible states, starting with scenario of using all left hand nums first
            # if we have used all left hand nums, then right hand num would point to last element in nums
            for l in range(i, -1, -1):
                # we reduce number of states by deriving 'r' from l and i
                r = len(nums) - 1 - i + l
                dp[i][l] = max(
                    nums[l] * multipliers[i] + dp[i + 1][l + 1],
                    nums[r] * multipliers[i] + dp[i + 1][l],
                )
        return dp[0][0]


from functools import lru_cache


# Top Down approach with memoization
# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         @lru_cache(None)
#         def dp(l: int, r: int, m: int) -> int:
#             if m == len(multipliers):
#                 return 0
#             return max(
#                 dp(l + 1, r, m + 1) + nums[l] * multipliers[m],
#                 dp(l, r - 1, m + 1) + nums[r] * multipliers[m],
#             )
#
#         return dp(0, len(nums) - 1, 0)


solution = Solution()
print(solution.maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
print(
    solution.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6])
)
