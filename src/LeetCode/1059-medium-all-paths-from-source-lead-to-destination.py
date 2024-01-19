# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:
#
# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# Return true if and only if all roads from source lead to destination.
#
#  
#
# Example 1:
#
#
# Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
# Output: false
# Explanation: It is possible to reach and get stuck on both node 1 and node 2.
# Example 2:
#
#
# Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
# Output: false
# Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
# Example 3:
#
#
# Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
# Output: true
#  
#
# Constraints:
#
# 1 <= n <= 104
# 0 <= edges.length <= 104
# edges.length == 2
# 0 <= ai, bi <= n - 1
# 0 <= source <= n - 1
# 0 <= destination <= n - 1
# The given graph may have self-loops and parallel edges.


from typing import List, Tuple, Set, Dict
import collections


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1 create graph
        self.graph = collections.defaultdict(list)
        for start, end in edges:
            self.graph[start].append(end)
        can_get_to_dest = collections.defaultdict(bool)

        def dfs(start) -> bool:
            if can_get_to_dest[start]:
                return True
            destinations = self.graph[start]
            if destinations and start == destination:
                return False
            if not destinations:
                return start == destination
            leads_to_dest = True
            while destinations:
                next_end = destinations.pop()
                leads_to_dest &= dfs(next_end)
                if leads_to_dest:
                    can_get_to_dest[next_end] = True
            if leads_to_dest:
                can_get_to_dest[start] = True
            return leads_to_dest

        return dfs(source)



solution = Solution()
print(solution.leadsToDestination(n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2))
print(solution.leadsToDestination(n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3))
print(solution.leadsToDestination(n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3))
print(solution.leadsToDestination(n = 5, edges = [[0,1],[0,2],[0,3],[0,3],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]], source = 0, destination = 4))
print(solution.leadsToDestination(n = 5, edges = [[0,1],[0,2],[1,3],[2,3],[3,0]], source=0, destination=3))
