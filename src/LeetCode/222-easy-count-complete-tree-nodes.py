from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def compute_depth(root) -> int:
            d = 0
            while root and root.left:
                root = root.left
                d += 1
            return d

        def exists(target, depth, root) -> bool:
            node = root
            left, right = 0, (2**depth) - 1
            for _ in range(depth):
                index = left + (right - left) // 2
                if index >= target:
                    node = node.left
                    right = index - 1
                else:
                    node = node.right
                    left = index + 1
            return node is not None

        depth = compute_depth(root)
        if depth == 0:
            return 1

        left, right = 1, (2**depth) - 1
        while left <= right:
            target = left + (right - left) // 2
            if exists(target, depth, root):
                left = target + 1
            else:
                right = target - 1

        return (2**depth - 1) + left
