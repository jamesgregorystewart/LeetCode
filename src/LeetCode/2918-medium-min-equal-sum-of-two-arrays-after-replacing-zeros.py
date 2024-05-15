from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        num1_zeros, num1_sum = 0, 0
        for num in nums1:
            num1_sum += num
            num1_zeros += 1 if num == 0 else 0

        num2_zeros, num2_sum = 0, 0
        for num in nums2:
            num2_sum += num
            num2_zeros += 1 if num == 0 else 0

        if (num1_sum + num1_zeros > num2_sum and num2_zeros == 0) or (
            num2_sum + num2_zeros > num1_sum and num1_zeros == 0
        ):
            return -1

        return max(num1_zeros + num1_sum, num2_zeros + num2_sum)
