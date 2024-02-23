# Given a string s, return the longest
# palindromic
#
# substring
#  in s.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        ans = [0, 0]
        # do the two-length palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ans = [i, i + 1]

        # do the 3+ length palindromes
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    ans = [i, j]
                    dp[i][j] = 1

        i, j = ans
        return s[i : j + 1]


solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("racecar"))
print(solution.longestPalindrome("aaaa"))
print(solution.longestPalindrome("aaaaa"))
