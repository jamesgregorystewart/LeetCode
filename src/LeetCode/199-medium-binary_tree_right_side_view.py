from re import L
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         right_arm, max_depth = True, 0
#         def helper(node, depth, res) -> None:
#             nonlocal max_depth
#             nonlocal right_arm
#             if not node:
#                 right_arm = False
#                 return
#             if right_arm or depth > max_depth:
#                 res.append(node.val)
#             max_depth = max(max_depth, depth)
#             helper(node.right, depth + 1, res)
#             helper(node.left, depth + 1, res)
#         helper(root, 0, res)
#         return res
#


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_to_node = {}

        def helper(node, depth) -> None:
            nonlocal level_to_node
            if not node:
                return
            if depth not in level_to_node:
                level_to_node[depth] = node.val
            helper(node.right, depth + 1)
            helper(node.left, depth + 1)

        helper(root, 0)
        return list(level_to_node.values())
