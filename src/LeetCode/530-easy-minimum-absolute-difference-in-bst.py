from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev = float("inf")

        def inorder(root) -> None:
            if not root:
                return
            inorder(root.left)
            self.min_diff = min(self.min_diff, abs(self.prev - root.val))
            self.prev = root.val
            inorder(root.right)

        inorder(root)
        return self.min_diff
