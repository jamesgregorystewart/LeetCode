from typing import List, Dict, Set
from collections import defaultdict

"""
Time Complexity: O(M*N) where M is the num of queries and N is the num of equations

We iterate through the equations to build the graph in O(N).
For each query we traverse the graph which in the worst case is O(N), and 
we do that M times.

Space Complexity: O(N) where N is the number of equations

We put all of the equations and their respective values into a graph.
Since we use recursion in the backtracking, there may be up to O(N) space used.
We do not count space used to hold result. If so, it would have been O(N + M)
"""


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        if not equations or not values or not queries:
            return []

        def dfs(cur_node, target_node, product, visited) -> float:
            visited.add(cur_node)
            ret = -1.0  # indicates there is no path from cur_node to target
            neighbors = graph[cur_node]
            if target_node in neighbors:
                ret = product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = dfs(neighbor, target_node, value * product, visited)
                    if ret != -1.0:
                        # this means we did not find the target down this path of neighbor as our next dividend
                        break

            # removing the cur_node is important because we are going to backtrack and attempt to go down a new path wherein we may need to add cur_node back into our path
            visited.remove(cur_node)
            return ret

        # Step 1 build the graph / adj list
        graph: Dict[str, Dict[str, float]] = defaultdict(defaultdict)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        ans: List[float] = []
        # Step 2 Evaluate the queries
        for dividend, divisor in queries:
            if divisor not in graph or dividend not in graph:
                ret = -1.0
            elif divisor == dividend:
                ret = 1.0
            else:
                visited: Set[str] = set()
                ret = dfs(dividend, divisor, 1.0, visited)
            ans.append(ret)

        return ans
