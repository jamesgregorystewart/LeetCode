import collections
from typing import List


# TLE
class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:

        # Create Graph
        graph = collections.defaultdict(list)
        for a, b, cost in roads:
            graph[a].append((b, cost))
            graph[b].append((a, cost))

        def dfs(origin, cur, seen, travel_cost, ans) -> None:
            ans[origin - 1] = min(
                ans[origin - 1], appleCost[cur - 1] + travel_cost + (travel_cost * k)
            )
            for adj_city, weight in graph[cur]:
                if adj_city not in seen:
                    seen.add(adj_city)
                    dfs(origin, adj_city, seen, travel_cost + weight, ans)
                    seen.remove(adj_city)

        ans = [float("inf")] * n
        for city in range(1, n + 1):
            ans[city - 1] = appleCost[city - 1]
            dfs(city, city, {city}, 0, ans)

class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:
        pass
        # is this going to detect my activity or not
