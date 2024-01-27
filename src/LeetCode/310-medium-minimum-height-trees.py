# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
#
#
#
# Example 1:
#
#
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
# Example 2:
#
#
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
#
#
# Constraints:
#
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.


"""
Idea is we construct the adj_list and in_degree map, then calculate MHT using highest in-degree nodes as roots first
until we get the first tree with a non min height. We terminate early by returning answer.
If this early termination case doesn't exist we iterate through all all possible trees.
When we get a tree with a new min height, we clear out the result array, and add that root in.
When we get a tree with the same min height, we append the root to the result array.
Iterate through queue (and tree) at a level per iteration

Possible optimization is to iterate through the roots in order of highest in-degree first
"""


from typing import List
import collections
import math


# My Failure of a solution using Khan's Algorithm
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if not edges:
#             return [0]
#         # build adj_list and in_degree map
#         adj_list = collections.defaultdict(list)
#         in_degree = collections.defaultdict(int)
#         for node1, node2 in edges:
#             adj_list[node1].append(node2)
#             adj_list[node2].append(node1)
#             in_degree[node1] += 1
#             in_degree[node2] += 1
#         tolerance = 0.50
#         tolerance_count = 0
#
#         min_height = float("inf")
#         result = []
#         for root in sorted(in_degree, key=in_degree.get, reverse=True):
#             # start each iteration with a new root
#             queue = collections.deque([root])
#             seen = set([root])
#             height = 0
#             while queue:
#                 band = len(queue)
#                 for _ in range(band):
#                     cur_node = queue.popleft()
#                     for node in adj_list[cur_node]:
#                         if node not in seen:
#                             seen.add(node)
#                             queue.append(node)
#                 height += 1
#             if height < min_height:
#                 result = [root]
#                 min_height = height
#             elif height == min_height:
#                 result.append(root)
#             else:
#                 tolerance_count += 1
#                 if tolerance_count > (min(1000, math.ceil(tolerance * n))):
#                     break
#         return result


# Editorial Solution using concept of "centroids"
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves


solution = Solution()
print(solution.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
print(solution.findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
