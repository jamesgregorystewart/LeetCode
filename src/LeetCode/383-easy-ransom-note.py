from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = Counter(ransomNote)
        magazine_letters = Counter(magazine)
        for k, v in ransom_letters.items():
            if k not in magazine_letters or v > magazine_letters[k]:
                return False
        return True
