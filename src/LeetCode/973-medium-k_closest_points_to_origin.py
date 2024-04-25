from typing import List, Tuple
import heapq
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(point: List[int]) -> float:
            return sqrt(point[0] ** 2 + point[1] ** 2)

        max_heap: List[Tuple[float, List[int]]] = []
        for point in points:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-calc_distance(point), point))
            elif calc_distance(point) < -max_heap[0][0]:
                heapq.heappushpop(max_heap, (-calc_distance(point), point))

        return [point for (dist, point) in max_heap]


solution = Solution()
print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], k=2))


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))[:k]
