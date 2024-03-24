from typing import List
from collections import deque
from sortedcontainers import SortedList
import unittest


# O(N* KlogK) with sorted windows approach
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         if k == 1:
#             return [float(num) for num in nums]
#
#         def median(window) -> float:
#             sorted_window = sorted(window)
#             if not k % 2:
#                 median = (sorted_window[k // 2] + sorted_window[(k // 2) - 1]) / 2
#             else:
#                 median = sorted_window[k // 2]
#             return float(median)
#
#         window = deque(nums[:k])
#         ans: List[float] = [median(window)]
#
#         for num in nums[k:]:
#             window.popleft()
#             window.append(num)
#             ans.append(median(window))
#
#         return ans


# O(Nlog(k))
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        tree = SortedList()
        res: List[float] = []
        for i, num in enumerate(nums):
            tree.add(num)
            if len(tree) > k:
                tree.remove(
                    nums[i - k]
                )  # if this was a heap it would be O(k); this is log(K)
            if len(tree) == k:
                median = (
                    tree[k // 2] if k % 2 else (tree[k // 2 - 1] + tree[k // 2]) / 2
                )
                res.append(float(median))
        return res


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample(self):
        self.assertEqual(
            self.solution.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3),
            [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000],
        )

    def testExample2(self):
        self.assertEqual(
            self.solution.medianSlidingWindow(nums=[1, 2, 3, 4, 2, 3, 1, 4, 2], k=3),
            [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000],
        )

    def testKIsOne(self):
        self.assertEqual(
            self.solution.medianSlidingWindow(nums=[1, 2], k=1), [1.00000, 2.00000]
        )


if __name__ == "__main__":
    unittest.main()
