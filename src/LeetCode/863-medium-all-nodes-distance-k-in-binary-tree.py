# Definition for a binary tree node.1
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


r"""
        3
       / \
      /   \
     5     1
    / \   / \
   6   2 0   8
  / \
 7   4
"""


# O(N) convert to graph
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def inorder(prev, root):
            if root:
                root.parent = prev
                inorder(root, root.left)
                inorder(root, root.right)

        inorder(None, root)
        q = collections.deque([target])
        seen = set()
        seen.add(target)
        ans = []
        dist = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if dist == k:
                    ans.append(node.val)
                    continue
                for adj in [node.parent, node.left, node.right]:
                    if adj and adj not in seen:
                        seen.add(adj)
                        q.append(adj)
            dist += 1
        return ans
