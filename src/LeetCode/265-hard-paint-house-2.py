# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
                # dp[house][color] = min_house_cost + costs[house][color]
#
# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.
#
# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Return the minimum cost to paint all houses.
#
#  
#
# Example 1:
#
# Input: costs = [[1,5,3],[2,9,4]]
# Output: 5
# Explanation:
# Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Example 2:
#
# Input: costs = [[1,3],[2,4]]
# Output: 5
#  
#
# Constraints:
#
# costs.length == n
# costs[i].length == k
# 1 <= n <= 100
# 2 <= k <= 20
# 1 <= costs[i][j] <= 20
#  
#
# Follow up: Could you solve it in O(nk) runtime?


from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[float('inf')] * k for _ in range(n-1)]
        dp += [costs[-1]]
        if len(dp) == 1:
            return min(dp[0])
        min_total_cost = float('inf')
        # track last two mins, and their respective color indices
        prev1_min = (float('inf'), float('inf'))
        prev2_min = (float('inf'), float('inf'))
        for i, cost in enumerate(costs[-1]):
            if cost <= prev1_min[1]:
                prev1_min, prev2_min = (i, cost), prev1_min

        for house in range(n-2, -1, -1):
            next_prev1_min = (float('inf'), float('inf'))
            next_prev2_min = (float('inf'), float('inf'))
            for color in range(k):
                if color == prev1_min[0]:
                    dp[house][color] = prev2_min[1] + costs[house][color]
                else:
                    dp[house][color] = prev1_min[1] + costs[house][color]
                if dp[house][color] <= next_prev1_min[1]:
                    next_prev2_min = next_prev1_min
                    next_prev1_min = (color, dp[house][color])
                if house == 0:
                    min_total_cost = min(min_total_cost, dp[house][color])

            prev1_min, prev2_min = next_prev1_min, next_prev2_min
        return min_total_cost

# class Solution:
#     def minCostII(self, costs: List[List[int]]) -> int:
#         n, k = len(costs), len(costs[0])
#         dp = [[float('inf')] * k for _ in range(n-1)]
#         dp += [costs[-1]]
#         if len(dp) == 1:
#             return min(dp[0])
#         min_total_cost = float('inf')
#         for house in range(n-2, -1, -1):
#             for color in range(k):
#                 min_color = float('inf')
#                 for i in range(1, k):
#                     min_color = min(min_color, dp[house+1][(color+i)%k])
#                 dp[house][color] = min_color + costs[house][color]
#                 if house == 0:
#                     min_total_cost = min(min_total_cost, dp[house][color])
#         print(dp)
#
#         return min_total_cost

solution = Solution()
# print(solution.minCostII(costs = [[1,5,3],[2,9,4]]))
# print(solution.minCostII(costs = [[1,3],[2,4]]))
# print(solution.minCostII(costs = [[1,3]]))
print(solution.minCostII(costs = [[8,16,12,18,9],[19,18,8,2,8],[8,5,5,13,4],[15,9,3,19,2],[8,7,1,8,17],[8,2,8,15,5],[8,17,1,15,3],[8,8,5,5,16],[2,2,18,2,9]]))
print(solution.minCostII([[10,15,12,14,18,5],[5,12,18,13,15,8],[4,7,4,2,10,18],[20,9,9,19,20,5],[10,15,10,15,16,20],[9,6,11,10,12,11],[7,10,6,12,20,8],[3,4,4,18,10,2]]))
