from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1 for _ in range(len(nums))]

        for _ in range(2):
            for i, num in enumerate(nums):
                while stack and nums[stack[-1]] < num:
                    popped = stack.pop()
                    ans[popped] = num
                stack.append(i)

        return ans
