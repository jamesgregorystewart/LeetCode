from typing import List
from collections import defaultdict


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # preprocess wordlist into encoded_map
        map = defaultdict(list)
        for word in wordSet:
            if word == beginWord:
                continue
            for i in range(len(word)):
                code = word[:i] + "*" + word[i + 1 :]
                map[code].append(word)

        def dfs(cur, path, seen, result) -> None:
            if cur == endWord:
                result[len(path)].append(path[:])
                self.min_path_length = min(self.min_path_length, len(path))
                return
            if len(path) >= self.min_path_length:
                return

            for i in range(len(cur)):
                code = cur[:i] + "*" + cur[i + 1 :]
                if code in map:
                    for word in map[code]:
                        if word not in seen:
                            path.append(word)
                            seen.add(word)
                            dfs(word, path, seen, result)
                            path.pop()
                            seen.remove(word)

        result = defaultdict(list)
        seen = set()
        self.min_path_length = float("inf")
        dfs(beginWord, [beginWord], seen, result)
        return result[self.min_path_length]
