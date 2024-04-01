from collections import defaultdict
from functools import reduce
import unittest


class Trie:

    def __init__(self):
        T = lambda: defaultdict(T)
        self.t = T()

    def insert(self, word: str) -> None:
        reduce(dict.__getitem__, word, self.t)[True] = True

    def search(self, word: str) -> bool:
        node = self.t
        for c in word:
            if (node := node.get(c)) is None:
                return False
        return True in node

    def startsWith(self, prefix: str) -> bool:
        node = self.t
        for c in prefix:
            if (node := node.get(c)) is None:
                return False
        return True


class TestTrie(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

    def testInsert(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))

    def testStartsWith(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.startsWith("hell"))

    def testMissing(self):
        self.assertFalse(self.trie.search("world"))


if __name__ == "__main__":
    unittest.main()
