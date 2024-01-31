# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#
#
# Example 1:
#
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List
import collections


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        fortified = set()
        n, m = len(board), len(board[0])

        def bfs(queue, fortifying):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if fortifying:
                fortified.add(queue[-1])
            else:
                board[queue[-1][0]][queue[-1][1]] = "X"
            while queue:
                (x, y) = queue.popleft()
                for d in directions:
                    x1, y1 = x + d[0], y + d[1]
                    if (
                        0 <= x1 < n
                        and 0 <= y1 < m
                        and board[x1][y1] == "O"
                        and (x1, y1) not in fortified
                    ):
                        if fortifying:
                            fortified.add((x1, y1))
                        else:
                            board[x1][y1] = "X"
                        queue.append((x1, y1))

        # First, add those nodes which are uncapturable to fortified
        for i in range(n):
            if board[i][0] == "O" and (i, 0) not in fortified:
                bfs(collections.deque([(i, 0)]), True)
            if board[i][m - 1] == "O" and (i, m - 1) not in fortified:
                bfs(collections.deque([(i, m - 1)]), True)

        for i in range(m):
            if board[0][i] == "O" and (0, i) not in fortified:
                bfs(collections.deque([(0, i)]), True)
            if board[n - 1][i] == "O" and (n - 1, i) not in fortified:
                bfs(collections.deque([(n - 1, i)]), True)

        # Second, traverse all the nodes in the middle area and if they aren't fortified
        # then capture them!
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if board[i][j] == "O" and (i, j) not in fortified:
                    bfs(collections.deque([(i, j)]), False)
