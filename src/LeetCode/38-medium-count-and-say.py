from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"

        for _ in range(n - 1):
            next = ""
            left, right = 0, 0
            while right < len(prev):
                while right < len(prev) and prev[left] == prev[right]:
                    right += 1
                next += str(right - left) + prev[left]
                left = right
            prev = next

        return prev
