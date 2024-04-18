from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, result):
            if not root:
                return
            dfs(root.left, result)
            has_left = root.left is not None
            has_right = root.right is not None
            if has_left ^ has_right:
                if has_left:
                    result.append(root.left.val)
                else:
                    result.append(root.right.val)
            dfs(root.right, result)

        result = []
        dfs(root, result)
        return result
