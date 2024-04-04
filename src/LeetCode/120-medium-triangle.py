from typing import List

"""
dp[row][col] = min(dp[row+1][col], dp[row+1][col+1]) + 1

1
1 2
1 2 3
1 2 3 4

ans = 4


2
3 4
6 5 7
4 1 8 3
"""


# O(n * (n+1) // 2) ~O(n^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp = [[float("inf") * len(triangle[0])] for _ in range(len(triangle))]
        dp = triangle.copy()
        n = len(triangle)
        for row in range(n - 2, -1, -1):
            for col in range(0, row + 1):
                dp[row][col] = (
                    min(dp[row + 1][col], dp[row + 1][col + 1]) + dp[row][col]
                )

        return dp[0][0]
