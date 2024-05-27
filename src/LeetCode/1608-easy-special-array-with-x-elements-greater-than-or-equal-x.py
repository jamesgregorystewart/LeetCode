from typing import List


"""
3 5 7 9 

3 5
"""


# O(NlogN)
# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort()
#
#         N = len(nums)
#         for i, num in enumerate(nums):
#             x = N - i
#             if num >= x and ((i > 0 and nums[i - 1] < x) or i == 0):
#                 return x
#         return -1


"""
prefix sum with frequencies. Reverse sum counts and return when i == sum of counts
Can use min of N and num as freq val since res can't be greater than N. All values
greater than N will be considered as N
"""


# O(N)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        freq = [0] * (N + 1)

        for num in nums:
            freq[min(N, num)] += 1

        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i

        return -1
