# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
#
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#  
#
# Example 1:
#
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:
#
# Input: prices = [1]
# Output: 0
#  
#
# Constraints:
#
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

from typing import List
from functools import lru_cache


# Top Down Solution
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         @lru_cache(None)
#         def dp(i: int, holding: int) -> int:
#             if i >= len(prices):
#                 return 0
#
#             do_nothing = dp(i+1, holding)
#             if holding:
#                 do_something = dp(i+2, 0) + prices[i]
#             else:
#                 do_something = dp(i+1, 1) - prices[i]
#             return max(do_nothing, do_something)
#         return dp(0, 0)

# Bottom Up Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices)+2)]
        for i in range(len(prices)-1, -1, -1):
            for holding in range(2):
                do_nothing = dp[i+1][holding]
                if holding:
                    do_something = dp[i+2][0] + prices[i]
                else:
                    do_something = dp[i+1][1] - prices[i]
                dp[i][holding] = max(do_nothing, do_something)
        return dp[0][0]


solution = Solution()
print(solution.maxProfit(prices = [1,2,3,0,2]))
print(solution.maxProfit(prices = [1]))

