# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#  
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#  
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#  
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

'''
Idea: create total product of all nums, keep count of zeros, keep count of negatives

O(nlog(m)) / O(1)
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        negative_count = 0
        total_product = 1
        
        for num in nums: # O(n)
            if num == 0:
                zero_count += 1
                continue
            elif num < 0:
                negative_count += 1
            total_product *= abs(num)
            
        for i, num in enumerate(nums):
            if num == 0 and zero_count == 1:
                nums[i] = total_product if negative_count % 2 == 0 else total_product*-1
            elif zero_count > 0:
                nums[i] = 0
            else:
                nums[i] = self.divide(dividend=abs(total_product), divisor=abs(num))
                nums[i] *= -1 if self.is_negative(negative_count, num) else 1

        return nums

    def is_negative(self, negative_count: int, num:int) -> bool:
        if (negative_count % 2 == 1 and num > 0) or (negative_count % 2 == 0 and num < 0):
            return True

        return False

    def divide(self, dividend: int, divisor: int):
        quotient = 0
        while dividend >= divisor:
            current_divisor = divisor
            multiple = 1

            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1

            dividend -= current_divisor
            quotient += multiple

        return quotient


solution = Solution()
# print(solution.productExceptSelf(nums = [1,2,3,4]))
# print(solution.productExceptSelf(nums = [1,-1]))
# print(solution.productExceptSelf(nums = [-1,1,0,-3,3]))

class SolutionNSpeed:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
       
        left, right = 1, 1
        for i in range(len(nums)):
            ans[i] *= left
            ans[~i] *= right
            
            left *= nums[i]
            right *= nums[~i]
            
        return ans

solution_n_speed = SolutionNSpeed()
print(solution_n_speed.productExceptSelf(nums = [1,2,3,4]))
