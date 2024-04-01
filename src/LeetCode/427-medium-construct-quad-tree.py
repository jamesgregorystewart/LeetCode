from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def is_uniform(grid):
            return all(
                grid[i][j] == grid[0][0]
                for i in range(len(grid))
                for j in range(len(grid[0]))
            )

        if is_uniform(grid):
            return Node(val=grid[0][0], isLeaf=True)

        n = len(grid)
        half = n // 2

        # Correctly slice the 2D grid into four parts
        top_left_grid = [row[:half] for row in grid[:half]]
        top_right_grid = [row[half:] for row in grid[:half]]
        bottom_left_grid = [row[:half] for row in grid[half:]]
        bottom_right_grid = [row[half:] for row in grid[half:]]

        node = Node(
            val=1,
            isLeaf=False,
            topLeft=self.construct(top_left_grid),
            topRight=self.construct(top_right_grid),
            bottomLeft=self.construct(bottom_left_grid),
            bottomRight=self.construct(bottom_right_grid),
        )

        return node
