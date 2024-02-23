# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
#
# Example 1:
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.


# DP solution O(N^2) / O(N^2)
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         ans = n
#         dp = [[0] * n for _ in range(n)]
#
#         for i in range(n):
#             dp[i][i] = 1
#
#         # 2-length
#         for i in range(n - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = 1
#                 ans += 1
#
#         # 3+ length
#         for diff in range(2, n):
#             for i in range(n - diff):
#                 j = i + diff
#                 if s[i] == s[j] and dp[i + 1][j - 1]:
#                     dp[i][j] = 1
#                     ans += 1
#
#         return ans


# Expand around Center O(N^2) / O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        self.n = len(s)
        for i in range(self.n - 1):
            ans += self.expand(s, i, i)
            ans += self.expand(s, i, i + 1)
        ans += self.expand(s, self.n - 1, self.n - 1)

        return ans

    def expand(self, ss: str, lo: int, hi: int) -> int:
        res = 0
        while lo >= 0 and hi < self.n:
            if ss[lo] != ss[hi]:
                break
            lo -= 1
            hi += 1
            res += 1
        return res


solution = Solution()
print(solution.countSubstrings("abc"))
print(solution.countSubstrings("aaa"))
print(solution.countSubstrings("a"))
print(solution.countSubstrings(""))
print(solution.countSubstrings("abbac"))
