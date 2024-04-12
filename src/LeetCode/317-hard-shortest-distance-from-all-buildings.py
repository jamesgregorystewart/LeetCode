from typing import List
from collections import deque

"""
[[1,0,2,0,1]
 [0,0,0,0,0]
 [0,0,1,0,0]]
"""

# from empty land to houses
# class Solution:
#     def shortestDistance(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#
#         def get_neighbors(node):
#             moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#             x, y = node
#             for dx, dy in moves:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 2:
#                     yield (nx, ny)
#
#         def bfs(r, c) -> int:
#             q = deque([(r, c)])
#             seen = set()
#             seen.add((r, c))
#             distance_travelled = 0
#             distance_to_all = 0
#             houses_found = 0
#             while q and houses_found != num_houses:
#                 for _ in range(len(q)):
#                     node = q.popleft()
#                     if grid[node[0]][node[1]] == 1:
#                         distance_to_all += distance_travelled
#                         houses_found += 1
#                         continue
#                     for x, y in get_neighbors(node):
#                         if (x, y) not in seen:
#                             seen.add((x, y))
#                             q.append((x, y))
#                 distance_travelled += 1
#
#             # we weren't able to reach all the houses from this node; set all nodes in path to '2'
#             if houses_found != num_houses:
#                 for x, y in seen:
#                     if grid[x][y] == 0:
#                         grid[x][y] = 2
#
#             return distance_to_all if houses_found == num_houses else float("inf")
#
#         num_houses = 0
#         for r in range(n):
#             for c in range(m):
#                 if grid[r][c] == 1:
#                     num_houses += 1
#
#         ans = float("inf")
#         for r in range(n):
#             for c in range(m):
#                 if grid[r][c] == 0:
#                     ans = min(ans, bfs(r, c))
#
#         return ans if ans != float("inf") else -1


# from houses to empty land
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        total = [[0 for _ in range(m)] for _ in range(n)]

        def bfs(r, c, empty_land):
            q = deque([(r, c)])
            steps = 0
            while q:
                steps += 1
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        dx, dy = x + dir[0], y + dir[1]
                        if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == empty_land:
                            total[dx][dy] += steps
                            grid[dx][dy] -= 1
                            q.append((dx, dy))

        ans = float("inf")
        empty_land = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    bfs(r, c, empty_land)
                    empty_land -= 1

        ans = float("inf")
        for r in range(n):
            for c in range(m):
                if grid[r][c] == empty_land and total[r][c] < ans:
                    ans = total[r][c]

        return ans if ans != float("inf") else -1
