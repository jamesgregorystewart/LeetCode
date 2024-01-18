# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.
#
# For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.
#
# Return the minimum total cost to supply water to all houses.
#
#  
#
# Example 1:
#
#
# Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# Output: 3
# Explanation: The image shows the costs of connecting houses using pipes.
# The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
# Example 2:
#
# Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
# Output: 2
# Explanation: We can supply water with cost two using one of the three options:
# Option 1:
#   - Build a well inside house 1 with cost 1.
#   - Build a well inside house 2 with cost 1.
# The total cost will be 2.
# Option 2:
#   - Build a well inside house 1 with cost 1.
#   - Connect house 2 with house 1 with cost 1.
# The total cost will be 2.
# Option 3:
#   - Build a well inside house 2 with cost 1.
#   - Connect house 1 with house 2 with cost 1.
# The total cost will be 2.
# Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 
#  
#
# Constraints:
#
# 2 <= n <= 104
# wells.length == n
# 0 <= wells[i] <= 105
# 1 <= pipes.length <= 104
# pipes[j].length == 3
# 1 <= house1j, house2j <= n
# 0 <= costj <= 105
# house1j != house2j

from typing import List, Tuple


class Solution:
    def minCostToSupplyWater(
            self,
            n: int,
            wells: List[int],
            pipes: List[List[int]]) -> int:

        ordered_edges: Tuple[int, int, int] = []
        uf = UnionFind(n)
        # Add the wells as edges to a virtual node 0
        for i, cost in enumerate(wells):
            ordered_edges.append((0, i+1, cost))
        # Add the pipes
        for house1, house2, cost in pipes:
            ordered_edges.append((house1, house2, cost))

        ordered_edges = sorted(ordered_edges, key=lambda x: x[2])

        total_cost = 0
        # Add unconnected edges to union
        for edge in ordered_edges:
            if not uf.connected(edge[0], edge[1]):
                uf.union(edge[0], edge[1])
                total_cost += edge[2]

        return total_cost


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

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
                self.root[rootX] = self.root[rootY]
            else:
                self.root[rootY] = self.root[rootX]
                self.rank[rootX] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


solution = Solution()
print(solution.minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]))
print(solution.minCostToSupplyWater(n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]))
