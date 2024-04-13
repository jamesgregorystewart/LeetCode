from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            max_val = float("-inf")
            for j in range(i, n):
                max_val = max(max_val, nums[j])
            if nums[i] == nums[j] == max_val:
                ans += 1

        return ans


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
        n = len(nums)
        ans = n

        for i, num in enumerate(nums):
            index_map[num].append(i)

        for val, indices in index_map.items():
            maxes = [0 for _ in range(len(nums))]
            if len(indices) > 1:
                for i in range(len(indices) - 1):
                    max_val = nums[indices[i]]
                    for j in range(i + 1, len(indices)):
                        for k in range(indices[i], indices[j] + 1):
                            max_val = max(max_val, nums[k])
                            maxes[k] = max(maxes[k], nums[k])
                        if max_val == val:
                            ans += 1

        return ans
