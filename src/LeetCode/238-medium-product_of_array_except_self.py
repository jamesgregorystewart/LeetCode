from typing import List


# class SolutionNSpeed:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = [1] * len(nums)
#
#         left, right = 1, 1
#         for i in range(len(nums)):
#             ans[i] *= left
#             ans[~i] *= right
#
#             left *= nums[i]
#             right *= nums[~i]
#
#         return ans

# solution_n_speed = SolutionNSpeed()
# print(solution_n_speed.productExceptSelf(nums=[1, 2, 3, 4]))


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_arr, r_arr = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            l_arr[i] = l_arr[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            r_arr[i] = r_arr[i + 1] * nums[i + 1]

        # compute
        ans: List[int] = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = l_arr[i] * r_arr[i]
        return ans
