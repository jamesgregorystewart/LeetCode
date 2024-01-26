# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
#
#
#
# Example 1:
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:
#
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:
#
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

from typing import List, Dict, Tuple
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times or n < 2:
            return -1

        # Build adj matrix
        graph: Dict[int, List[Tuple[int, int]]] = collections.defaultdict(list)
        for src, to, weight in times:
            graph[src].append((to, weight))
        queue = [(0, k)]  # This is a min heap
        processed = set()
        max_cost = 0

        """
        We are going to continue popping off the node with the shortest path, taking
        what is the current delay get where we were previously and adding the weight
        to the adjacent nodes and putting those back onto the queue. Once we have
        visited all of the nodes, and the queue is empty, we will be able to return
        what we have calculate to be the max delay along the longest path in the graph.
        """

        while queue:
            weight, node = heapq.heappop(queue)
            if node in processed:
                continue
            for adj_node, adj_weight in graph[node]:
                if adj_node not in processed:
                    heapq.heappush(queue, (weight + adj_weight, adj_node))
            processed.add(node)
            max_cost = max(max_cost, weight)

        return max_cost if len(processed) == n else -1


solution = Solution()
print(solution.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(solution.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
print(solution.networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
print(solution.networkDelayTime(times=[[1, 2, 1], [2, 3, 2], [1, 3, 2]], n=3, k=1))
