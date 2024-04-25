import collections
import heapq
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[2], edge[1], i))
            graph[edge[1]].append((edge[2], edge[0], i))

        pq = []
        seen = set()
        seen.add(0)
        ans = [False] * len(edges)
        # shortest_path = None
        for adj in graph[0]:
            heapq.heappush(pq, (adj[0], adj[1], adj[2]))

        shortest_path = float("inf")
        while pq:
            weight, node, edge_i = heapq.heappop(pq)
            # ans[edge_i] = True
            if node == n - 1:
                shortest_path = weight
                break
            for neigh_weight, neighbor_val, neighbor_edge_i in graph[node]:
                if neighbor_val not in seen:
                    seen.add(node)
                    heapq.heappush(
                        pq, (weight + neigh_weight, neighbor_val, neighbor_edge_i)
                    )

        def dfs(cur, edge_path, path_weight, dfs_seen) -> None:
            if path_weight > shortest_path:
                return
            if cur == n - 1 and path_weight == shortest_path:
                for edge in edge_path:
                    ans[edge] = True
                return

            for neighbor_weight, neighbor_val, neighbor_edge_i in graph[cur]:
                if neighbor_val not in dfs_seen:
                    dfs_seen.add(neighbor_val)
                    edge_path.append(neighbor_edge_i)
                    dfs(
                        neighbor_val, edge_path, path_weight + neighbor_weight, dfs_seen
                    )
                    dfs_seen.remove(neighbor_val)
                    edge_path.pop()

        dfs_seen = set()
        dfs_seen.add(0)
        dfs(0, [], 0, dfs_seen)

        return ans
