from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans: List[float] = []
        queue = deque([root])
        while queue:
            level = len(queue)
            sum = 0
            for _ in range(level):
                node = queue.popleft()
                sum += node.val if node else 0
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)

            ans.append(sum / level)
        return ans
