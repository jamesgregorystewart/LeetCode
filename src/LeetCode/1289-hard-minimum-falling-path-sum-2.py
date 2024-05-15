from typing import List
import inf

"""
dp[i][j] min sum through row i with last col == j

Relation:
skip = 
pick = 
dp[i][j] = min(dp[i][])
"""


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # dp[i][j] min sum through row i with last col == j
        dp = [[inf] * n for _ in range(m)]
        
        for i in range(n):
            for 
