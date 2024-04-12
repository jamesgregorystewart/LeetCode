from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def dfs(lo, hi) -> bool:
            if self.i == len(preorder):
                return True

            root = preorder[self.i]
            if lo > root or root > hi:
                return False

            self.i += 1
            left = dfs(lo, root)
            right = dfs(root, hi)
            return left or right

        self.i = 0
        return dfs(float("-inf"), float("inf"))
