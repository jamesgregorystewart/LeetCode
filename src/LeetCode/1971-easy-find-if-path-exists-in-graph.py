# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
#
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
#
#  
#
# Example 1:
#
#
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# Example 2:
#
#
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
#  
#
# Constraints:
#
# 1 <= n <= 2 * 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.

from typing import List

import collections


class Solution:
    def validPath(
            self,
            n: int,
            edges: List[List[int]],
            source: int, destination: int) -> bool:
        if source == destination:
            return True
        # Step 1 build the adjacency graph
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Step 2 initialize the seen set and the search stack
        seen = [False] * n
        seen[source] = True
        stack = [source]

        # Step 3 find that path
        while stack:
            cur_vertex = stack.pop()
            for vertex in graph[cur_vertex]:
                if vertex == destination:
                    return True
                if not seen[vertex]:
                    stack.append(vertex)
            seen[cur_vertex] = True

        return False


solution = Solution()
print(solution.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
print(solution.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))
