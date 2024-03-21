from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def helper(A, B) -> bool:
            if not A and not B:
                return True
            if not A or not B:
                return False
            if A.val != B.val:
                return False
            return helper(A.left, B.right) and helper(A.right, B.left)

        return helper(root.left, root.right)
