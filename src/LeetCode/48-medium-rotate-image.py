from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        column becomes row
        len(matrix) - 1 - row becomes column?
        """
        n = len(matrix)
        # this is the starting row
        for i in range(n // 2 + n % 2):
            # this is the starting column
            for j in range(n // 2):
                (
                    matrix[i][j],
                    matrix[i][n - j - 1],
                    matrix[n - i - 1][j],
                    matrix[n - i - 1][n - j - 1],
                ) = (
                    matrix[n - i - 1][j],
                    matrix[i][j],
                    matrix[n - i - 1][n - j - 1],
                    matrix[i][n - j - 1],
                )
        print(matrix)


solution = Solution()
solution.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
