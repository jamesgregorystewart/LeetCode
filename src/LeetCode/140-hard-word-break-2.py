from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()
        for word in wordDict:
            node = root
            for c in word:
                if c in node.children:
                    node = node.children[c]
                else:
                    new_node = TrieNode()
                    node.children[c] = new_node
                    node = new_node
            node.isWord = True

        def dfs(i, path, result):
            if i == len(s):
                result.append(" ".join(path))
                return

            node = root
            j = i
            builder = []
            while j < len(s) and s[j] in node.children:
                builder.append(s[j])
                node = node.children[s[j]]
                if node.isWord:
                    path.append("".join(builder))
                    dfs(j + 1, path, result)
                    path.pop()
                j += 1

        result = []
        dfs(0, [], result)
        return result
