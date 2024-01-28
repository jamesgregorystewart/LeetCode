# Tries

Balanced Trees and Hash Tables offer the possibility to search for a word in a dataset of strings. And though a hash table has O(1) time complexity for keys, it is not efficient when:
- finding all keys with a common prefix
- enumerating a dataset of strings in lexicographical order

Tries have an additional benefit of not having collisions, and thus not having a worst case time complexity break down to a linear-rhythmic figure, but instead is maxed at m, the length of the key. Search for a key in a balanced tree is O(mlogn)

A Trie will consist of nodes (or defaultdictionaries as we will see in our python solution) that point to children, and there is a terminal indicator which offers insight to where words are.

```python
class Trie:
    def __init__(self):
        # Recursively create a nested defaultdict for each entry
        T = lambda: collections.defaultdict(T)
        self.t = T()

    def insert(self, word: str) -> None:
        """
        This will iterate through the chars in word, creating new entries in the dictionary
        it will end by setting "True" or "1" for the last character as "True" which means
        is a terminal character, and thus the end of a word.
        """
        functools.reduce(dict.__getitem__, word, self.t)[True] = True

    def search(self, word: str) -> bool:
        node = self.t  # get the first dictionary of trie
        for c in word:
            # use := assignment in conditional
            # if key is not in dict then False
            if (node := node.get(c)) is None:
                return False
        # make sure that the last key has the terminal indicator for a complete word
        return True in node

    def startsWith(self, prefix: str) -> bool:
        # Same as search() but we don't care if last char is also end of a word
        node = self.t
        for c in prefix:
            if (node := node.get(c)) is None:
                return False
        return True
```

Trie with wilcards.
Problem: [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)

```python
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
                    wildcard_route = self.search(word[i + 1 :], node[key])
                    if wildcard_route:
                        return True
            if (node := node.get(c)) is None:
                return False
        return True in node or wildcard_route
```
