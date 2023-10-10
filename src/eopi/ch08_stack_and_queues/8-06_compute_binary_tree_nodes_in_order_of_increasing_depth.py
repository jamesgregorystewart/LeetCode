""" Compute Binary Tree Nodes in Order of Increasing Depth """

"""
Learnings from this problem:
    - Use list comprehensions to create lists of nodes by level
"""

from types import List

def compute_nodes(tree: BinaryTreeNode) -> List[List[int]]:
    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        # Below will create list of nodes by level
        curr_depth_nodes = [
                child for curr in curr_depth_nodes
                for child in (curr.left, curr.right) if child
        ]
    return result
