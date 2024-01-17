# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
#
#  
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#  
#
# Constraints:
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        disjointset = DisjointSet(len(isConnected))
        for i in range(disjointset.n-1):
            for j in range(i+1, disjointset.n):
                if isConnected[i][j]:
                    disjointset.union(i, j)
        res = set()
        for x in disjointset.root:
            res.add(disjointset.find(x))
        return len(res) if res else 0


solution = Solution()
print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(solution.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
print(solution.findCircleNum([[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,1,0,0,1,1,0,0,1],[0,0,0,0,1,1,0,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1]]))
