from typing import List

"""
1) sort
2) function for finding triplets with fixed i
3) iterate through nums

"""


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         def twoSum(nums, target, res) -> None:
#             seen = set()
#             for i in range(len(nums)):
#                 if target - nums[i] in seen:
#                     triplet = [-target, target - nums[i], nums[i]]
#                     res.append(triplet)
#                 seen.add(nums[i])
#
#         nums.sort()
#         result = []
#         for i in range(len(nums) - 2):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i - 1] != nums[i]:
#                 twoSum(nums[i + 1 :], 0 - nums[i], result)
#         return [list(triplet) for triplet in result]

"""
[-1,0,1,2,-1,-4]
"""


# O(N^2) / O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups, seen = set(), set(), set()
        for i in range(len(nums) - 2):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i + 1, len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in seen:
                        res.add(tuple(sorted([nums[i], nums[j], complement])))
                    seen.add(nums[j])
                seen.clear()
        return [list(trip) for trip in res]
