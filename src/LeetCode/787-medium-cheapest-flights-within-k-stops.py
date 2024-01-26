# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
#
#
#
# Example 1:
#
#
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Example 2:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Example 3:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
#
#
# Constraints:
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

from typing import List, Dict, Tuple
import collections


# Bellman-Ford
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [float("inf")] * n

        costs[src] = 0
        for _ in range(k + 1):
            temp = costs.copy()
            for start, end, price in flights:
                # Below checks if we have yet been to where we are starting from
                if costs[start] != float("inf"):
                    temp[end] = min(temp[end], costs[start] + price)
            costs = temp
        return costs[dst] if costs[dst] != float("inf") else -1


# Dijkstra's
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        import heapq

        # adj matrix
        adj = collections.defaultdict(list)
        for start, end, price in flights:
            adj[start].append((end, price))
        pq = [(0, 0, src)]  # weight, stops, start
        visited = set()

        while pq:
            price, stops, start = heapq.heappop(pq)
            if start in visited:
                continue
            for end, next_price in adj[start]:
                if end not in visited:
                    heapq.heappush(pq, (price + next_price, stops + 1, end))
            visited.add(start)


solution = Solution()
print(
    solution.findCheapestPrice(
        n=4,
        flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        src=0,
        dst=3,
        k=1,
    )
)
