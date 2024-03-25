from typing import List
import unittest


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        a, b, c = 0, 1, 2
        if nums[a] + nums[b] + nums[c] <= target:
            return 0
        

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution


if __name__ == "__main__":
    unittest.main() x
