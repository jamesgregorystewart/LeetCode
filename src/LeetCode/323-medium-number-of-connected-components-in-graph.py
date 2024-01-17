# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.
#
#  
#
# Example 1:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
#  
#
# Constraints:
#
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

from typing import List


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointset = DisjointSet(n)
        for edge in edges:
            disjointset.union(edge[0], edge[1])
        roots = set()
        for i in range(n):
            roots.add(disjointset.find(i))
        return len(roots)


solution = Solution()
print(solution.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))
print(solution.countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]))
