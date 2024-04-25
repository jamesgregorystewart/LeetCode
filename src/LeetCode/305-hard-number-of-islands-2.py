from typing import List

"""
Approach:
- DSU to union adjacent cells
- ans[i] = i + 1 - num_of_connected_cells
"""


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        land_seen = set()
        dsu = DSU(m, n)
        ans = []
        islands = 0

        for i, j in positions:
            if (i, j) in land_seen:
                ans.append(islands)
                continue
            islands += 1
            for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                dx, dy = i + d[0], j + d[1]
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) in land_seen:
                    if not dsu.is_connected((i, j), (dx, dy)):
                        dsu.union((i, j), (dx, dy))
                        islands -= 1
            land_seen.add((i, j))
            ans.append(islands)
        return ans


class DSU:
    def __init__(self, n, m) -> None:
        self.root = [[(i, j) for j in range(m)] for i in range(n)]
        self.rank = [[0] * m for _ in range(n)]

    def find(self, pos):
        x, y = pos
        if (x, y) == self.root[x][y]:
            return (x, y)
        self.root[x][y] = self.find(self.root[x][y])
        return self.root[x][y]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            ax, ay = rootA
            bx, by = rootB
            if self.rank[ax][ay] > self.rank[bx][by]:
                self.root[bx][by] = rootA
            elif self.rank[ax][ay] < self.rank[bx][by]:
                self.root[ax][ay] = rootB
            else:
                self.root[bx][by] = rootA
                self.rank[ax][ay] += 1

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)
