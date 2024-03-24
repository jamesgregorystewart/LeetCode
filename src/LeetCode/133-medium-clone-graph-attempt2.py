from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        def helper(node) -> Optional["Node"]:
            if not node:
                return None
            new_node = (
                self.nodes[node.val] if node.val in self.nodes else Node(node.val)
            )
            self.nodes[node.val] = new_node
            for neighbor in node.neighbors:
                if (node.val, neighbor.val) not in self.mappings:
                    self.mappings.add((new_node.val, neighbor.val))
                    new_node.neighbors.append(helper(neighbor))
            return new_node

        self.nodes = {}
        self.mappings: Set[Tuple[int, int]] = set()
        return helper(node)
