from typing import List

"""
Inequalities
nums1[i] + nums1[j] > nums2[i] + nums2[j]
nums1[i] - nums2[i] > nums2[j] - nums1[j]

nums1[i] + nums1[j] - (nums2[i] + nums2[j]) > 0

"""


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        differences = [nums1[i] - nums2[i] for i in range(N)]
        differences.sort()

        pairs = 0
        left, right = 0, N - 1
        while left < right:
            if differences[left] + differences[right] > 0:
                pairs += right - left
                right -= 1
            else:
                left += 1
        return pairs
