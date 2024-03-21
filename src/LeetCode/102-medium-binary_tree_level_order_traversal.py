from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         levels = []
#         def helper(node, depth, levels) -> None:
#             if not node:
#                 return
#
#             if depth < len(levels):
#                 levels[depth].append(node.val)
#             else:
#                 levels.append([node.val])
#
#             helper(node.left, depth + 1, levels)
#             helper(node.right, depth + 1, levels)
#
#         helper(root, 0, levels)
#         return levels

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels: List[List[int]] = []
        queue = deque([root])
        while queue:
            iterations = len(queue)
            level = []
            for _ in range(iterations):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            levels.append(level)
        return levels
