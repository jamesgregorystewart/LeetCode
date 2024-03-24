from typing import List
from collections import defaultdict
import unittest


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        sequences = defaultdict(int)
        for i in range(9, len(s)):
            sequence = s[i - 9 : i + 1]
            sequences[sequence] += 1
        return [sequence for sequence, count in sequences.items() if count > 1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testShortS(self):
        self.assertEqual(self.solution.findRepeatedDnaSequences("ACCGT"), [])

    def testFound(self):
        self.assertEqual(
            self.solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),
            ["AAAAACCCCC", "CCCCCAAAAA"],
        )


if __name__ == "__main__":
    unittest.main()
