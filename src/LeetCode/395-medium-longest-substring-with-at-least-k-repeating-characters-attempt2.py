from collections import Counter
from typing import List


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(arr: List[str]) -> int:
            if not arr:
                return 0
            counts = Counter(arr)
            return max()

        return helper(list(s))
