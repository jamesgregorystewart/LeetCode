from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
inorder traversal k iterations -> O(H + k) / O(1)
H is bounded between log(n) and n
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.iterations = 1
        self.ans = None

        def helper(root) -> None:
            if not root or self.ans:
                return
            helper(root.left)
            if self.iterations == k and not self.ans:
                self.ans = root.val
            self.iterations += 1
            helper(root.right)

        helper(root)
        return self.ans
