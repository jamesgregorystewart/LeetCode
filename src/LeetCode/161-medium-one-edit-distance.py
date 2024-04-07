"""
abcd  abde
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        edited = False
        si = ti = 0
        while si < len(s) and ti < len(t):
            if s[si] != t[ti]:
                if edited:
                    return False
                if len(s) < len(t):
                    # do an insert
                    ti += 1
                elif len(s) > len(t):
                    # do a deletion
                    si += 1
                else:
                    si, ti = si + 1, ti + 1
                edited = True
            else:
                si, ti = si + 1, ti + 1

        return abs(si - ti) <= 1
