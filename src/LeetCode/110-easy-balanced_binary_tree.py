# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def helper(node) -> int:
            nonlocal is_balanced
            if not is_balanced or not node:
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            if abs(left_depth - right_depth) > 1:
                is_balanced = False
            return max(left_depth, right_depth) + 1
        helper(root)
        return is_balanced
