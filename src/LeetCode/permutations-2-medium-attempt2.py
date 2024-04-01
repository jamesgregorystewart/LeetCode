from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm, count) -> None:
            if len(perm) == len(nums):
                permutations.append(perm[:])
                return

            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    backtrack(perm, count)
                    perm.pop()
                    count[num] += 1

        permutations = []
        backtrack([], collections.Counter(nums))
        return permutations
