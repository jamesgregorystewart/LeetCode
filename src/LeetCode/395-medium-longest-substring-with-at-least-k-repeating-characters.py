from collections import Counter
import unittest


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        for c, v in counts.items():
            if v < k:
                return max(
                    [self.longestSubstring(sub, k) for sub in s.split(c)]
                    if len(s) >= k
                    else [0]
                )
        return len(s)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testKIsOne(self):
        self.assertEqual(self.solution.longestSubstring("abcdsa", 1), 6)

    def testExample(self):
        self.assertEqual(self.solution.longestSubstring(s="aaabb", k=3), 3)

    def testExample2(self):
        self.assertEqual(self.solution.longestSubstring(s="ababbc", k=2), 5)

    def testStringShorterThanK(self):
        self.assertEqual(self.solution.longestSubstring(s="a", k=2), 0)


if __name__ == "__main__":
    unittest.main()
