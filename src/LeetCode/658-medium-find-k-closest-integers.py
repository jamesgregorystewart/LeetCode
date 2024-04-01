from typing import List
import unittest
import collections


# O (log(N) + K)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] > x:
                right = mid
            else:
                left = mid
        left_diff = abs(arr[left] - x)
        right_diff = abs(arr[right] - x)
        index = left if left_diff <= right_diff else right

        # now we expand outwards
        queue = collections.deque([arr[index]])
        left, right = index - 1, index + 1
        while len(queue) < k and left >= 0 and right < len(arr):
            if abs(arr[left] - x) <= abs(arr[right] - x):
                queue.appendleft(arr[left])
                left -= 1
            else:
                queue.append(arr[right])
                right += 1
        while len(queue) < k:
            if left >= 0:
                queue.appendleft(arr[left])
                left -= 1
            else:
                queue.append(arr[right])
                right += 1
        return list(queue)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample1(self):
        self.assertEqual(
            self.solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3),
            [1, 2, 3, 4],
        )

    def testExample2(self):
        self.assertEqual(
            self.solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1),
            [1, 2, 3, 4],
        )

    # def testExample3(self):
    #     self.assertEqual(self.solution.findClosestElements())
    # def testExample4(self):
    #     self.assertEqual(self.solution.findClosestElements())
    #


if __name__ == "__main__":
    unittest.main()
