""" 22 MEDIUM Generate Parentheses """

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#  
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#  
#
# Constraints:
#
# 1 <= n <= 8

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(ans, "", 0, 0, n)
        return ans

    def backtrack(self, ans: List[str], cur: str, open: int, close: int, max: int) -> None:
        if len(cur) == 2 * max:
            ans.append(cur)
            return

        if open < max:
            self.backtrack(ans, cur + "(", open + 1, close, max)
        if close < open:
            self.backtrack(ans, cur + ")", open, close + 1, max)


solution = Solution()
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))
