from typing import List
import bisect

"""

[-4,-3,-2,0,0,1,3,5]   k = 2; mk = 6

"""


# O(NlogN + N^2logN)
# class Solution:
#     def threeSumSmaller(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         result = 0
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 big_i = bisect.bisect_left(nums, target - nums[i] - nums[j], lo=j + 1)
#                 if big_i <= j:
#                     break
#                 result += big_i - (j + 1)
#         return result


"""
-1 -1 -1 1
"""


# O(N^2) solution with two pointers and O(1) Memory
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        def twoSumSmaller(left, t) -> int:
            sum = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < t:
                    sum += right - left
                    left += 1
                else:
                    right -= 1
            return sum

        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            ans += twoSumSmaller(i + 1, target - nums[i])

        return ans
