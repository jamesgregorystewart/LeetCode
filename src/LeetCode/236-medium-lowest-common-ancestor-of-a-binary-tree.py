# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        ans: "Treenode" = None

        def helper(node) -> int:
            nonlocal ans
            if not node or ans:
                return 0
            sum = helper(node.left) + helper(node.right)
            sum = sum + 1 if node.val in [p.val, q.val] else sum
            if sum == 2:
                ans = node
                return 0
            return sum

        helper(root)
        return ans
