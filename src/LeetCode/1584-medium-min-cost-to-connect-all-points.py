# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
#
#
#
# Example 1:
#
#
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
#
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:
#
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
#
#
# Constraints:
#
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

from typing import List, Tuple
import collections


# Kruskal's Algorithm; Creating, sorting, then iterating through edges
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         # Edges is a list of points
#         edges: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
#         for i in range(len(points)):
#             for j in range(i + 1, len(points)):
#                 a = (points[i][0], points[i][1])
#                 b = (points[j][0], points[j][1])
#                 edges.append((a, b))
#         sorted_edges = sorted(edges,
#                               key=lambda edge: abs(edge[0][0]-edge[1][0]) +
#                               abs(edge[0][1]-edge[1][1]))
#
#         uf = UnionFind()
#         cost, count = 0, len(points)-1
#         for a, b in sorted_edges:
#             if count == 0:
#                 return cost
#             if not uf.connected(a, b):
#                 uf.union(a, b)
#                 cost += abs(a[0]-b[0])+abs(a[1]-b[1])
#                 count -= 1
#         return cost
#
#
# class UnionFind:
#     def __init__(self):
#         self.root = {}
#         self.rank = {}
#
#     def find(self, x: Tuple[int,int]) -> int:
#         if x not in self.root:
#             self.root[x] = x
#             self.rank[x] = 1
#             return x
#         if self.root[x] != x:
#             self.root[x] = self.find(self.root[x])
#         return self.root[x]
#
#     def union(self, x: int, y: int) -> None:
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = self.root[rootX]
#             elif self.rank[rootY] > self.rank[rootX]:
#                 self.root[rootX] = self.root[rootY]
#             else:
#                 self.root[rootY] = self.root[rootX]
#                 self.rank[rootX] += 1
#
#     def connected(self, x: int, y: int) -> bool:
#         return self.find(x) == self.find(y)


# Prim's Algorithm; Add vertices one at a time
"""
Idea is to add all the edges from point 0 to heap,
iteratively popping edges off and checking if you have seen the second point,
if not you mark it as visited, update cost, update count, and add more edges 
to heap. When count is 0 or heap is depleted you are done
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        edges = []
        seen = [True] + [False] * (len(points) - 1)
        count = len(points) - 1
        result = 0

        for i in range(1, len(points)):
            cost = abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1])
            edge = Edge(0, i, cost)
            edges.append(edge)

        import heapq

        heapq.heapify(edges)
        while edges and count > 0:
            edge = heapq.heappop(edges)
            point2 = edge.point2
            cost = edge.cost
            if not seen[point2]:
                seen[point2] = True
                result += cost
                count -= 1
                for i in range(1, len(points)):
                    distance = abs(points[point2][0] - points[i][0]) + abs(
                        points[point2][1] - points[i][1]
                    )
                    edge = Edge(point2, i, distance)
                    heapq.heappush(edges, edge)
        return result


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


solution = Solution()
print(solution.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(solution.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
