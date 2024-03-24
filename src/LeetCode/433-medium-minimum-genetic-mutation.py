from typing import List
import collections
import unittest


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if not bank:
            return -1
        mutations = 0
        queue = collections.deque([startGene])
        visited = set()
        visited.add(startGene)
        while queue:
            band = len(queue)
            mutations += 1
            for _ in range(band):
                gene = queue.popleft()
                for i in range(8):
                    for letter in ["A", "C", "G", "T"]:
                        if letter == gene[i]:
                            continue
                        mutation = gene[:i] + letter + gene[i + 1 :]
                        if mutation not in visited and mutation in bank:
                            if mutation == endGene:
                                return mutations
                            visited.add(mutation)
                            queue.append(mutation)

        return -1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def testNoBank(self) -> None:
        self.assertEqual(
            self.solution.minMutation(
                startGene="AACCGGTT", endGene="AACCGGTA", bank=[]
            ),
            -1,
        )

    def testNumberOfMutations(self):
        self.assertEqual(
            self.solution.minMutation(
                startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"]
            ),
            1,
        )

    def testNumberOfMutationsTwo(self):
        self.assertEqual(
            self.solution.minMutation(
                startGene="AACCGGTT",
                endGene="AAACGGTA",
                bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"],
            ),
            2,
        )

    def testNoPath(self):
        self.assertEqual(
            self.solution.minMutation(
                startGene="AACCGGTT",
                endGene="AAACGGGG",
                bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"],
            ),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
