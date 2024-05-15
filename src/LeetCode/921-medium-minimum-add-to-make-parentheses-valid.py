class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens, closes = 0, 0
        operations = 0

        for c in s:
            if c == ")":
                closes += 1
            if c == "(":
                opens += 1
            if closes > opens:
                opens += 1
                operations += 1
        operations += opens - closes if opens > closes else 0
        return operations
