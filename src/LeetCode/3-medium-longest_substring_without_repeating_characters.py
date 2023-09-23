""" 3 MEDIUM Longest Substring Without Repeating Characters """

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
#
#  
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#  
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        window_set = set([s[l]])
        longest_substring = 1
        while r < len(s):
            if s[r] not in window_set :
                window_set.add(s[r])
            else:
                # We have hit a duplicate 
                longest_substring = max(longest_substring, len(window_set))
                while s[r] in window_set:
                    window_set.remove(s[l])
                    l += 1
                window_set.add(s[r])
            r += 1
        longest_substring = max(longest_substring, len(window_set))
        return longest_substring

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring(""))
print(solution.lengthOfLongestSubstring("a"))
print(solution.lengthOfLongestSubstring("aa"))
print(solution.lengthOfLongestSubstring("ab"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("abba"))
print(solution.lengthOfLongestSubstring("dvdf"))
