from typing import List
import unittest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()


if __name__ == "__main__":
    unittest.main()
