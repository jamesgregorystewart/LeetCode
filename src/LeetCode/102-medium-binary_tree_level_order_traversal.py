# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def helper(node, depth, levels) -> None:
            if not node:
                return

            if depth < len(levels):
                levels[depth].append(node.val)
            else:
                levels.append([node.val])

            helper(node.left, depth + 1, levels)
            helper(node.right, depth + 1, levels)

        helper(root, 0, levels)
        return levels
