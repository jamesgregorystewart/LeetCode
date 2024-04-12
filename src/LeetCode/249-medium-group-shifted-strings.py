from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strings:
            first_char = string[0]
            key = []
            for c in string:
                if c >= first_char:
                    key.append(ord(c) - ord(first_char))
                else:
                    key.append(ord(c) + 26 - ord(first_char))
            map[tuple(key)].append(string)

        return map.values()
