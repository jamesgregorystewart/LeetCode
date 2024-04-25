from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = [0] * (len(nums))
        stack = []
        for i in range(len(nums)):
            mins[i] = i if i > 0 and nums[i] < nums[mins[i - 1]] else mins[i - 1]

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack and nums[mins[stack[-1]]] < nums[i]:
                return True

            stack.append(i)
        return False
