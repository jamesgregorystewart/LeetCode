from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur, start, cur_sum) -> None:
            if cur_sum == target:
                result.append(cur[:])
            if cur_sum >= target:
                return
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                cur_sum += candidates[i]
                backtrack(cur, i, cur_sum)
                cur.pop()
                cur_sum -= candidates[i]

        result = []
        backtrack([], 0, 0)
        return result
