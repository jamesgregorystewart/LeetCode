from typing import List
import unittest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                # answer is on the right
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample1(self):
        self.assertEqual(self.solution.findMin(nums=[1, 3, 5]), 1)

    def testExample2(self):
        self.assertEqual(self.solution.findMin(nums=[2, 2, 2, 0, 1]), 0)


if __name__ == "__main__":
    pass
