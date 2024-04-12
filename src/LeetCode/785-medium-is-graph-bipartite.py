from typing import List

"""
[[1,2,3],[0,2],[0,1,3],[0,2]]

0: A
1: B
2: A

graph = [[1,3],[0,2],[1,3],[0,2]]

0: 0
1: 1
2: 0
3: 1
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bipartite(node, expected_set) -> bool:
            if node in self.set_map and self.set_map[node] != expected_set:
                return False
            if node in self.set_map:
                return True

            self.set_map[node] = expected_set

            for vertex in graph[node]:
                if not bipartite(vertex, expected_set ^ 1):
                    return False
            return True

        self.set_map = {}
        for i in range(len(graph)):
            if i not in self.set_map:
                if not bipartite(i, 0):
                    return False

        return True
