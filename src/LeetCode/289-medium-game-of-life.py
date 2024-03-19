from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 or board[i][j] == 2:
                    # it's dead
                    live_neighbors = self.liveNeighbors(board, i, j)
                    if live_neighbors == 3:
                        board[i][j] = 2
                elif board[i][j] == 1 or board[i][j] == -1:
                    # it's alive
                    live_neighbors = self.liveNeighbors(board, i, j)
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1

        # do the transitions
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

    def liveNeighbors(self, board, i, j) -> int:
        # returns how many live neigbors this cell has
        n, m = len(board), len(board[0])
        directions = [
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
        ]
        live_neighbors = 0
        for d in directions:
            di, dj = i + d[0], j + d[1]
            if 0 <= di < n and 0 <= dj < m and board[di][dj] in [1, -1]:
                live_neighbors += 1

        return live_neighbors
