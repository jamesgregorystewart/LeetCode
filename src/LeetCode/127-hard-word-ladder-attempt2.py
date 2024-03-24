from typing import List
from collections import deque, defaultdict
import unittest


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                standardized = word[:i] + "*" + word[i + 1 :]
                graph[standardized].append(word)
        visited = set([beginWord])

        transformations = 1
        queue = deque([beginWord])
        while queue:
            band = len(queue)
            for _ in range(band):
                node = queue.popleft()
                for i in range(len(node)):
                    standardized = node[:i] + "*" + node[i + 1 :]
                    if standardized in graph:
                        for word in graph[standardized]:
                            if word == endWord:
                                return transformations + 1
                            if word not in visited:
                                visited.add(word)
                                queue.append(word)

            transformations += 1

        return 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testEndMissingWordList(self):
        self.assertEqual(
            self.solution.ladderLength(
                beginWord="hit",
                endWord="cog",
                wordList=["hot", "dot", "dog", "lot", "log"],
            ),
            0,
        )

    def testMissingWordList(self):
        self.assertEqual(
            self.solution.ladderLength(
                beginWord="hit",
                endWord="cog",
                wordList=[],
            ),
            0,
        )

    def testLadder(self):
        self.assertEqual(
            self.solution.ladderLength(
                beginWord="hit",
                endWord="cog",
                wordList=["hot", "dot", "dog", "lot", "log", "cog"],
            ),
            5,
        )


if __name__ == "__main__":
    unittest.main()
