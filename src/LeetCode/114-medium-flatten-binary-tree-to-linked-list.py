from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                temp = root.right
                con = root.left
                while con and con.right:
                    con = con.right
                root.right = root.left
                con.right = temp
                root.left = None
            root = root.right
