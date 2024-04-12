from typing import List, Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_map = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                col_map[col].append(node.val)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        min_col, max_col = min(col_map.keys()), max(col_map.keys())
        res = []
        for col in range(min_col, max_col + 1):
            res.append(col_map[col])
        return res
