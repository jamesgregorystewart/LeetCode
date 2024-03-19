from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = len(points)
        points.sort()
        hi = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= hi:
                arrows -= 1
                hi = min(hi, points[i][1])
            else:
                hi = points[i][1]
        return arrows
