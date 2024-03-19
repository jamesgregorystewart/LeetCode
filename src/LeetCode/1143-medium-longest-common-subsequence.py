# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
#
#
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
# Constraints:
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

"""
Time/Space: O(n*m)
"""

# Pull; this is more elegant b/c indices are consistent between inputs and dp
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
#
#         for i in range(len(text1)-1, -1, -1):
#             for j in range(len(text2)-1, -1, -1):
#                 if text1[i] == text2[j]:
#                     dp[i][j] = dp[i+1][j+1] + 1
#                 else:
#                     dp[i][j] = max(dp[i+1][j], dp[i][j+1])
#         return dp[0][0]


# Push
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]


from functools import lru_cache


# Top Down w/ memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(len(text1) - 1, len(text2) - 1)


solution = Solution()
print(solution.longestCommonSubsequence(text1="abcde", text2="ace"))
print(solution.longestCommonSubsequence(text1="abc", text2="abc"))
print(solution.longestCommonSubsequence(text1="abc", text2="def"))
print(solution.longestCommonSubsequence(text1="abcde", text2="be"))
print(solution.longestCommonSubsequence(text1="bsbininm", text2="jmjkbkjkv"))
