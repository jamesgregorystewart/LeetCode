# Given a string s, partition s such that every
# substring
#  of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.
#
#
#
# Example 1:
#
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
#
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.

from typing import List
import math


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i, cur):
            if i == len(s):
                ans.append(cur.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()

        def is_palindrome(t: str) -> bool:
            n = math.ceil(len(t) / 2)
            return t[:n] == t[-n:][::-1]

        ans: List[List[str]] = []
        backtrack(0, [])
        return ans


solution = Solution()
print(solution.partition(s="aab"))
