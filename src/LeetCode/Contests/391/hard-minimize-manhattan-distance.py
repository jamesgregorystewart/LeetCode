from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def backtrack(max_val, indices) -> None:
            if len(indices == len(points) - 2):
                result = min(result, max_val)

        result = float("inf")
        backtrack(result, [])
        return result
