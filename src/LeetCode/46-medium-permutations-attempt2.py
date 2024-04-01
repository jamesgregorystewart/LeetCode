from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(perm) -> None:
            if len(perm) == len(nums):
                permutations.append(perm[:])
                return

            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm)
                    perm.pop()

        permutations = []
        backtrack([])
        return permutations
