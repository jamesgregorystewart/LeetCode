import collections
import functools


class WordDictionary:

    def __init__(self):
        T = lambda: collections.defaultdict(T)
        self.t = T()

    def addWord(self, word: str) -> None:
        functools.reduce(dict.__getitem__, word, self.t)[True] = True

    def search(self, word: str, node=None) -> bool:
        node = node if node else self.t
        wildcard_route = False
        for i, c in enumerate(word):
            if c == ".":
                for key in [k for k in node.keys() if k is not True]:
                    wildcard_route = self.search(word[i + 1 :], node.get(key))
                    if wildcard_route:
                        return True
            if (node := node.get(c)) is None:
                return False
        return True in node or wildcard_route
