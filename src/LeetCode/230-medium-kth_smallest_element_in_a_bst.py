# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_found, i, res = False, 1, None
        def helper(node):
            nonlocal smallest_found
            nonlocal i
            nonlocal res
            if not node:
                smallest_found = True
                return
            helper(node.left)
            if res:
                return
            if smallest_found and i == k:
                res = node
            if smallest_found:
                i += 1
            helper(node.right)
        helper(root)
        return res.val
