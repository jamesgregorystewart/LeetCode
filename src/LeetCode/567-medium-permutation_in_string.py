""" 567. MEDIUM Permutation in String """

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#  
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#  
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

"""
Idea:
    - Make key_map of frequencies in s1
    - Move window of size len(s1) across s2, checking for equivalence with dynamic freq_map

Time: O(n)
Space: O(n)
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False
        
        # Create maps
        key_map = dict(Counter(s1))
        l, r = 0, len(s1)
        while r <= len(s2):
            seek_map = dict(Counter(s2[l:r]))
            print(seek_map)
            if key_map == seek_map:
                return True
            l, r = l + 1, r + 1

        return False

solution = Solution()
# print(solution.checkInclusion("ab", "eidbaooo"))
# print(solution.checkInclusion("ab", "eidboaoo"))
print(solution.checkInclusion("adc", "dcda"))

