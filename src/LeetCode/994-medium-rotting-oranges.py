# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#  
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#  
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        n, m = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0
        if len(queue) == 0:
            return -1

        def get_neighbors(row, col):
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for row_diff, col_diff in directions:
                n_row, n_col = row + row_diff, col + col_diff
                if not (0 <= n_row < n and 0 <= n_col < m):
                    continue
                if grid[n_row][n_col] != 1:
                    continue
                yield (n_row, n_col)

        minutes = -1
        while queue:
            minutes += 1
            band = len(queue)
            for _ in range(band):
                row, col = queue.popleft()
                for orange in get_neighbors(row, col):
                    grid[orange[0]][orange[1]] = 2
                    fresh -= 1
                    queue.append(orange)
        return minutes if fresh == 0 else -1


solution = Solution()
print(solution.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
print(solution.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
print(solution.orangesRotting(grid = [[0,2]]))
