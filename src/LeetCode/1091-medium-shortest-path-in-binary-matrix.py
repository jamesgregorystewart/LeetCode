# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
#
#  
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:
#
#
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
#  
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1


from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] != 0:
            return -1

        queue = collections.deque()
        queue.append((0,0)) # x, y, path_dist
        moves = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        seen = [[False] * len(grid[0]) for _ in range(len(grid))]
        seen[0][0] = True

        # Let's make sure we stay in bounds
        def is_valid_move(row, col) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and \
                grid[row][col] == 0

        path_length = 1
        while queue:
            band = len(queue)
            for _ in range(band):
                row, col = queue.popleft()
                if row == len(grid)-1 and col == len(grid[0]) - 1:
                    return path_length
                for move in moves:
                    n_row, n_col = [a + b for a, b in zip([row, col], move)]
                    if is_valid_move(n_row, n_col) and not seen[n_row][n_col]:
                        seen[n_row][n_col] = True
                        queue.append((n_row, n_col))
            path_length += 1
        return -1


solution = Solution()
print(solution.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]))
print(solution.shortestPathBinaryMatrix(grid = [[0,0,0],[0,0,0],[0,0,0]]))
print(solution.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]))
print(solution.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
