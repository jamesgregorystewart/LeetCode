"""

 "MCMXCIV" 1994
 1) while iterator >= 0:
 2) if letter > prev; add part to res and start new part
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        sym_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = len(s) - 1
        result = 0
        part = 0
        prev = None
        while i >= 0:
            cur = sym_map[s[i]]
            if prev and cur > prev:
                result += part
                part = cur
            else:
                if not prev or cur == prev:
                    part += cur
                else:
                    part -= cur
            if i == 0:
                result += part
                break
            prev = cur
            i -= 1
        return result
