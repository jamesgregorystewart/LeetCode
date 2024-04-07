from typing import List

"""
[-1,2,1,-4] t= 1
-4 -1 1 2
"""


# O(N^2)
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#
#         def twoSumClosest(i_val, left, t) -> int:
#             closest_sum = float("inf")
#             right = len(nums) - 1
#             while left < right:
#                 diff = t - nums[left] - nums[right]
#                 closest_sum = (
#                     closest_sum
#                     if abs(target - closest_sum) < abs(diff)
#                     else i_val + nums[left] + nums[right]
#                 )
#                 if diff == 0:
#                     break
#                 if diff > 0:
#                     left += 1
#                 else:
#                     right -= 1
#             return closest_sum
#
#         nums.sort()
#         ans = float("inf")
#         for i in range(len(nums) - 2):
#             two_sum = twoSumClosest(nums[i], i + 1, target - nums[i])
#             ans = ans if abs(target - ans) < abs(target - two_sum) else two_sum
#         return ans


# more efficient and concise version of above
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
