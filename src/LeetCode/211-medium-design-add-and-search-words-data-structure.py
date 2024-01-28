# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

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
                # we will recursively iterate all possible paths at wildcards.
                for key in [k for k in node.keys() if k is not True]:
                    wildcard_route = self.search(word[i + 1 :], node[key])
                    if wildcard_route:
                        return True
            if (node := node.get(c)) is None:
                return False
        return True in node or wildcard_route


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
