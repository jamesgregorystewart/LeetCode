from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.operators = {2: lambda x, y: x | y, 3: lambda x, y: x & y}

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root and not root.left and not root.right:
            return root.val == 1
        elif root:
            left_tree = self.evaluateTree(root.left)
            right_tree = self.evaluateTree(root.right)
            res = self.operators[root.val](left_tree, right_tree)
            return res
        return False
