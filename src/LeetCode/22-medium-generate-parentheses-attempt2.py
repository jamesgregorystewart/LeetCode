from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open, close, p) -> None:
            if len(p) == 2 * n:
                result.append("".join(p))
                return

            if open < n:
                p.append("(")
                backtrack(open + 1, close, p)
                p.pop()
            if close < open:
                p.append(")")
                backtrack(open, close + 1, p)
                p.pop()

        result = []
        backtrack(0, 0, [])
        return result
