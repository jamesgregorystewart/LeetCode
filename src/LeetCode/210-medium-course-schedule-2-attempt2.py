from typing import List
from collections import deque, defaultdict
import unittest


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order: List[int] = []

        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[prerequisite] += 0
            in_degree[course] += 1

        for i in range(numCourses):
            if i not in in_degree:
                in_degree[i] += 0

        queue = deque(
            [prerequisite for prerequisite, value in in_degree.items() if value == 0]
        )
        while queue:
            prerequisite = queue.popleft()
            order.append(prerequisite)
            del in_degree[prerequisite]
            for course in graph[prerequisite]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        return order if len(order) == numCourses else []


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testNoPrereqs(self):
        numCourses = 1
        prerequisites = []
        expected = [0]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)

    def testfindOrder(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)

    def testfindNoOrder(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = []
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
