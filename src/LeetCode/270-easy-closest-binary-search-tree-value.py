from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return -1

        greater = (10**9) + 1
        smaller = (-(10**9)) - 1
        while root:
            if root.val > target:
                greater = min(greater, root.val)
                root = root.left
            else:
                smaller = max(smaller, root.val)
                root = root.right

        return greater if abs(greater - target) < abs(target - smaller) else smaller
