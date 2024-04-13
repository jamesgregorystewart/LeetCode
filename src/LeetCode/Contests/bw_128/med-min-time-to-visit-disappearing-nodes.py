from collections import defaultdict
from typing import List
import heapq


class Solution:
    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        shortest_distance_to = defaultdict(int)
        graph = defaultdict(list)
        for u, v, length in edges:
            if u == v:
                continue
            graph[u].append((v, length))
            graph[v].append((u, length))

        q = [(0, 0)]
        processed = set()

        while q:
            distance, node = heapq.heappop(q)
            if node in processed:
                continue
            if node not in shortest_distance_to:
                shortest_distance_to[node] = distance
            else:
                shortest_distance_to[node] = min(shortest_distance_to[node], distance)
            for adj_node, adj_weight in graph[node]:
                if distance + adj_weight < disappear[adj_node]:
                    heapq.heappush(q, ((distance + adj_weight), adj_node))
            processed.add(node)

        res = []
        for i in range(n):
            if i not in shortest_distance_to or shortest_distance_to[i] >= disappear[i]:
                res.append(-1)
            else:
                res.append(shortest_distance_to[i])

        return res
