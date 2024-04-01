from typing import List
import unittest

"""
We use the second Binary Search Template because it means we only have to do one adjacent cell check. Since we know it doesn't increase going right, we include mid (which could be the answer) in the next binary search on the left side, so that element stays in contention. If we moved right = mid - 1 and exited on left <= right we would have to also check to see if the left side increased or decreased, and return mid if we were at a peak. Less complexity with this approach.
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()


if __name__ == "__main__":
    unitest.main()
