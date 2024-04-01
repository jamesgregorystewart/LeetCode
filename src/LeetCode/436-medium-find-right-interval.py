from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted(
            [[start, i] for i, (start, _) in enumerate(intervals)]
            + [[float("inf"), -1]]
        )
        return [
            sorted_intervals[bisect.bisect_left(sorted_intervals, [end, 0])][1]
            for _, end in intervals
        ]
