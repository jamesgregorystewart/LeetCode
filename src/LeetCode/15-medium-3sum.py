from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for left in range(n - 2):
            complements = {}
            target = 0 - nums[left]
            for it in range(left + 1, n):
                mid = target - nums[it]
                if mid in complements:
                    ans.append(tuple(sorted([nums[left], mid, nums[it]])))
                complements[nums[it]] = it
        return list(set(ans))
