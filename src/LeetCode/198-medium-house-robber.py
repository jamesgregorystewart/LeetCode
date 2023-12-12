from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for i in range(len(nums)-1, -1, -1):
            prev1, prev2 = max(prev1, prev2 + nums[i]), prev1
        return prev1


solution = Solution()
print(solution.rob(nums=[2,4,6,2,5]))
print(solution.rob(nums=[1,2,3,1]))
