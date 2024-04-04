"""
10000
01000
00100
00010
00001
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        ans = [0, 0]
        for i in range(len(s)):
            dp[i][i] = 1

        # do the two length
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ans = [i, i + 1]

        # do 3 + length palindromes
        for diff in range(2, len(s)):
            for i in range(len(s) - diff):
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    ans = [i, i + diff]
                    dp[i][i + diff] = 1
        return s[ans[0] : ans[1] + 1]


sol = Solution()
sol.longestPalindrome("babad")
