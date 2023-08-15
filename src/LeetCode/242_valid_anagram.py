# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#  
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#  
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#  
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''
O(n) / O(n)

Idea: create two maps of char counts to compare for equivalence

1) check length
2) iterate pointer through strings and maintain two hashmaps of char counts

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}
        counter = 0
        while counter < len(s):
            if s[counter] not in s_chars:
                s_chars[s[counter]] = 1
            else:
                s_chars[s[counter]] += 1

            if t[counter] not in t_chars:
                t_chars[t[counter]] = 1
            else:
                t_chars[t[counter]] += 1

            counter += 1
        return s_chars == t_chars

solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="anagram", t="nagara"))

