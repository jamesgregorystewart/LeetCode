from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def countSmaller(mid, smaller, larger):
            n = len(matrix)
            row, col = n - 1, 0
            count = 0
            while row >= 0 and col < n:
                val = matrix[row][col]
                if val > mid:
                    row -= 1
                    larger = min(larger, val)
                else:
                    count += row + 1
                    col += 1
                    smaller = max(smaller, val)
            return count, smaller, larger

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) // 2
            count, smaller, larger = countSmaller(mid, start, end)
            if count == k:
                return smaller
            if count < k:
                start = larger
            if count > k:
                end = smaller
        return start
