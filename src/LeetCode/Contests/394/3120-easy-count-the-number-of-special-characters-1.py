class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        seen = set()
        ans = 0
        for c in word_set:
            if c in seen:
                continue
            if ord(c) >= 97:
                if chr(ord(c) - 32) in word_set:
                    ans += 1
                    seen.add(c)
        return ans
