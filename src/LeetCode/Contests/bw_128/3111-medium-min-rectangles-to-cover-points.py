from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        print(points)
        rectangles = 0
        prev_rectangle = None
        for x, _ in points:
            if not prev_rectangle or w < (x - prev_rectangle[0]):
                prev_rectangle = [x, x]
                rectangles += 1
                continue
            prev_rectangle[1] = x
        return rectangles
