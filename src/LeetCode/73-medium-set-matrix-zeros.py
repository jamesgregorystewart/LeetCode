from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.zeroOut(matrix, i, j)

    def zeroOut(self, matrix, row, col) -> None:
        n = len(matrix)
        m = len(matrix[0])
        # zero the row
        for i in range(m):
            if matrix[row][i] == 0 and i != col:
                zeroOut()
