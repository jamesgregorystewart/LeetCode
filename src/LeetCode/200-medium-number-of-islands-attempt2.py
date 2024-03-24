from typing import List, Tuple
import collections
import unittest
import copy


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def sink(queue) -> None:
            self.islands += 1
            moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            while queue:
                coord = queue.popleft()
                for move in moves:
                    x, y = coord[0] + move[0], coord[1] + move[1]
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                        grid[x][y] = "0"  # key is to set to 0 as you find the neighbors
                        queue.append((x, y))

        self.islands = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    sink(collections.deque([(i, j)]))
        return self.islands


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.grid = [["0"] * 5 for _ in range(5)]

    def test_empty_grid(self):
        self.assertEqual(self.solution.numIslands([]), 0)

    def test_no_islands(self):
        grid = [["0"] * 3 for _ in range(3)]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_no_land(self):
        grid = [["1"] * 3 for _ in range(3)]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_one_island(self):
        grid = [["0"] * 3 for _ in range(3)]
        grid[1][1] = "1"
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_multiple_disconnected_islands(self):
        t_grid = copy.deepcopy(self.grid)
        t_grid[0][1] = "1"
        t_grid[1][1] = "1"
        t_grid[2][2] = "1"
        self.assertEqual(self.solution.numIslands(t_grid), 2)


if __name__ == "__main__":
    unittest.main()
