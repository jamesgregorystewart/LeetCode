from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        target = image[sr][sc]
        if target == color:
            return image
        q = deque([(sr, sc)])
        image[sr][sc] = color
        n, m = len(image), len(image[0])
        while q:
            x, y = q.popleft()
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < n and 0 <= dy < m and image[dx][dy] == target:
                    image[dx][dy] = color
                    q.append((dx, dy))
        return image
