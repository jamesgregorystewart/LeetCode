"""
Remove:
- close before open
- remaining opens at end
"""

from typing import List


# O(N) / O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # left to right
        close = 0
        opens: List[int] = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == ")":
                close += 1
                if close > len(opens):
                    s = s[:i] + s[i + 1 :]
                    close -= 1
                    continue
                elif opens:
                    close -= 1
                    opens.pop()
            if c == "(":
                opens.append(i)
            i += 1
        while opens:
            index = opens.pop()
            s = s[:index] + s[index + 1 :]
        return s
