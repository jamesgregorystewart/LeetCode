# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_val) -> int:
            if not node:
                return 0
            left_count = helper(node.left, max(max_val, node.val))
            right_count = helper(node.right, max(max_val, node.val))

            if node.val >= max_val:
                return left_count + right_count + 1
            else:
                return left_count + right_count

        return helper(root, root.val)
