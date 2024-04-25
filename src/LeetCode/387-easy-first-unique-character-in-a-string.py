from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        i_map = {}
        d = defaultdict(int)
        for i, num in enumerate(s):
            i_map[num] = i
            d[num] += 1

        for num, count in d.items():
            if count == 1:
                return i_map[num]
        return -1
