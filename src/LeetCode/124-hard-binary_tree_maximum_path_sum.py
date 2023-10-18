# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')
        def helper(node) -> int:
            nonlocal max_path_sum
            if not node:
                return 0
            left_sum = max(0, helper(node.left))
            right_sum = max(0, helper(node.right))
            max_path_sum = max(max_path_sum, left_sum + node.val + right_sum)
            return node.val + max(left_sum, right_sum) 
        helper(root)
        return max_path_sum
