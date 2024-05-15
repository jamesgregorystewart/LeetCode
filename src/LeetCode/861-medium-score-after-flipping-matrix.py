import functools
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        # Flip rows to get 1 in first position
        for row in grid:
            if row[0] == 0:
                row[:] = [1 - x for x in row]  # Flip the entire row

        R, C = len(grid), len(grid[0])
        # Flip columns
        for c in range(C):
            col_sum = sum(grid[r][c] for r in range(R))
            if col_sum < (R / 2):
                for r in range(R):
                    grid[r][c] = 1 - grid[r][c]

        ans = 0
        for row in grid:
            # Convert binary row to integer
            ans += int("".join(map(str, row)), 2)

        return ans
