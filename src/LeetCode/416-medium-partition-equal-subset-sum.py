# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[target]


solution = Solution()
print(solution.canPartition(nums=[1, 5, 11, 5]))
print(solution.canPartition(nums=[1, 2, 3, 5]))
