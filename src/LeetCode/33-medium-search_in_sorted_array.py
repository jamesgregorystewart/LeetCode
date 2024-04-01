from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:
                # left side is sorted
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right side is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample(self):
        self.assertEqual(self.solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0), 4)

    def testExample2(self):
        self.assertEqual(self.solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3), -1)

    def testExample3(self):
        self.assertEqual(self.solution.search(nums=[1], target=0), -1)


if __name__ == "__main__":
    unittest.main()
