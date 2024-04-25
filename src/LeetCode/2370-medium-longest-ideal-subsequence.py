class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for i in range(len(s)):
            cur = ord(s[i]) - ord("a")
            l, r = max(0, cur - k), min(cur + k + 1, 26)
            dp[cur] = 1 + max([dp[j] for j in range(l, r)])
        return max(dp)
