from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(root) -> int:
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)
            self.ans += abs(left) + abs(right)

            # The number of coins current has available to exchange
            return (root.val - 1) + left + right

        helper(root)
        return self.ans
