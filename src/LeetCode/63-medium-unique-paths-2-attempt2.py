"""
000
010
000

2110
1010
1110
0000
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp[n - 1][m - 1] = 1
        if obstacleGrid[n - 1][m - 1] == 1:
            return 0

        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if obstacleGrid[row][col] == 1 or (row == n - 1 and col == m - 1):
                    continue
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        return dp[0][0]
