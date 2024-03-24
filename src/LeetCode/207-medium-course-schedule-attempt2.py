from typing import List, Dict
from collections import defaultdict, deque
import unittest

"""
Space: O(M + N)
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or not prerequisites:
            return True

        adj_list = defaultdict(list)
        in_degree = defaultdict(int)

        # O(M); M is between N-1 and N*(N-1) or 2N or N
        for course, prerequisite in prerequisites:
            adj_list[prerequisite].append(course)
            in_degree[prerequisite] += 0
            in_degree[course] += 1

        # O(N) to look through all the courses and their indegrees
        queue = deque([course for course, degree in in_degree.items() if degree == 0])
        # O(N) because you are traversing through all of the edges in the graph of which
        # there are at most N*(N-1) -> 2N -> N
        while queue:
            prerequisite = queue.popleft()
            del in_degree[prerequisite]
            for course in adj_list[prerequisite]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return not in_degree


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testNoPrereqs(self):
        self.assertEqual(self.solution.canFinish(1, []), True)

    def testDoesFinish(self):
        self.assertEqual(self.solution.canFinish(2, [[1, 0]]), True)

    def testDoesntFinish(self):
        self.assertEqual(self.solution.canFinish(2, [[1, 0], [0, 1]]), False)


if __name__ == "__main__":
    unittest.main()
