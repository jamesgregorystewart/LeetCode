# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
#  
#
# Example 1:
#
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:
#
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:
#
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#  
#
# Constraints:
#
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.

from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjointset = DisjointSet(len(s))
        for pair in pairs:
            disjointset.union(pair[0], pair[1])
        # Identify the components; create independent maps of root to c/i
        root_to_characters_map = {}
        root_to_indices_map = {}
        for i in range(len(s)):
            if disjointset.find(i) not in root_to_characters_map:
                root_to_characters_map[disjointset.find(i)] = [s[i]]
                root_to_indices_map[disjointset.find(i)] = [i]
            else:
                root_to_characters_map[disjointset.find(i)].append(s[i])
                root_to_indices_map[disjointset.find(i)].append(i)
        res = [""] * len(s)
        # Independently sort the c/i in each component; zip them together
        for key in root_to_characters_map.keys():
            ordered_characters = sorted(root_to_characters_map[key])
            ordered_indices = sorted(root_to_indices_map[key])
            for i in range(len(ordered_characters)):
                res[ordered_indices[i]] = ordered_characters[i]
        return "".join(res)


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


solution = Solution()
print(solution.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
print(solution.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
print(solution.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))
