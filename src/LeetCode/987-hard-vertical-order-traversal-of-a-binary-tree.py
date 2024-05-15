import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_col = 0
        self.max_col = 0

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def inorder(root, r, c) -> None:
            if not root:
                return

            inorder(root.left, r + 1, c - 1)
            columns[c].append((r, c, root.val))
            self.min_col = min(self.min_col, c)
            self.max_col = max(self.max_col, c)
            inorder(root.right, r + 1, c + 1)

        columns = collections.defaultdict(list)
        inorder(root, 0, 0)

        ans = [[] for _ in range(self.max_col - self.min_col + 1)]
        for c, tuples in columns.items():
            ans[c - self.min_col].extend([v for _, _, v in sorted(tuples)])

        return ans
