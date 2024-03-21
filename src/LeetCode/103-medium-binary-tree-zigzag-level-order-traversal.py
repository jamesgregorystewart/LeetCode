from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left = True
        levels: List[List[int]] = []
        queue = deque([root])
        while queue:
            band = len(queue)
            level = []
            for _ in range(band):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left:
                levels.append(level)
            else:
                levels.append(level[::-1])
            left = not left
        return levels
