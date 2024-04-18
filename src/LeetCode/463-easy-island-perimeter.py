from typing import List
from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs(x, y) -> int:
            perimeter = 0
            q = deque([(x, y)])
            seen = set()
            seen.add(q[-1])
            n, m = len(grid), len(grid[0])
            while q:
                x, y = q.popleft()
                water_tiles = 4
                for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    dx, dy = x + d[0], y + d[1]
                    if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1:
                        if (dx, dy) not in seen:
                            seen.add((dx, dy))
                            q.append((dx, dy))
                        water_tiles -= 1
                perimeter += water_tiles
            return perimeter

        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return bfs(r, c)
        return 0
