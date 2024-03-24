from typing import List
from collections import deque
import unittest

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
                
        
        

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testNoBoard(self):
        board = [[]]
        self.assertEqual(self.solution.snakesAndLadders(board), 0)

if __name__ == "__main__":
    unittest.main()
