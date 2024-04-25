class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        map = {}
        for i, c in enumerate(word):
            if ord(c) >= 97:
                map[c] = i
            elif c not in map:
                map[c] = i
        ans = 0
        for c, i in map.items():
            if ord(c) >= 97:
                upper = chr(ord(c) - 32)
                if upper in map:
                    upper_i = map[upper]
                    if upper_i > i:
                        ans += 1
        return ans
