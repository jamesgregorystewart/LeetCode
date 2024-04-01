import collections
import functools
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        n, m = len(board), len(board[0])
        ans = []
        for i in range(n):
            for j in range(m):
                letter = board[i][j]
                if letter in trie.t:
                    seen = set()
                    seen.add((i, j))
                    trie.searchBoard(i, j, trie.t.get(letter), letter, board, seen, ans)
        return list(set(ans))


class Trie:
    def __init__(self) -> None:
        T = lambda: collections.defaultdict(T)
        self.t = T()

    def insert(self, word) -> None:
        functools.reduce(dict.__getitem__, word, self.t)[True] = True

    def searchBoard(self, x, y, node, word, board, seen, ans) -> None:
        if True in node:
            ans.append(word)
        # search adjacent nodes; for each, check if it is a key in trie, if so, recurse
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n, m = len(board), len(board[0])
        for d in directions:
            dx, dy = d[0] + x, d[1] + y
            if (
                0 <= dx < n
                and 0 <= dy < m
                and board[dx][dy] in node
                and (dx, dy) not in seen
            ):
                seen.add((dx, dy))
                self.searchBoard(
                    dx,
                    dy,
                    node.get(board[dx][dy]),
                    word + board[dx][dy],
                    board,
                    seen,
                    ans,
                )
                seen.remove((dx, dy))
