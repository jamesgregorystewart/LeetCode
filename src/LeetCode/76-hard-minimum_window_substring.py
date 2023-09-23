""" 76 HARD Minimum Window Substring """


# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
#  
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#  
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#  
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?

"""
Idea:
    - Two frequency maps, when the larger contains the smaller, shrink the larger till it's minimally
        equivalent to the smaller map

Time: O(n + m)
Space: O(n)

Optimizations:
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        key_map = dict(Counter(t))
        l = r = 0
        window_map = {}
        formed = 0
        min_window_substring = s
        while r < len(s):
            if s[r] in key_map.keys():
                window_map[s[r]] = window_map.get(s[r], 0) + 1
                formed = formed + 1 if window_map[s[r]] == key_map[s[r]] else formed
                if formed == len(key_map):
                    while s[l] not in key_map.keys() or window_map[s[l]] > key_map[s[l]]:
                        if s[l] in key_map.keys():
                            window_map[s[l]] -= 1
                        l += 1
                    min_window_substring = s[l:r+1] if r-l+1 < len(min_window_substring) else min_window_substring
            r += 1
        return min_window_substring if formed == len(key_map) else ""

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("a", "a"))
print(solution.minWindow("a", "aa"))
print(solution.minWindow("a", "b"))
