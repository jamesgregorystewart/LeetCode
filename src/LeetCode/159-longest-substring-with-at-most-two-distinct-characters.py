from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = ans = 0
        counts = defaultdict(int)
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > 2:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
