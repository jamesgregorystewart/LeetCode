# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
#
#
#
# Example 1:
#
#
#
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:
#
#
#
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:
#
#
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
#
#
# Constraints:
#
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

from typing import List
import heapq


# Dijkstra's Algorithm
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Add all edges into priorityqueue which will give us the next best edge, greedily to take
        """
        pq = [(0, 0, 0)]
        visited = [[False] * len(heights[0]) for _ in range(len(heights))]
        min_effort = 0

        def get_neighbors(x, y):
            moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for move in moves:
                new_row, new_col = x + move[0], y + move[1]
                if (
                    0 <= new_row < len(heights)
                    and 0 <= new_col < len(heights[0])
                    and not visited[new_row][new_col]
                ):
                    yield (new_row, new_col)

        while pq:
            node = heapq.heappop(pq)
            min_effort = max(min_effort, node[0])
            if node[1] == len(heights) - 1 and node[2] == len(heights[0]) - 1:
                return min_effort
            for x, y in get_neighbors(node[1], node[2]):
                effort = abs(heights[node[1]][node[2]] - heights[x][y])
                heapq.heappush(pq, (effort, x, y))
            visited[node[1]][node[2]] = True

        return min_effort


solution = Solution()
print(solution.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(solution.minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(
    solution.minimumEffortPath(
        heights=[
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
    )
)
