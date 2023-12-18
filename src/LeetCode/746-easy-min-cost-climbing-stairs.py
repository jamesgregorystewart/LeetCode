from typing import List
from functools import lru_cache


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         if len(cost) == 1:
#             return cost[0]
#
#         # important to break this up instead of creating in one line to prevent
#         # trailing nan entry
#         dp: List[int] = [float('inf')] * len(cost)
#         dp[0], dp[1] = cost[0], cost[1]
#         for i in range(2, len(cost)):
#             dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
#         return min(dp[-1], dp[-2])


# Top Down
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         @lru_cache(None)
#         def dp(i: int) -> int:
#             if i >= len(cost):
#                 return 0
#
#             return min(dp(i+1), dp(i+2)) + cost[i]
#         return min(dp(0), dp(1))


# Bottom Up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = prev2 = 0
        for i in range(len(cost)-1, -1, -1):
            prev2, prev1 = prev1, min(prev2, prev1) + cost[i]
        return min(prev1, prev2)



solution = Solution()
print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
print(solution.minCostClimbingStairs(cost=[10, 15]))
