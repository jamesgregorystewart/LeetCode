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
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(solution.dailyTemperatures([30, 40, 50, 60]))
