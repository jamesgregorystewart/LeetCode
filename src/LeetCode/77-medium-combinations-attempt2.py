from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(i, combo) -> None:
            if len(combo) == k:
                combinations.append(combo[:])
                return

            for num in range(i, n + 1):
                combo.append(num)
                backtrack(num + 1, combo)
                combo.pop()

        combinations = []
        backtrack(1, [])

        return combinations
