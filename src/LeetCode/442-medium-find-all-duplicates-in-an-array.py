from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupes = set()
        i, n = 0, len(nums)
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            elif i != correct_idx and nums[i] == nums[correct_idx]:
                dupes.add(nums[i])
                i += 1
            else:
                i += 1
        return list(dupes)
