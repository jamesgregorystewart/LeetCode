# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
#
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# from typing import List, Dict
import collections
import functools


class Trie:
    def __init__(self):
        # Recursively create a nested defaultdict for each entry
        T = lambda: collections.defaultdict(T)
        self.t = T()

    def insert(self, word: str) -> None:
        # This will iterate through the chars in word, creating new entries in the dictionary
        # it will end by setting "True" or "1" for the last character as "True" which means
        # is a terminal character, and thus the end of a word.
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
        node = self.t
        for c in prefix:
            if (node := node.get(c)) is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)