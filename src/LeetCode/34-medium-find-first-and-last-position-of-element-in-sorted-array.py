from typing import List
import unittest

"""
Idea: Two binary searches, one to find each index
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # Find the starting index
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] != target and nums[left] != target:
            return [-1, -1]
        ans = []
        if nums[left] == target:
            ans.append(left)
        else:
            ans.append(right)

        # seek end index
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            ans.append(right)
        else:
            ans.append(left)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample1(self):
        self.assertEqual(
            self.solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8), [3, 4]
        )

    def testExample2(self):
        self.assertEqual(
            self.solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1]
        )


if __name__ == "__main__":
    unittest.main()
