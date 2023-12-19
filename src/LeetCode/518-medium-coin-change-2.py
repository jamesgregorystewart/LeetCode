from typing import List


# Basic RECURSIVE solution; gets TLE in LeetCode
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         def helper(remaining: int, i: int) -> int:
#             if remaining == 0:
#                 return 1
#             if i == len(coins):
#                 return 0
#
#             if coins[i] > remaining:
#                 return helper(remaining, i + 1)
#             else:
#                 return (helper(remaining - coins[i], i) +
#                         helper(remaining, i + 1))
#
#         return helper(amount, 0)


# Recusive solution with Memoization
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         def helper(remaining: int, i: int) -> int:
#             if remaining == 0:
#                 return 1
#             if i == len(coins):
#                 return 0
#             if memo[i][remaining] != -1:
#                 return memo[i][remaining]
#
#             if coins[i] > remaining:
#                 memo[i][remaining] = helper(remaining, i + 1)
#             else:
#                 memo[i][remaining] = (helper(remaining, i + 1) +
#                                       helper(remaining - coins[i], i))
#
#             return memo[i][remaining]
#
#         # memo[i][j] stores the number of ways to make up j amount,
#         # using coins beginning at index i
#         memo = [[-1] * (amount + 1) for _ in range(len(coins))]
#         return helper(amount, 0)


# DP Bottom-Up (Pull) Solution; Iterative
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         """
#         dp[i][j] stores the number of ways to make up j amount using coins
#         beginning at index i
#         """
#         # give dp an extra row of 0s to prevent index out of bounds
#         dp: List[List[int]] = [[1] + [0] * amount for _ in range(len(coins)+1)]
#         for i in range(len(coins)-1, -1, -1):
#             for j in range(1, amount+1):
#                 if coins[i] > j:
#                     dp[i][j] = dp[i+1][j]
#                 else:
#                     dp[i][j] = dp[i+1][j] + dp[i][j-coins[i]]
#         return dp[0][amount]


# DP Bottom-Up (Push) Solution; Iterative
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:


# DP Bottom-Up (Pull/Standard) Space-Optimized Solution; Iterative
"""
As Errichto said, it's often possible to remove a dimension from the space
by iterating over the same cells more than once
"""
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp: List[int] = [1] + [0] * amount
#         for i in range(len(coins)-1, -1, -1):
#             for j in range(coins[i], amount+1):
#                 dp[j] += dp[j-coins[i]]
#         return dp[amount]








class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]


solution = Solution()
print(solution.change(5, coins=[5, 1, 2]))
print(solution.change(amount = 3, coins = [2]))
print(solution.change(amount = 10, coins = [10]))
