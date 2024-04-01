from typing import List, Dict
from collections import Counter, defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)
        for row in matrix:
            patterns[tuple(row)] += 1
            patterns[tuple([abs(1 - e) for e in row])] += 1
        return max(patterns.values())
