from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %= k
            if remainder not in remainders:
                remainders[remainder] = i
            elif i - remainders[remainder] >= 2:
                return True
        return False
