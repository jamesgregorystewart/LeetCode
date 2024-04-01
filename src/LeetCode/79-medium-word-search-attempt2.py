from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        remaining = list(word[::-1])

        def backtrack(x, y, remaining, used) -> bool:
            if not remaining:
                return True

            n, m = len(board), len(board[0])
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            found = False
            for d in directions:
                dx, dy = d[0] + x, d[1] + y
                if (
                    0 <= dx < n
                    and 0 <= dy < m
                    and (dx, dy) not in used
                    and board[dx][dy] == remaining[-1]
                ):
                    letter = remaining.pop()
                    used.add((dx, dy))
                    found = backtrack(dx, dy, remaining, used)
                    if found:
                        return True
                    remaining.append(letter)
                    used.remove((dx, dy))
            return False

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == remaining[-1]:
                    letter = remaining.pop()
                    used = set()
                    used.add((i, j))
                    if backtrack(i, j, remaining, used):
                        return True
                    remaining.append(letter)
        return False
