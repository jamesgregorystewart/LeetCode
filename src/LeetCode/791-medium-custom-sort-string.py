from typing import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = Counter(s)
        ans = []

        for c in order:
            if c in s_counts:
                ans.extend([c] * s_counts[c])
                del s_counts[c]
        for c, count in s_counts.items():
            ans.extend([c] * count)
        return "".join(ans)
