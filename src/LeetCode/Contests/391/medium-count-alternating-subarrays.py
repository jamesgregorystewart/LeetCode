from typing import List


# O(n)
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:

        def addCount(left, right) -> None:
            length = right - left + 1
            self.ans += length * (length - 1) // 2

        prev = -1
        left = 0
        self.ans = 0
        for right in range(len(nums)):
            if nums[right] == prev:
                addCount(left, right)
                left = right
            else:
                prev = nums[right]

        addCount(left, len(nums))
        return self.ans
