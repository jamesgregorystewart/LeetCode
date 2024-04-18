from typing import Optional, Tuple, Deque
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if depth == 1:
            return TreeNode(val, left=root)

        q: Deque[Tuple[TreeNode, int]] = deque([(root, 1)])
        while q:
            node, cur_depth = q.popleft()
            if cur_depth >= depth:
                return root
            if cur_depth == depth - 1:
                temp_left = node.left
                node.left = TreeNode(val, left=temp_left)
                temp_right = node.right
                node.right = TreeNode(val, right=temp_right)
            else:
                if node.left:
                    q.append((node.left, cur_depth + 1))
                if node.right:
                    q.append((node.right, cur_depth + 1))
        return root
