from typing import List
import unittest


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroFound = False
        l, r = 0, -1
        zero_ptr = -1
        ans = 0
        while r < len(nums) - 1:
            r += 1
            if not nums[r]:
                if zeroFound:
                    ans = max(ans, r - l)
                    l = zero_ptr + 1
                zeroFound = True
                zero_ptr = r

        ans = max(ans, r - l + 1)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testNoZeros(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums=[1, 1, 1, 1, 1]), 5)

    def testNoOnes(self):
        self.assertEqual(
            self.solution.findMaxConsecutiveOnes(nums=[0, 0, 0, 0, 0, 0]), 1
        )

    def testExample(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0]), 4)

    def testExample2(self):
        self.assertEqual(
            self.solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]), 4
        )


if __name__ == "__main__":
    unittest.main()
