from typing import List
import unittest


# Cycle Sort O(n) / O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] < n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1

        return n + 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample1(self):
        self.assertEqual(self.solution.firstMissingPositive(nums=[1, 2, 0]), 3)

    def testExample2(self):
        self.assertEqual(self.solution.firstMissingPositive(nums=[3, 4, -1, 1]), 2)

    def testExample3(self):
        self.assertEqual(self.solution.firstMissingPositive(nums=[7, 8, 9, 11, 12]), 1)


if __name__ == "__main__":
    unittest.main()
