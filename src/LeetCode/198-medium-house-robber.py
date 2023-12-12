from typing import List


# Pull/Standard Solution
"""
Here the pull is preferable because it is less vulnerable to
index out of bounds error based on empty input
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for i in range(len(nums)-1, -1, -1):
            prev1, prev2 = max(prev1, prev2 + nums[i]), prev1
        return prev1


# Push/Forward Solution
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         prev2, prev1 = nums[0], nums[1]
#         for i in range(2, len(nums)):
#             prev1, prev2 = max(prev1, prev2 + nums[i]), prev1
#         return prev1


solution = Solution()
print(solution.rob(nums=[2,4,6,2,5]))
print(solution.rob(nums=[1,2,3,1]))
