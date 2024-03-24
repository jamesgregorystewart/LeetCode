from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        counts = defaultdict(int)
        ans = 0
        while r < len(s):
            counts[s[r]] += 1
            ans = max(ans, r - l)
            while counts[s[r]] > 2:
                counts[s[l]] -= 1
                l += 1
            r += 1
        ans = max(ans, r - l)
        return ans


solution = Solution()
print(solution.maximumLengthSubstring(s="bcbbbcba"))
print(solution.maximumLengthSubstring(s="aaaa"))
print(solution.maximumLengthSubstring(s="acedc"))
print(solution.maximumLengthSubstring(s="eebadadbfa"))
