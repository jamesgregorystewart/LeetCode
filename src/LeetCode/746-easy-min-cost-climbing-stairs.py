from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]

        # important to break this up instead of creating in one line to prevent
        # trailing nan entry
        dp: List[int] = [float('inf')] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        return min(dp[-1], dp[-2])


solution = Solution()
print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
print(solution.minCostClimbingStairs(cost=[10, 15]))
print(solution.minCostClimbingStairs(cost=[10]))
