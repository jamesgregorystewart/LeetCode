# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
#
#  
#
# Example 1:
#
#
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Example 2:
#
#
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#  
#
# Constraints:
#
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.


from typing import List

import collections


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # build adjacency list
        adjacency_list = collections.defaultdict(list)
        for i, edges in enumerate(graph):
            adjacency_list[i] += edges

        # init seen and stack
        target = len(graph) - 1
        seen = [True] + [False] * target
        stack = [[0]]
        paths: List[List[int]] = []

        while stack:
            cur_path = stack.pop()
            seen[cur_path[-1]] = True
            if cur_path[-1] == target:
                paths.append(cur_path)
                # reset seen for tracking new path
                if stack:
                    for i in range(len(cur_path)-1, len(stack[-1])-2, -1):
                        seen[cur_path[i]] = False
                continue
            # add new possible paths to stack
            for vertex in adjacency_list[cur_path[-1]]:
                if not seen[vertex]:
                    stack.append(cur_path + [vertex])
        return paths


solution = Solution()
print(solution.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))
print(solution.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))
