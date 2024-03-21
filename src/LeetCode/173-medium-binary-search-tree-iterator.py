from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pointer = root
        while self.pointer and self.pointer.left:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left
        if self.pointer:
            self.stack.append(self.pointer)
            self.pointer.left = TreeNode(-1)
            self.pointer = self.pointer.left

    def next(self) -> int:
        if self.pointer and self.pointer.right:
            self.pointer = self.pointer.right
            while self.pointer and self.pointer.left:
                self.stack.append(self.pointer)
                self.pointer = self.pointer.left
        elif self.stack:
            self.pointer = self.stack.pop()
        else:
            print("something aint right")
        return self.pointer.val

    def hasNext(self) -> bool:
        if self.stack or (self.pointer and self.pointer.right):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
