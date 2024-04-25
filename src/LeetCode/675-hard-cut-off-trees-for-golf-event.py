from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        sorted_forest = sorted(
            (v, r, c)
            for r, row in enumerate(forest)
            for c, v in enumerate(row)
            if v > 1
        )

        def bfs(cur, dest) -> int:
            q = deque([cur])
            seen = set()
            steps = 0
            n, m = len(forest), len(forest[0])
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if (x, y) == dest:
                        return steps
                    for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        dx, dy = x + d[0], y + d[1]
                        if (
                            0 <= dx < n
                            and 0 <= dy < m
                            and (dx, dy) not in seen
                            and forest[dx][dy] != 0
                        ):
                            seen.add((dx, dy))
                            q.append((dx, dy))
                steps += 1
            return -1

        start = (0, 0)
        ans = 0
        for _, r, c in sorted_forest:
            dist = bfs(start, (r, c))
            if dist == -1:
                return -1
            ans += dist
            start = (r, c)
        return ans
