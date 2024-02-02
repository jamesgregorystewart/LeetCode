# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#
# Return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.

"""
iterate from right looking for the final occurence of the first char.
- while iterating maintain a map of the final index of every character encountered.
- the first substring will end at the max index from all the chars between the first character's first and last occurence.
- Same process will be followed for each subsequent set, except now we already have the map so we just continually find the max index from all characters between the first and last index of the next beginning character
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_index = {c: i for i, c in enumerate(s)}
        ans = []
        prev = -1
        segment_boundary = max_index[s[0]]
        for i, c in enumerate(s):
            segment_boundary = max(segment_boundary, max_index[c])
            if i == segment_boundary:
                ans.append(segment_boundary - prev)
                prev = segment_boundary
        return ans


solution = Solution()
print(solution.partitionLabels(s="ababcbacadefegdehijhklij"))
print(solution.partitionLabels(s="eccbbbbdec"))
