from collections import deque
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack, ans = deque(), [0] * n
        for log in logs:
            id, action, timestamp = log.split(":")
            id, timestamp = int(id), int(timestamp)
            if action == "start":
                stack.append((id, timestamp))
            else:
                id, initTime = stack.pop()
                elapsedTime = timestamp + 1 - initTime
                ans[id] += elapsedTime

                if stack:
                    ans[stack[-1][0]] -= elapsedTime

        return ans
