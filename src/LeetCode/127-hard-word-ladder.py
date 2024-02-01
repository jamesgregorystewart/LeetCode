# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#
# Constraints:
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


from typing import List, Set


# DFS solution O(n*n!)
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         def dfs(word: str, path_length: int, remaining: Set[str]):
#             if word in remaining:
#                 remaining.remove(word)
#             nonlocal shortest_path
#             if word == endWord:
#                 shortest_path = min(shortest_path, path_length)
#                 return
#             for next_word in next_words(word, remaining):
#                 remaining.remove(next_word)
#                 dfs(next_word, path_length + 1, remaining)
#                 remaining.add(next_word)
#
#         def next_words(word, remaining):
#             for candidate in remaining:
#                 l, r = 0, len(word) - 1
#                 while l < r:
#                     if word[l] == candidate[l]:
#                         l += 1
#                     elif word[r] == candidate[r]:
#                         r -= 1
#                     else:
#                         break
#                 if l == r:
#                     yield candidate
#
#         shortest_path = 5002
#         dfs(beginWord, 1, set(wordList))
#         return shortest_path if shortest_path != 5002 else 0

import collections


# BFS solution O(m^2 * n) w/constraint could be O(n)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        adj_list = collections.defaultdict(list)
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                adj_list[word[:i] + "*" + word[i + 1 :]].append(word)

        def bfs(start, remaining):
            path_length = 1
            if start in remaining:
                remaining.remove(start)
            queue = collections.deque([start])
            while queue:
                band = len(queue)
                for _ in range(band):
                    word = queue.popleft()
                    for i in range(n):
                        intermediate_word = word[:i] + "*" + word[i + 1 :]
                        for next_word in adj_list[intermediate_word]:
                            if next_word == endWord:
                                return path_length + 1
                            if next_word in remaining:
                                queue.append(next_word)
                                remaining.remove(next_word)
                path_length += 1
            return 0

        return bfs(beginWord, set(wordList))


solution = Solution()
print(
    solution.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)
print(
    solution.ladderLength(
        beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
    )
)
print(
    solution.ladderLength(
        beginWord="leet",
        endWord="code",
        wordList=["lest", "leet", "lose", "code", "lode", "robe", "lost"],
    )
)
