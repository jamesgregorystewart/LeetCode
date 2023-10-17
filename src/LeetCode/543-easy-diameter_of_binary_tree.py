# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def helper(node) -> int:
            nonlocal diameter
            if not node:
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            diameter = max(diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        helper(root)
        return diameter

