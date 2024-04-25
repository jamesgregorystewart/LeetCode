from math import inf
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_count = [(0, -inf, inf)] * len(s)
        for i, c in enumerate(s):
            if i > 0:
                count, prev, next = candle_count[i - 1]
                candle_count[i] = (count, prev + 1, next - 1)
            if c == "|":
                count, prev, next = candle_count[i]
                candle_count[i] = (count + 1, 0, 0)
        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1:
                count, prev, next = candle_count[i + 1]
                candle_count[i] = (count, prev - 1, next + 1)
            if s[i] == "|":
                count, prev, next = candle_count[i]
                candle_count[i] = (count, 0, 0)

        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            ans[i] = (
                query[1]
                - candle_count[query[1]][1]
                - query[0]
                + candle_count[query[0]][2]
                - candle_count[query[1]][0]
                + candle_count[query[0]][0]
            )
            ans[i] = 0 if ans[i] in [inf, -inf] else ans[i]
        return ans
