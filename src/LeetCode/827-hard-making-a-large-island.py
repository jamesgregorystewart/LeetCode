from typing import List

"""
1) Create DSU that will track all islands and their sizes by root
2) iterate over grid and for each 0 check for largest unconnected neighbors
3) maintain largest possible island to be created
"""


# O(N)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dsu = DSU(N)
        land = 0

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    land += 1
                    for d in [[1, 0], [0, 1]]:
                        dr, dc = r + d[0], c + d[1]
                        if 0 <= dr < N and 0 <= dc < N and grid[dr][dc] == 1:
                            dsu.union((r, c), (dr, dc))

        if not land:
            return 1
        if land == N**2:
            return N**2

        largest_island = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    unique_islands = set()
                    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        dr, dc = r + d[0], c + d[1]
                        if 0 <= dr < N and 0 <= dc < N and grid[dr][dc] == 1:
                            unique_islands.add(dsu.find((dr, dc)))
                    possible_island_size = 1 + sum(
                        dsu.size[root[0]][root[1]] for root in unique_islands
                    )
                    largest_island = max(largest_island, possible_island_size)
        return largest_island


class DSU:
    def __init__(self, n) -> None:
        self.root = [[(i, j) for j in range(n)] for i in range(n)]
        self.rank = [[1] * n for _ in range(n)]
        self.size = [[1] * n for _ in range(n)]

    def find(self, a):
        (x, y) = a
        if self.root[x][y] == a:
            return a
        self.root[x][y] = self.find(self.root[x][y])
        return self.root[x][y]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            (ax, ay) = rootA
            (bx, by) = rootB
            if self.rank[ax][ay] > self.rank[bx][by]:
                self.root[bx][by] = self.root[ax][ay]
                self.size[ax][ay] += self.size[bx][by]
            elif self.rank[ax][ay] < self.rank[bx][by]:
                self.root[ax][ay] = self.root[bx][by]
                self.size[bx][by] += self.size[ax][ay]
            else:
                self.root[bx][by] = self.root[ax][ay]
                self.size[ax][ay] += self.size[bx][by]
                self.rank[ax][ay] += 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)
