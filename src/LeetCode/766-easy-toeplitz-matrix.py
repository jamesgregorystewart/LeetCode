from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R, C = len(matrix), len(matrix[0])

        for i in range(R - 1, -1, -1):
            r, c = i, 0
            num = matrix[r][c]
            while r < R and c < C:
                if matrix[r][c] != num:
                    return False
                r, c = r + 1, c + 1

        for i in range(C):
            r, c = 0, i
            num = matrix[r][c]
            while r < R and c < C:
                if matrix[r][c] != num:
                    return False
                r, c = r + 1, c + 1
        return True
