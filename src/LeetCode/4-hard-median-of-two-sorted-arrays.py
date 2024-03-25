from typing import List
import unittest


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 or not nums2:
            nonempty = nums1 if nums1 else nums2
            return (
                nonempty[(len(nonempty) - 1) // 2]
                if len(nonempty) % 2
                else (
                    (nonempty[(len(nonempty) - 1) // 2] + nonempty[len(nonempty) // 2])
                    / 2
                )
            )
        n, m = len(nums1), len(nums2)
        odd = True if (n + m) % 2 else False
        a = b = 0
        while a < len(nums1) and b < len(nums2):
            smaller = a + b
            greater = m + n - smaller - 2
            if odd and smaller > greater:
                print("finding median of odd count")
                # find the odd median
                return float(min(nums1[a], nums2[b]))
            if not odd and smaller == greater:
                return (nums1[a] + nums2[b]) / 2
            if a < n - 1 and nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1

        return 0.0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testExample(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]), 2.00000
        )

    def testExample2(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]), 2.50000
        )

    def testAEmpty(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1=[], nums2=[2]), 2.00000
        )

    def testBEmpty(self):
        self.assertEqual(
            self.solution.findMedianSortedArrays(nums1=[1, 3], nums2=[]), 2.00000
        )


if __name__ == "__main__":
    unittest.main()
