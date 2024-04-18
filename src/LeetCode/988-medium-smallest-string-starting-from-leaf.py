from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Brute Force Solution: O(N) / O(N)
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, path, result) -> None:
            if not root:
                return

            path.append(root.val)
            dfs(root.left, path, result)
            if not root.left and not root.right:
                result.append(list(reversed(path[:])))
            dfs(root.right, path, result)
            path.pop()

        paths = []
        dfs(root, [], paths)
        return "".join([chr(c + 97) for c in sorted(paths)[0]])


# space optimized but not as fast in practice: O(N) / O(1)
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, path) -> None:
            if not root:
                return

            path.append(root.val)
            dfs(root.left, path)
            if not root.left and not root.right:
                path_code = "".join([chr(c + 97) for c in list(reversed(path[:]))])
                if not self.ans:
                    self.ans = path_code
                else:
                    norm_length = min(len(path), len(self.ans))
                    if self.ans[:norm_length] > path_code[:norm_length] or (
                        self.ans[:norm_length] == path_code[:norm_length]
                        and len(path_code) < len(self.ans)
                    ):
                        self.ans = path_code
            dfs(root.right, path)
            path.pop()

        self.ans = None
        dfs(root, [])
        return self.ans
