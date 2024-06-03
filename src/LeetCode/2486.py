class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr = 0

        for c in s:
            if ptr == len(t):
                return 0
            if t[ptr] == c:
                ptr += 1
        return len(t) - ptr
