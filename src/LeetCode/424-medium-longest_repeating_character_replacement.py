""" 424 Medium Longest Repeating Character Replacement """

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#  
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.
#  
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

"""
Time: O(n)
Space: O(n)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l, r = 0, 0
        max_replacement = 0
        while r < len(s):
            window_size = r-l+1
            if s[r] in freq_map:
                freq_map[s[r]] += 1
            else:
                freq_map[s[r]] = 1
            max_key = max(freq_map, key=freq_map.get)
            max_frequency = freq_map[max_key]
            while (r-l+1)-max_frequency > k:
                max_key = max(freq_map, key=freq_map.get)
                max_frequency = freq_map[max_key]
                freq_map[s[l]] -= 1
                l += 1
            max_replacement = max(max_replacement, r-l+1)
            r += 1
        return max_replacement

solution = Solution()
print(solution.characterReplacement("ABAB", 2))
print(solution.characterReplacement("AABABBA", 1))
print(solution.characterReplacement("AA", 2))

