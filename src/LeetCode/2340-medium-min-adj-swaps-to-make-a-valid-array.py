from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        # find max and min element values
        min_v, max_v = min(nums), max(nums)
        min_i = -1
        swaps = 0

        for i, num in enumerate(nums):
            if num == min_v:
                min_i = i
                swaps += i
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == max_v:
                swaps += n - 1 - i
                if min_i > i:
                    swaps -= 1
                break

        return swaps
