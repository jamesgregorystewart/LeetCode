# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
#
# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.
#
# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".
#
# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.
#
#
#
# Example 1:
#
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
#
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
#
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

from typing import List
import collections


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        # STEP 1: Build the adjacency and degree maps
        lex_order = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for i in range(1, len(words)):
            prev, cur = words[i - 1], words[i]
            min_length = min(len(prev), len(cur))
            lex_mapped = False
            # Go letter by letter mapping topographical mapping
            for j in range(min_length):
                if prev[j] != cur[j] and not lex_mapped:
                    lex_order[prev[j]].append(cur[j])
                    in_degree[prev[j]] += 0
                    in_degree[cur[j]] += 1
                    lex_mapped = True
                else:
                    in_degree[prev[j]] += 0
                    in_degree[cur[j]] += 0
            if len(prev) == len(cur):
                continue
            if not lex_mapped and len(prev) > len(cur):
                return ""
            longer_word = prev if len(prev) > len(cur) else cur
            # map rest of letters
            for c in longer_word[min_length:]:
                in_degree[c] += 0
        queue = collections.deque([k for k, v in in_degree.items() if v == 0])

        res = ""
        while queue:
            cur_letter = queue.popleft()
            res += cur_letter
            for next in lex_order[cur_letter]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    queue.append(next)

        return res if len(res) == len(in_degree.keys()) else ""


solution = Solution()
print(solution.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
print(solution.alienOrder(words=["z", "x"]))
print(solution.alienOrder(words=["z", "x", "z"]))
print(solution.alienOrder(words=["z", "z"]))
print(solution.alienOrder(words=["ab", "adc"]))
print(solution.alienOrder(words=["abe", "adcf"]))
