class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while len(s) > 1 and i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2 :]
                i = max(0, i - 1)
            else:
                i += 1
        return s


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
