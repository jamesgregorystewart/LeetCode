# You are given an m x n grid rooms initialized with these three possible values.
#
# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
#
#
# Example 1:
#
#
# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
# Example 2:
#
# Input: rooms = [[-1]]
# Output: [[-1]]
#
#
# Constraints:
#
# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 231 - 1.

"""
Idea:
- bfs from every gate marking the min of what's there or the distance from the gate; skip adding neighbors which have a distance equal to or further than what is already present in the cell
- optimizations may include:
    - early termination of a bfs path when we know there is a closer gate
    - starting a bfs from a gate once we reach a gate -> recursively start bfs from that gate once found and then when we return to resume bfs from original gate we can skip any 
"""

from typing import List
import collections


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        n, m = len(rooms), len(rooms[0])
        print(rooms)

        def bfs(i, j):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = collections.deque([(i, j)])
            distance = 1
            while queue:
                band = len(queue)
                for _ in range(band):
                    (x, y) = queue.popleft()
                    for d in directions:
                        x1, y1 = x + d[0], y + d[1]
                        if (
                            0 <= x1 < n
                            and 0 <= y1 < m
                            and rooms[x1][y1] != -1
                            and rooms[x1][y1] != 0
                            and rooms[x1][y1] > distance
                        ):
                            queue.append((x1, y1))
                            rooms[x1][y1] = distance
                distance += 1

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    bfs(i, j)
