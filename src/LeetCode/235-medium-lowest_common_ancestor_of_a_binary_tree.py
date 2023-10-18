# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node, p, q) -> 'TreeNode':
            if not node:
                return None

            if node == q or node == p:
                return node

            left_lca = right_lca = None
            if p.val < node.val or q.val < node.val:
                left_lca = helper(node.left, p, q)
            if p.val > node.val or q.val > node.val:
                right_lca = helper(node.right, p , q)

            if left_lca and right_lca:
                return node
            elif left_lca:
                return left_lca
            else:
                return right_lca

        return helper(root, p, q)
