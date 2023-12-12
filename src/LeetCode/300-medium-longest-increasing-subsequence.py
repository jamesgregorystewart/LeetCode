from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[int] = [1] * len(nums)  # base case is every seq is at least 1
        res = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])
        return res


solution = Solution()
print(solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
