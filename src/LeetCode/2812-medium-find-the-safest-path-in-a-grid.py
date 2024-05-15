import collections
import heapq
from typing import Deque, List

"""
1) BFS from each thief; encode empty cells with dist to nearest thief
2) BFS from start to end using heap returning max safeness seen so far when end is found
"""


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = -1

        while q:
            r, c = q.popleft()
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dr, dc = r + d[0], c + d[1]
                if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] == -1:
                    grid[dr][dc] = grid[r][c] + 1
                    q.append((dr, dc))

        pq = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1

        while pq:
            safeness, r, c = heapq.heappop(pq)
            if r == R - 1 and c == C - 1:
                return -safeness

            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dr, dc = r + d[0], c + d[1]
                if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] != -1:
                    heapq.heappush(pq, (-min(-safeness, grid[dr][dc]), dr, dc))
                    grid[dr][dc] = -1
        return -1
