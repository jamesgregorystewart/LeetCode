# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
#
#  
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#  
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100


from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return min(matrix[0])
        dp = [[float('inf')] * (n+2) for _ in range(m)]
        dp[m-1][1:n+1] = matrix[m-1]
        min_path = float('inf')
        for i in range(m-2, -1, -1):
            for j in range(n, 0, -1):
                dp[i][j] = (min(dp[i+1][j+1], dp[i+1][j], dp[i+1][j-1]) +
                            matrix[i][j-1])
                if i == 0:
                    min_path = min(min_path, dp[i][j])
        return min_path


solution = Solution()
print(solution.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
print(solution.minFallingPathSum(matrix = [[-19,57],[-40,-5]]))
