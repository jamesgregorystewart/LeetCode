from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def successor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root.right
        while node and node.left:
            node = node.left
        return node.val

    def predecessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root.left
        while node and node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # delete the node
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
        return root
