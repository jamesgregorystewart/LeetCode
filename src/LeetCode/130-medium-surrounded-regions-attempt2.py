from typing import List
import collections


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None

        def bfs(coord) -> None:
            n, m = len(board), len(board[0])
            board[coord[0]][coord[1]] = "I"
            queue = collections.deque([coord])
            moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while queue:
                (x, y) = queue.popleft()
                for move in moves:
                    dx, dy = x + move[0], y + move[1]
                    if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == "O":
                        board[dx][dy] = "I"
                        queue.append((dx, dy))

        n, m = len(board), len(board[0])
        # check sides
        for i in range(n):
            if board[i][0] == "O":
                bfs((i, 0))
            if board[i][m - 1] == "O":
                bfs((i, m - 1))

        # check top and bottom
        for j in range(m):
            if board[0][j] == "O":
                bfs((0, j))
            if board[n - 1][j] == "O":
                bfs((n - 1, j))

        # flip to final state
        for i in range(n):
            for j in range(m):
                if board[i][j] == "I":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
