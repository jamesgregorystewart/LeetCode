# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        def helper(root) -> int:
            if not root or self.ans:
                return 0
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            sum = left_sum + right_sum
            sum += 1 if root.val == p.val or root.val == q.val else 0
            if sum == 2:
                self.ans = root
                return 0
            return sum

        root = p
        while root.parent:
            root = root.parent
        helper(root)
        return self.ans
