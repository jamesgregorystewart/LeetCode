from typing import List
import unittest


# O(log(N)) solution; we will binary search to find pivot, then binary search to find target
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                # dont know where we stand
                right -= 1
            elif nums[mid] > nums[right]:
                # left hand side is sorted
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right hand side is sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample(self):
        self.assertEqual(
            self.solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0), True
        )

    def testExample2(self):
        self.assertEqual(
            self.solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3), False
        )

    def testExample3(self):
        self.assertEqual(
            self.solution.search(nums=[6, 0, 0, 1, 2, 2, 3, 5], target=3), True
        )

    def testEmptyNums(self):
        self.assertEqual(self.solution.search(nums=[], target=1), False)

    def testTargetTooBig(self):
        self.assertEqual(
            self.solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=7), False
        )

    def testTargetTooSmall(self):
        self.assertEqual(
            self.solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=-1), False
        )


if __name__ == "__main__":
    unittest.main()
