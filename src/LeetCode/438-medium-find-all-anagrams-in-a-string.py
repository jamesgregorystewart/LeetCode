from typing import List
import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = [0] * 26
        for c in p:
            p_counts[ord(c) - ord("a")] += 1
        n, m = len(s), len(p)

        s_counts = [0] * 26
        for c in s[:m]:
            s_counts[ord(c) - ord("a")] += 1
        ans: List[int] = []
        if p_counts == s_counts:
            ans.append(0)

        for i in range(1, n - m + 1):
            prev_c = s[i - 1]
            s_counts[ord(prev_c) - ord("a")] -= 1
            s_counts[ord(s[i + m - 1]) - ord("a")] += 1
            if p_counts == s_counts:
                ans.append(i)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testNothing(self):
        self.assertEqual(self.solution.findAnagrams(s="asdfewd", p="z"), [])

    def testExample1(self):
        self.assertEqual(self.solution.findAnagrams(s="cbaebabacd", p="abc"), [0, 6])

    def testExample2(self):
        self.assertEqual(self.solution.findAnagrams(s="abab", p="ab"), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
