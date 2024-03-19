# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

"""
Intuition:
Work through word backwards. When a word made from the substring s[len(s)-i:] is found in the dict, and that word concatenated with the word that starts after the end of the found word makes up the rest of the string s, then add that concatened word to dp[i].

States:
1) all substrings of length i from len(s) - i to end made up of words from word dict.
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp: List[str] = [""] * (len(s) + 1)
        # Iterate over all states
        for i in range(len(s) + 1, -1, -1):
            # iterate over all possible words; there could be multiple per i
            for word in wordDict:
                if (
                    len(word) <= len(s) - i
                    and word == s[i : i + len(word)]
                    and len(word) + len(dp[i + len(word)]) == len(s) - i
                ):
                    dp[i] = word + dp[i + len(word)]
        return dp[0] == s


solution = Solution()
print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(solution.wordBreak(s="abcd", wordDict=["a", "abc", "b", "cd"]))
