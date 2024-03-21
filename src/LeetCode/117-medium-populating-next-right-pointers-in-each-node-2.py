# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        head = root

        def helper(root):
            if not root:
                return

            def findNext(root):
                while root:
                    if root.left:
                        return root.left
                    if root.right:
                        return root.right
                    root = root.next
                return None

            if root.left and root.right:
                root.left.next = root.right
            elif root.left:
                root.left.next = findNext(root.next)
            if root.right:
                root.right.next = findNext(root.next)
            helper(root.right)
            helper(root.left)

        helper(root)
        return head
