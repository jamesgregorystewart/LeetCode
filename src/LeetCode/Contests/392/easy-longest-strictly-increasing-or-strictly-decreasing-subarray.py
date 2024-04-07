from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 1
        prev = None
        increasing = False
        for right, num in enumerate(nums):
            if not prev:
                prev = num
                continue
            if right - left == 1:
                if num == prev:
                    left = right
                else:
                    increasing = True if num > prev else False
                    ans = max(ans, 2)
            elif (
                num == prev
                or (num > prev and not increasing)
                or (num < prev and increasing)
            ):
                ans = max(ans, right - left)
                if num == prev:
                    left = right
                else:
                    left = right - 1
                    increasing = True if num > prev else False
            if right == len(nums) - 1:
                ans = max(ans, right - left + 1)
            prev = num
        return ans


solution = Solution()
print(solution.longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]))
print(solution.longestMonotonicSubarray(nums=[3, 3, 3, 3]))
print(solution.longestMonotonicSubarray(nums=[3, 2, 1]))
print(solution.longestMonotonicSubarray(nums=[1, 5, 2, 7]))
print(solution.longestMonotonicSubarray(nums=[1, 5, 10, 3]))
