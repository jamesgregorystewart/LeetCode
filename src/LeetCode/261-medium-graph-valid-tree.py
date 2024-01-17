# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
#
# Return true if the edges of the given graph make up a valid tree, and false otherwise.
#
#  
#
# Example 1:
#
#
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
#  
#
# Constraints:
#
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        disjointset = DisjointSet(n)
        for edge in edges:
            if disjointset.connected(edge[0], edge[1]):
                return False
            disjointset.union(edge[0], edge[1])
        # Now check for multiple graphs
        root = disjointset.find(0)
        for i in range(1, n):
            if disjointset.find(i) != root:
                return False
        return True


solution = Solution()
print(solution.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
print(solution.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]))
print(solution.validTree(n = 4, edges = [[0,1],[2,3]]))
print(solution.validTree(n = 3, edges = [[1,0],[0,2],[2,1]]))
