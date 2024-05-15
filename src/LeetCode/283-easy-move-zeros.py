from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z_ptr, ptr = 0, 0
        while z_ptr < len(nums) and ptr < len(nums):
            while nums[z_ptr] != 0:
                z_ptr += 1
                if z_ptr == len(nums):
                    return
            while ptr < z_ptr or nums[ptr] == 0:
                ptr += 1
                if ptr == len(nums):
                    return
            if z_ptr < len(nums) and ptr < len(nums):
                nums[z_ptr], nums[ptr] = nums[ptr], nums[z_ptr]
