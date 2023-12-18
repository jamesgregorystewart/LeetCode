# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#  
#
# Example 1:
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:
#
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#  
#
# Constraints:
#
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

from functools import lru_cache
from typing import List


# Top Down Approach
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         @lru_cache(None)
#         def dp(i: int, txns: int, holding: int) -> int:
#             if txns == 0 or i == len(prices):
#                 return 0
#
#             do_nothing = dp(i+1, txns, holding)
#             if holding:
#                 # Sell stock
#                 do_something = dp(i+1, txns-1, 0) + prices[i]
#             else:
#                 # Buy stock
#                 do_something = dp(i+1, txns, 1) - prices[i]
#
#             return max(do_nothing, do_something)
#
#         return dp(0, k, 0)


# Bottom Up Approach
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0] * 2 for _ in range(k+1)] for __ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            for txns in range(1, k+1):
                for holding in range(2):
                    do_nothing = dp[i+1][txns][holding]
                    if holding:
                        # Sell stock
                        do_something = dp[i+1][txns-1][0] + prices[i]
                    else:
                        # Buy stock
                        do_something = dp[i+1][txns][1] - prices[i]
                    dp[i][txns][holding] = max(do_nothing, do_something)

        return dp[0][k][0]


solution = Solution()
print(solution.maxProfit(k = 2, prices = [2,4,1]))
print(solution.maxProfit(k = 2, prices = [3,2,6,5,0,3]))
print(solution.maxProfit(k = 2, prices = [6,5,0]))
print(solution.maxProfit(k = 0, prices = [3,2,6,5,0,3]))
