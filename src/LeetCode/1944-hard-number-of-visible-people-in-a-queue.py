from typing import List

"""

Input: heights =    [10,6,8,5,11,9]
Output:             [3,1,2,1,1,0]

[10,8,5]
[3,1,2,1,0,0]

"""


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)

        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] <= num:
                popped = stack.pop()
                ans[popped] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)

        return ans
