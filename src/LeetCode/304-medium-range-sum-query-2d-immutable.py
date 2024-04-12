from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        self.sum_matrix = self._instantiate_sum_matrix()

    def _instantiate_sum_matrix(self) -> List[List[int]]:
        n, m = len(self.matrix), len(self.matrix[0])
        sum_matrix = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(1, n + 1):
            for c in range(1, m + 1):
                sum_matrix[r][c] = (
                    self.matrix[r - 1][c - 1]
                    + sum_matrix[r - 1][c]
                    + sum_matrix[r][c - 1]
                    - sum_matrix[r - 1][c - 1]
                )
        return sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sum_matrix[row2 + 1][col2 + 1]
            - self.sum_matrix[row2 + 1][col1]
            - self.sum_matrix[row1][col2 + 1]
            + self.sum_matrix[row1][col1]
        )
