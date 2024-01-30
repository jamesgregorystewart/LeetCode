# # Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
# Constraints:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(sum_set, cur_sum, index):
            if cur_sum == target:
                ans.append(sum_set.copy())
                return
            elif cur_sum > target:
                return
            for i in range(index, len(candidates)):
                c = candidates[i]
                if i != index and c == candidates[i - 1]:
                    continue
                backtrack(sum_set + [c], cur_sum + c, i + 1)

        ans: List[List[int]] = []
        backtrack([], 0, 0)
        return ans


solution = Solution()
print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
