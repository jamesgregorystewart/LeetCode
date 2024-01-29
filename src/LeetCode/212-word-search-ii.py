# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be seen more than once in a word.
#
#
#
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.


"""
Idea:
- read words into a trie
- iterate through cells of board checking if letter is at start of trie
- if so work through the trie, adding all neighbors which are keys into queue; when None is discovered add current word to result
    Alternatively, when multiple keys are discovered recursively call search with each node, and the current word;
"""


from typing import List, Set
import functools
import collections


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        results: Set[str] = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                node = trie.t
                if letter in node:
                    trie.add_words(
                        board, (i, j), node.get(letter), letter, set(), results
                    )
                if len(results) == len(words):
                    break
        return list(results)


class Trie:
    def __init__(self):
        T = lambda: collections.defaultdict(T)
        self.t = T()

    def insert(self, word: str):
        functools.reduce(dict.__getitem__, word, self.t)[True] = True

    def add_words(self, board, coord, node, word, seen, results):
        if True in node:
            results.add(word)
        seen.add(coord)
        for neighbor in self.neighbors(coord, board, node, seen):
            letter = board[neighbor[0]][neighbor[1]]
            next_node = node.get(letter)
            self.add_words(board, neighbor, next_node, word + letter, seen, results)
        seen.remove(coord)

    def neighbors(self, coord, board, node, seen):
        x, y = coord[0], coord[1]
        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for move in moves:
            next_row, next_col = x + move[0], y + move[1]
            if (
                0 <= next_row < len(board)
                and 0 <= next_col < len(board[0])
                and (next_row, next_col) not in seen
                and board[next_row][next_col] in node
            ):
                yield (next_row, next_col)


solution = Solution()
print(
    solution.findWords(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
)
print(solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
print(
    solution.findWords(
        board=[
            ["o", "a", "b", "n"],
            ["o", "t", "a", "e"],
            ["a", "h", "k", "r"],
            ["a", "f", "l", "v"],
        ],
        words=["oa", "oaa"],
    )
)
