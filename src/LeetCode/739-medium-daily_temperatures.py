""" 739 MEDIUM Daily Temperatures """

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
#  
#
# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
#
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
#
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#  
#
# Constraints:
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

"""
Tricks:
    - Use of monotonic stack which stores the indices of the temperatures, since that is what we actually care about,
    and the indices serve as lookup to temperature from the input
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for cur_day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = cur_day - prev_day
            stack.append(cur_day)

        return ans

solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(solution.dailyTemperatures([30,40,50,60]))
