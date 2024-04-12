from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        def helper(root):
            if not root:
                return

            helper(root.left)
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            self.last = root

            helper(root.right)

        self.first = None
        self.last = None
        helper(root)

        if self.first and self.last:
            self.first.left = self.last
            self.last.right = self.first

        return self.first
