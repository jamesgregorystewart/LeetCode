from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def helper(root) -> bool:
            if not root or (
                root.left is None and root.right is None and root.val == target
            ):
                return False

            left = helper(root.left)
            right = helper(root.right)
            if not left:
                root.left = None
            if not right:
                root.right = None

            return False if (not left and not right and root.val == target) else True

        dummy = TreeNode(0, None, root)
        helper(dummy)
        return dummy.right
