from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_bound, max_bound) -> bool:
            if not node:
                return True
            if node.left and (node.left.val >= node.val or node.left.val <= min_bound):
                return False
            if node.right and (
                node.right.val <= node.val or node.right.val >= max_bound
            ):
                return False
            return helper(node.left, min_bound, node.val) and helper(
                node.right, node.val, max_bound
            )

        return helper(root, float("-inf"), float("inf"))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float("-inf")
        self.isValid = True

        def inorder(root) -> None:
            if not root or not self.isValid:
                return
            inorder(root.left)
            if self.prev >= root.val:
                print("not valid")
                self.isValid = False
                return
            self.prev = root.val
            inorder(root.right)

        inorder(root)
        return self.isValid
