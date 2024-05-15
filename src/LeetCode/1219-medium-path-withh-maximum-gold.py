import functools
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        R, C = len(grid), len(grid[0])

        total_gold = functools.reduce(lambda gold, row: gold + sum(row), grid, 0)

        def dfs(r, c, sum) -> None:
            if self.ans == total_gold:
                return
            matched = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dr, dc = r + dx, c + dy
                if 0 <= dr < R and 0 <= dc < C and grid[dr][dc]:
                    temp = grid[dr][dc]
                    grid[dr][dc] = 0
                    dfs(dr, dc, sum + temp)
                    grid[dr][dc] = temp
                    matched += 1
            if not matched:
                self.ans = max(self.ans, sum)

        for r in range(R):
            for c in range(C):
                if self.ans == total_gold:
                    return self.ans
                if grid[r][c]:
                    temp = grid[r][c]
                    grid[r][c] = 0
                    dfs(r, c, temp)
                    grid[r][c] = temp

        return self.ans
