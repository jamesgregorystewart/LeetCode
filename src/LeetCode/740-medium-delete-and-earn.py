# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.
#
#
#
# Example 1:
#
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:
#
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104


from typing import List
from collections import Counter


# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#
#         counts = Counter(nums)
#
#         max_val = max(nums)
#         dp: List[int] = [0] * (max_val + 1)
#
#         dp[1] = counts[1] if 1 in counts else 0
#
#         for i in range(2, max_val + 1):
#             dp[i] = max(dp[i-2] + (counts[i] * i), dp[i-1])
#         return dp[max_val]


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        counter = Counter(nums)
        max_val = max(nums)
        dp = [0] * (max_val + 3)
        for i in range(max_val, 0, -1):
            if i in counter:
                dp[i] = max(dp[i + 1], dp[i + 2] + counter[i] * i)
            else:
                dp[i] = max(dp[i + 1], dp[i + 2])
        return dp[1]


solution = Solution()
print(solution.deleteAndEarn(nums=[2, 2, 3, 3, 5]))
print(solution.deleteAndEarn([3, 4, 2]))
print(solution.deleteAndEarn([2, 2, 3, 3, 3, 4]))
