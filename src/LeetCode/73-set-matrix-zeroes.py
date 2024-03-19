from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # should top or side be setZeroes
        topzero, sidezero = False, False
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0] == 0:
                sidezero = True
                break
        for i in range(m):
            if matrix[0][i] == 0:
                topzero = True
                break

        # set flags
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # flip inside to zero
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # flip top and side to zero
        if topzero:
            for i in range(m):
                matrix[0][i] = 0
        if sidezero:
            for i in range(n):
                matrix[i][0] = 0
