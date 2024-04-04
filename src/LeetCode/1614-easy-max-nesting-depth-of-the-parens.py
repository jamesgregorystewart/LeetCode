class Solution:
    def maxDepth(self, s: str) -> int:
        max_nest = nested = 0
        for c in s:
            if c == "(":
                nested += 1
                max_nest = max(max_nest, nested)
            if c == ")":
                nested -= 1
        return max_nest
