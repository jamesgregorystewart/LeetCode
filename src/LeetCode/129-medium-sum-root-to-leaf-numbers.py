from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, sum) -> int:
            if not node:
                return sum
            if not node.left and not node.right:
                return (sum * 10) + node.val
            left_subtree = right_subtree = 0
            if node.left:
                left_subtree = dfs(node.left, (sum * 10) + node.val)
            if node.right:
                right_subtree = dfs(node.right, (sum * 10) + node.val)
            return left_subtree + right_subtree

        return dfs(root, 0)
